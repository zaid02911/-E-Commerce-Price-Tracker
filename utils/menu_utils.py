from core import Database , PriceDatabase , CATEGORIES
from modules import ProductTracker , PriceScraper
from utils.formatting import FR
import time
class UI : 
    @staticmethod
    def display_main_menu():
        time.sleep(1) 
        print("\n" + "=" * 50)
        print("🏠 MAIN MENU")
        print("=" * 50)
        print("1. 📋 PRODUCT MANAGEMENT")
        print("   Add, view, edit, or remove tracked products")
        print("")
        print("2. 🔍 PRICE CHECKING")
        print("   Check prices, view history, and track changes")
        print("")
        print("3. 💾 DATA MANAGEMENT")
        print("   Import/export your tracking data")
        print("")
        print("0. 🚪 EXIT")
        print("   Save and exit the application")
        print("=" * 50)

        return input("\n🎯 Enter your choice (0-3): ")
    @staticmethod
    def data_management_menu():
        time.sleep(1) 
        print("\n" + "=" * 50)
        print("💾 DATA MANAGEMENT")
        print("=" * 50)
        print("1. 📤 EXPORT DATA")
        print("   Save your tracked products to CSV or Excel")
        print("")
        print("2. 📥 IMPORT DATA")
        print("   Load products from a CSV or Excel file")
        print("")
        print("0. ↩️  BACK TO MAIN MENU")
        print("=" * 50)

        choice = input("\n🎯 Enter your choice (0-2): ")

        # Validate input (optional)
        while choice not in ["1", "2", "0"]:
            print("Invalid choice. Please choose again.")
            choice = input("Enter your choice: ")
        if choice =="0":
            return
        elif choice == "2":
            print("Please ensure your file contains the following headers in this exact order:")
            print("id,product_id,name, url, store, category, target, status")
        filepath=input("Enter your file path : ")

        f_type=filepath.split(".")[-1]
        while f_type not in ["xlsx","csv"] :
            print("THE file type should be .csv or .xlsx")
            if choice == 2:
                print("Please ensure your file contains the following headers in this exact order:")
                print("id,product_id,name, url, store, category, target, status")
            filepath=input("Enter your file path : ")
            f_type=filepath.split(".")[-1]
        match choice :
            case "1":
                Database.save_data_as(filepath,f_type)
            case "2" :
                Database.import_data_from(filepath,f_type)
            
    @staticmethod
    def price_tracker_menu():
        time.sleep(1) 
        while True:
            print("\n" + "=" * 50)
            print("🔍 PRICE CHECKING")
            print("=" * 50)
            print("1. 🔄 CHECK ALL PRICES")
            print("   Check current prices for all tracked products")
            print("")
            print("2. 🔍 CHECK SPECIFIC PRODUCT")
            print("   Check price for a single product by ID")
            print("")
            print("3. 📊 VIEW ALL PRICE HISTORY")
            print("   See all price records across all products")
            print("")
            print("4. 📈 VIEW PRODUCT HISTORY")
            print("   See price history for a specific product")
            print("")
            print("0. ↩️  BACK TO MAIN MENU")
            print("=" * 50)

            choice = input("\n🎯 Enter your choice (0-4): ")
            while choice not in ["1", "2","0","3","4"]:
                print("❌ Invalid choice. Please choose 0-4.")
                choice = input("\n🎯 Enter your choice (0-4): ")
            if choice=='0':
                print("\n↩️  Returning to main menu...")
                return
            match choice :
                case "1":
                    PriceScraper.check_all_prices()
                case "2":
                    print("\n" + "=" * 50)
                    print("🔍 CHECK SPECIFIC PRODUCT")
                    print("=" * 50)
                    print("💡 Find the Product ID in Product Management menu")
                    print("-" * 50)
                    product_id=input("🆔 Enter Product ID (or 'Q' to quit): ").strip()
                    if product_id.lower() == 'q':
                        continue
                    if not product_id:
                        print("❌ Product ID cannot be empty")
                        continue
                    print(f"\n🔍 Checking product {product_id}...")
                    PriceScraper.check_product_price(product_id)
                case "3":
                    print("\n" + "=" * 50)
                    print("📊 ALL PRICE HISTORY")
                    print("=" * 50)
                    print("📈 Loading all price records...")
                    print("-" * 50)
                    data=PriceDatabase.get_all_price_data()
                    FR.price_history(data)
                case "4":
                    print("\n" + "=" * 50)
                    print("📈 PRODUCT PRICE HISTORY")
                    print("=" * 50)
                    print("💡 Find the Product ID in Product Management menu")
                    print("-" * 50)
                    product_id = input("🆔 Enter Product ID (or 'Q' to quit): ").strip()
                    if product_id.lower() == 'q':
                        continue

                    if not product_id:
                        print("❌ Product ID cannot be empty")
                        continue

                    print(f"\n📈 Loading price history for {product_id}...")
                    data=PriceDatabase.get_price_history(product_id)
                    FR.product_price_history(data)

    @staticmethod
    def display_product_tracker_menu():
        time.sleep(1) 
        Database().create_tables()
        while True :
            print("\n" + "=" * 50)
            print("📋 PRODUCT MANAGEMENT")
            print("=" * 50)
            print("1. ➕ ADD NEW PRODUCT")
            print("   Start tracking a new product")
            print("")
            print("2. 👁️  VIEW ALL PRODUCTS")
            print("   See all products you're tracking")
            print("")
            print("3. 🗑️  REMOVE PRODUCT")
            print("   Stop tracking a product")
            print("")
            print("4. ✏️  EDIT PRODUCT")
            print("   Update product details or target price")
            print("")
            print("0. ↩️  BACK TO MAIN MENU")
            print("=" * 50)
            choice = input("\n🎯 Enter your choice (0-4): ")
            while choice not in ["1", "2","4","3","0"]:
                print("Invalid choice. Please choose again.")
                choice = input("\n🎯 Enter your choice (0-4): ")
            match choice:
                case "1":
                    ProductTracker.add_product()
                case "2":
                    FR.list_products()
                case "3":
                    ProductTracker.remove_product()
                case "4":
                    ProductTracker.edit_product()
                case "0":
                    print("\n↩️  Returning to main menu...")
                    return
