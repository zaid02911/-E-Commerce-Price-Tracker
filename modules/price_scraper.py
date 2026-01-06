from httpcore import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
from core import Database ,PriceDatabase
import time
import random



JSON_PATH="data/sites.json"

with open(JSON_PATH, "r") as f:
    SITE_CONFIG = json.load(f)
class PriceScraper:
    
    @staticmethod
    def extract_price(html_content,url):
        store=PriceScraper.get_store_name(url)
        sites = SITE_CONFIG
        if store in sites.keys():
            dict=sites[store]["price"]
            soup=BeautifulSoup(html_content,"html.parser")
            price=""
            if dict["tag"]=="script":
                script = soup.find("script", type=dict["name"])
                data=json.loads(script.string)
                if isinstance(data, list):
                    price = data["offers"]["offers"][0][dict["value"]]
                else:
                    price = data["offers"][dict["value"]]
            elif dict["tag"]=="meta":
                data=soup.find(dict["tag"],itemprop=dict["value"])
                price=data.get("content")
            if price !=None :
                return price
        return ""
    
    @staticmethod
    def check_all_prices():
        print("\n" + "=" * 50)
        print("🔄 Checking prices for all products...")
        print("⏳ This may take a few minutes depending on the number of products.")
        print("⚠️  Please do not close the editor.")
        print("=" * 50)
        driver=PriceScraper.create_driver()

        Database.create_tables()
        data=Database.get_all_data()
        if not data:
            print("❌ No products found to track. Please add products first.")
            driver.quit()
            return
        try:
            for tuple in data : 
                time.sleep(random.uniform(5,10))  
                url=tuple[3]
                html_content=PriceScraper.get_html_content(driver,url)
                product_name=tuple[2]
                product_id=tuple[1]
                status=PriceScraper.check_availability(html_content,url)
                price=PriceScraper.extract_price(html_content,url)
                print(f"[{product_name}] Price: {price} | Status:{status}")
                print("")
                Database.update_product(product_id,"status",status)
                PriceDatabase.save_price(product_id,product_name,price)
        finally:
            driver.quit()   

    def check_product_price(product_id):
        try:
            print("Scrapping...")
            driver=PriceScraper.create_driver()
            tpl=Database.get_product_data(product_id)
            print(tpl)
            url=tpl[3]
            product_name=tpl[2]
            html_content=PriceScraper.get_html_content(driver,url)
            status=PriceScraper.check_availability(html_content,url)
            price=PriceScraper.extract_price(html_content,url)
            print(f"[{product_name}] Price: {price} | Status: {status}")
            Database.update_product(product_id,"status",status)
            PriceDatabase.save_price(product_id,product_name,price)
        finally:
            driver.quit()  
    @staticmethod
    def check_availability(html_content,url):
        store=PriceScraper.get_store_name(url)
        sites = SITE_CONFIG
        if store in sites.keys():
            dict=sites[store]["stock"]
            soup=BeautifulSoup(html_content,"html.parser")
            availability=""
            if dict["value"]=="InStock":
                return "InStock"
            elif dict["tag"]=="script":
                script = soup.find("script", type=dict["name"])
                data=json.loads(script.string)
                if isinstance(data, list):
                    availability = data["offers"]["offers"][0][dict["value"]]
                else:
                    availability = data["offers"][dict["value"]]
            elif dict["tag"]=="meta":
                data=soup.find(dict["tag"],itemprop=dict["value"])
                availability=data.get("content")
            if availability !=None :
                return availability.split("/")[-1]
        return ""

    
    
    
    @staticmethod
    def get_html_content(driver,url):
        try:
            driver.get(url)

        # Try to wait for JSON-LD, but don't fail if it's missing
            try:
                WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//script[@type='application/ld+json']")
                )
            )
            except TimeoutException:
                pass  # JSON-LD not present, continue normally

            return driver.page_source
        except Exception as e:
            
            print(f"[ERROR] Failed to load {url}: {e}")
            return ""
   
   
    @staticmethod
    def get_store_name(url):
        store_name=url.split(".")[1]
        return store_name
    @staticmethod
    def create_driver():
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(10)
        return driver
