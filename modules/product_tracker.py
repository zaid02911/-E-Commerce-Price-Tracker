from core import Database , ValidationInputs, CATEGORIES,STORES
from utils.formatting import FR
import time
import uuid
class ProductTracker:
    @staticmethod
    def add_product():
        time.sleep(1)
        print("\n" + "=" * 60)
        print("➕ ADD NEW PRODUCT")
        print("=" * 60)
        print("📝 Please enter the following details:")
        print("-" * 60)

        name = input("1️⃣ Product Name: ")
        print("💡 Tip: Enter the exact product page URL for accurate tracking. Otherwise, tracking will not work.")
        url = input("2️⃣ Product URL: ")
        FR.print_list(STORES)
        store = input("3️⃣ Store (from list above): ")
        target = input("4️⃣ Target Price: ")
        print("\n📂 Available Categories:")
        print("-" * 30)
        FR.print_list(CATEGORIES)
        print("-" * 30)
        category = input("5️⃣  Category (from list above): ")

        print("\n" + "=" * 60)
        print("🔍 Reviewing your information...")
        print("=" * 60)
        if ValidationInputs.validate_all(url, category, name, target, store):
            product = {
                "id": str(uuid.uuid4())[:8],
                "name": name.strip(),
                "url": url.strip(),
                "store": store.strip(),
                "target": target.strip(),
                "category": category.strip(),
                "status": "Unknown",
            }

            print("\n💾 Saving product to database...")
            if Database.add_product(product):
                print("\n✅ PRODUCT ADDED SUCCESSFULLY!")
                print(f"   📍 Product ID: {product['id']}")
                print(f"   📛 Name: {name[:40]}...")
                print(f"   🎯 Target: ${target}")
                print("=" * 60)
                time.sleep(1)
            else:
                print("\n❌ Failed to add product. Please try again.")
        else:
            print("\n❌ Product validation failed. Please try again.")
            retry = input("\n↩️  Press Enter to try again or 'Q' to quit: ").lower()
            if retry != 'q':
                ProductTracker.add_product()

        # Add new product to track


    @staticmethod
    def remove_product():
        time.sleep(1)        
        print("\n" + "=" * 60)
        print("🗑️  REMOVE PRODUCT")
        print("=" * 60)
        print("💡 Tip: View all products first to find the Product ID")
        print("-" * 60)
        while True:
            product_id = input("🆔 Enter Product ID to remove (or 'Q' to quit): ").strip()

            if product_id.lower() == 'q':
                print("\n↩️  Returning to menu...")
                return
            product_data = Database.get_product_data(product_id)
            if not product_data:
                print(f"\n❌ No product found with ID: {product_id}")
                continue
            print(f"\n⚠️  CONFIRM REMOVAL")
            print("=" * 40)
            print(f"📛 Product: {product_data[2]}")
            print(f"🏪 Store: {product_data[4]}")
            print(f"📂 Category: {product_data[5]}")
            print("=" * 40)

            confirm = input("\n❓ Are you sure you want to remove this product? (y/N): ").lower()
            if confirm=='y':
                Database().remove_product(product_id)
                print("🗑️  Removing product...")
                time.sleep(1)
                print("✅ Product removed successfully!")
            else :
                print("\n↩️  Removal cancelled")

            another = input("\n❓ Remove another product? (y/N): ").lower()
            if another != 'y':
                print("\n↩️  Returning to menu...")
                return
        # Stop tracking product

    @staticmethod
    def edit_product():
        time.sleep(1) 
        print("\n📋 EDIT PRODUCT DETAILS")
        print("=" * 30)
        print("💡 Tip: To find the product ID, first view all tracked products.")
        print("   Then copy the ID of the product you want to edit.\n")
        product_id = input("🆔 Enter the Product ID to edit: ")
        print("\n✏️  EDIT OPTIONS")
        print("=" * 30)
        print("A. 📛 Edit product name")
        print("B. 🔗 Edit product URL")
        print("C. 🎯 Edit target price")
        print("D. 📁 Edit category")
        print("E. 🏪 Edit store")
        print("F. 📝 Edit all details")
        print("G. ↩️  Back to menu")
        print("-" * 30)
        choice = input("Enter a letter between A and G: ").upper()
        while choice not in ["A", "B","C","D","E","F","G"]:
            print("Invalid choice. Please choose again.")
            choice = input("Enter a letter between A and G: ").upper()
        match choice:
            case "A":
                Database.update_product(product_id,"name",input("1️⃣ Product Name: "))
            case "B":
                Database.update_product(product_id,"url",input("1️⃣ Product URL: "))
            case "C":
                Database.update_product(product_id,"target",input("4️⃣ Target Price: "))
            case "D":
                Database.update_product(product_id,"category",input("5️⃣ Category: ").upper())
            case "E":
                Database.update_product(product_id,"store",input("3️⃣ Store (Amazon/eBay/etc.): ").upper())
            case "F":
                Database.update_product(product_id,"name",input("1️⃣ Product Name: ").upper())
                Database.update_product(product_id,"url",input("1️⃣ Product URL: "))
                Database.update_product(product_id,"store",input("3️⃣ Store (Amazon/eBay/etc.): ").upper())
                Database.update_product(product_id,"target",input("4️⃣ Target Price: "))
                Database.update_product(product_id,"category",input("5️⃣ Category: ").upper())
            case "G":
                return
