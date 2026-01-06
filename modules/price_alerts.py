from plyer import notification
import re
from core import PriceDatabase, Database
class PriceAlerts:
    def check_changes():
        data=Database.get_all_data()
        for tuple in data :
            # tuple(id,product_id,name,url,store_name,category,target,out_of_stock)
            PriceAlerts.check_price_drop(tuple[1],tuple)
    
    def check_price_drop(product_id,product):
        data=PriceDatabase.get_price_history(product_id)
        target=product[6]
        price =re.findall(r'\d+\.?\d*', data[0][1])[0]
        if float(price) <= float(target) :
            PriceAlerts.send_desktop_alert(product[2],price,target)
        return
        #Compare with target price

 
    def send_desktop_alert(product_name, price, target):
        try:
            notification.notify(
                title=f"🎉 PRICE DROP ALERT: {product_name[:30]}...",
                message=f"💰 Current Price: ${price:.2f}\n🎯 Target Price: ${target:.2f}\n✅ Time to buy!",
                timeout=15,
                app_name="Price Tracker"
            )
            print(f"   📢 Desktop notification sent!")
            print(f"   🛒 Product: {product_name[:30]}...")
            print(f"   💰 Price: ${price:.2f} (Target: ${target:.2f})")
        except Exception as e:
            print(f"   ⚠️  Could not send desktop notification: {str(e)}")
            print(f"   📢 Price drop alert for {product_name[:30]}...")
            print(f"   💰 Price: ${price:.2f} is at/below target: ${target:.2f}")
