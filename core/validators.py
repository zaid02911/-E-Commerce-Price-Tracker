import requests
from .constants import CATEGORIES ,STORES
class ValidationInputs :
    def validate_all (url,category,name,target,store):
        print("\n🔍 Validating input data...")
        print("-" * 40)
        flags=[]
        flags.append(ValidationInputs.validate_name(name) )
        flags.append(ValidationInputs.validate_storeName(store))
        flags.append(ValidationInputs.validate_url(url))
        flags.append(ValidationInputs.validate_category(category))
        flags.append(ValidationInputs.validate_corrency(target))
        if all(flags):
            print("\n✅ All validations passed successfully!")
            print("-" * 40)
            return True
        else:
            print("\n❌ Validation failed. Please correct the errors above.")
            print("-" * 40)
            return False

    @staticmethod
    def validate_url(url):
        print(f"   🔗 Validating URL: {url[:60]}...")

        if not url.startswith(("http://", "https://")):
            print("   ⚠️  Adding missing protocol (https://)")
            url = "http://" + url  # auto-fix missing scheme

        try:
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            response = requests.head(url,headers=headers, timeout=5)
            if response.status_code < 400:
                print("   ✅ URL is valid and accessible")
                return True
            else:
                print(f"   ❌ URL returned error code: {response.status_code}")
                return False
        except requests.RequestException as e:
                print(f"   ❌ Cannot access URL: {str(e)[:50]}")
                return False
    @staticmethod
    def validate_category(category):
        print(f"   📂 Validating category: {category}")
        category_names = [
        item.split(" ", 1)[1].upper()
        for item in CATEGORIES
        ]
        if category.upper() not in category_names:
            print("   ❌ Category not found in list")
            print("   📋 Available categories:")
            for i, cat in enumerate(CATEGORIES, 1):
                cat.split(" ")[-1].upper()
                print(f"      {i:2}. {cat}")
            return False
        print(f"   ✅ Category '{category}' is valid")
        return True
    @staticmethod
    def validate_corrency(price):
        print(f"   💰 Validating price: {price}")

        try:
            price_value = float(price)
            if price_value <= 0:
                print("   ❌ Price must be greater than 0")
                return False
            print(f"   ✅ Price is valid: {price_value:.2f}")
            return True
        except ValueError:
            print("   ❌ Price must be a valid number (e.g., 29.99)")
            return False
    @staticmethod
    def validate_name(name):
        """Validate product name is not empty."""
        print(f"   📛 Validating product name...")

        if not name or name.strip() == "":
            print("   ❌ Product name cannot be empty")
            return False

        print(f"   ✅ Product name is valid: {name[:30]}...")
        return True
    @staticmethod
    def validate_storeName(store):
        """Validate store name is not empty."""
        print(f"   🏪 Validating store name...")

        if not store or store.strip() == "":
            print("   ❌ Store name cannot be empty")
            return False

        if store.upper() not in [item.upper() for item in STORES]:
            print("   ❌ Store not found in list")
            print("   📋 Available Stores:")
            for i, st in enumerate(STORES, 1):
                print(f"      {i:2}. {st}")
            return False
        print(f"   ✅ Store name is valid: {store}")
        return True
