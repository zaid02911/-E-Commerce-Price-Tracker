from core import Database
import time

class FR:
    @staticmethod
    def print_list(items):
        """Print a formatted list of items."""
        if not items:
            print("   📭 No items to display")
            return

        max_len = max(len(str(item)) for item in items) + 5
        items_per_line = 60 // max_len

        for i, item in enumerate(items, start=1):
            print(f"   {i:2}. {item}", end="")

            # Add spacing for alignment
            spaces_needed = max_len - len(str(item))
            print(" " * spaces_needed, end="")

            # New line after certain number of items
            if i % items_per_line == 0:
                print()

        if len(items) % items_per_line != 0:
            print()

    @staticmethod
    def list_products():
        """Display all tracked products in a formatted table."""
        print("\n" + "=" * 80)
        print("📋 TRACKED PRODUCTS")
        print("=" * 80)
        print("🔄 Loading products from database...")
        print("-" * 80)

        time.sleep(1)
        db = Database.get_all_data()

        if not db:
            print("\n📭 No products found in database.")
            print("💡 Add your first product using 'Add new product' option")
            print("=" * 80)
            return

        # Header
        header_format = "{:<5} {:<25} {:<15} {:<15} {:<10} {:<10}"
        print(header_format.format(
            "#", "📛 Product Name", "🏪 Store", "📂 Category", "🎯 Target", "📦 Status"
        ))
        print("-" * 80)

        # Product rows
        for i, product in enumerate(db, 1):
            product_name = product[2]
            if len(product_name) > 22:
                product_name = product_name[:22] + "..."

            store = product[4]
            if len(store) > 12:
                store = store[:12] + "..."

            category = product[5]
            if len(category) > 12:
                category = category[:12] + "..."

            target = f"${float(product[6]):.2f}"

            status = product[7]
            if status == "1" or status == "In Stock":
                status_display = "✅ In Stock"
            elif status == "0" or status == "Out of Stock":
                status_display = "❌ Out of Stock"
            else:
                status_display = "❓ Unknown"

            print(header_format.format(
                f"{i:2}.",
                product_name,
                store,
                category,
                target,
                status_display
            ))

            # Show product ID every few rows or on request
            if i <= 5 or i == len(db):
                print(f"     🆔 ID: {product[1]} | 🔗 URL: {product[3][:50]}...")
                print("-" * 80)
            elif i % 5 == 0:
                print("     ...")
                print("-" * 80)

        # Footer
        print(f"\n📊 TOTAL: {len(db)} product{'s' if len(db) != 1 else ''}")
        print("💡 Tip: Use the Product ID for editing or removing products")
        print("=" * 80)
        time.sleep(1)

    @staticmethod
    def product_price_history(data):
        """Display price history for a specific product."""
        if not data:
            print("\n📭 No price history found for this product")
            print("💡 Try checking the price first using 'Check specific product price'")
            return

        product_name = data[0][0]
        print("\n" + "=" * 50)
        print(f"📈 PRICE HISTORY: {product_name[:40]}...")
        print("=" * 50)

        # Header
        print(f"{'📅 Date':<20} | {'💰 Price':<15}")
        print("-" * 40)

        # Price entries
        for price_data in data:
            date_str = price_data[2]
            price_str = price_data[1]

            # Format date nicely
            if " " in date_str:
                date_part = date_str.split(" ")[0]
            else:
                date_part = date_str

            # Try to parse and format price
            try:
                price_num = float(''.join(filter(lambda x: x.isdigit() or x == '.', price_str)))
                formatted_price = f"${price_num:.2f}"
            except:
                formatted_price = price_str

            print(f"{date_part:<20} | {formatted_price:<15}")

        # Summary
        print("-" * 40)
        print(f"📊 Total records: {len(data)}")

        # Calculate price change if enough data
        if len(data) >= 2:
            try:
                latest = float(''.join(filter(lambda x: x.isdigit() or x == '.', data[0][1])))
                oldest = float(''.join(filter(lambda x: x.isdigit() or x == '.', data[-1][1])))
                change = latest - oldest
                change_pct = (change / oldest) * 100

                print(f"📉 Price change: ${change:+.2f} ({change_pct:+.1f}%)")

                if change < 0:
                    print("📉 Trend: Decreasing")
                elif change > 0:
                    print("📈 Trend: Increasing")
                else:
                    print("➡️  Trend: Stable")
            except:
                pass

        print("=" * 50)

    @staticmethod
    def price_history(data):
        """Display all price history records."""
        if not data:
            print("\n📭 No price history records found")
            return

        print("\n" + "=" * 80)
        print("📊 ALL PRICE HISTORY")
        print("=" * 80)
        print(f"📈 Found {len(data)} price record{'s' if len(data) != 1 else ''}")
        print("-" * 80)

        # Header
        header_format = "{:<30} {:<15} {:<20} {:<10}"
        print(header_format.format("📛 Product", "💰 Price", "📅 Date", "🆔 ID"))
        print("-" * 80)

        # Limit display to avoid overwhelming
        display_limit = min(50, len(data))

        for i, record in enumerate(data[:display_limit], 1):
            product_name = record[1]
            if len(product_name) > 27:
                product_name = product_name[:27] + "..."

            price_str = record[3]
            try:
                price_num = float(''.join(filter(lambda x: x.isdigit() or x == '.', price_str)))
                formatted_price = f"${price_num:.2f}"
            except:
                formatted_price = price_str

            date_str = record[4]
            if " " in date_str:
                date_part = date_str.split(" ")[0]
                time_part = date_str.split(" ")[1][:5]
                formatted_date = f"{date_part} {time_part}"
            else:
                formatted_date = date_str

            product_id = record[2][:8] + "..." if len(record[2]) > 8 else record[2]

            print(header_format.format(
                product_name,
                formatted_price,
                formatted_date,
                product_id
            ))

        # Show more info if there are more records
        if len(data) > display_limit:
            print("-" * 80)
            print(f"📋 Showing {display_limit} of {len(data)} records")
            print("💡 Use 'View specific product price history' for detailed view")

        print("=" * 80)
