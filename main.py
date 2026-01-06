import sys
from utils import UI
from modules import PriceAlerts
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "auto":
        print("🔔 Running automatic price alert check...")
        PriceAlerts.check_changes()
        return
    print("=" * 50)
    print("🛒  E-COMMERCE PRICE TRACKER  📊")
    print("=" * 50)
    print("📈 Track prices • Set alerts • Save money")
    print("=" * 50)

    # Display main menu and handle user choice
    while True:
        user_choice = UI.display_main_menu()
        while user_choice not in ["1", "2","0","3"]:
                print("❌ Invalid choice. Please try again.")
                user_choice = input("\n🎯 Enter your choice (0-3): ")
        match user_choice:
            case "1":
                UI.display_product_tracker_menu()
            case "2":
                UI.price_tracker_menu()
            case "3":
                UI.data_management_menu()
            case "0":
                print("\n" + "=" * 40)
                print("👋 Thank you for using Price Tracker!")
                print("💾 Your data has been saved.")
                print("=" * 40)
                return
                

if __name__ == "__main__":
    main()