import sqlite3
import csv
import pandas as pd
DB_PATH="data/database.sqlite"
class Database:
    
    @staticmethod
    def save_data_as(filepath ,f_type):
        print(f"\n💾 Exporting data to {f_type.upper()} file...")
        print(f"   📁 Destination: {filepath}")
        Database.create_tables()
        data=Database.get_all_data()
        header=["id","product_id","name","url","store","category","target","status"]
        if f_type=="csv":
            try:
                with open(filepath, "w", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(data)
                print(f"   ✅ Successfully exported {len(data)} products to CSV")

            except Exception as e:
                print(f"   ❌ Failed to export to CSV: {str(e)}")
        else:
            try:
                df = pd.DataFrame(data, columns=header)
                df.to_excel(filepath, index=False)
                print(f"   ✅ Successfully exported {len(data)} products to Excel")
            except Exception as e:
                print(f"   ❌ Failed to export to Excel: {str(e)}")

    @staticmethod
    def import_data_from(filepath ,f_type) :
        print(f"\n📥 Importing data from {f_type.upper()} file...")
        print(f"   📁 Source: {filepath}")
        Database.create_tables()
        try:
            if f_type == "csv":
                with open(filepath, "r", encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header

                    with sqlite3.connect(DB_PATH) as conn:
                        cur = conn.cursor()
                        count = 0
                        for row in reader:
                            if len(row) >= 7:
                                cur.execute("""
                                    INSERT INTO products VALUES (NULL,?,?,?,?,?,?,?)
                                """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                                count += 1
                        conn.commit()
                print(f"   ✅ Successfully imported {count} products from CSV")
            else:
                with sqlite3.connect(DB_PATH) as conn:
                    df = pd.read_excel(filepath)
                    count = len(df)
                    df.to_sql("products", conn, if_exists="append", index=False)
                print(f"   ✅ Successfully imported {count} products from Excel")

        except Exception as e:
            print(f"   ❌ Import failed: {str(e)}")

    @staticmethod
    def create_tables():
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_id TEXT  NOT NULL,
                        name TEXT NOT NULL,
                        url  TEXT NOT NULL,
                        store TEXT NOT NULL,
                        category TEXT ,
                        target  INTEGER ,
                        status TEXT
                        );
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS product_prices (
                        price_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_name TEXT NOT NULL,
                        product_id TEXT NOT NULL,
                        price Text NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (product_id) REFERENCES products(product_id),
                        FOREIGN KEY (product_name) REFERENCES products(name)
                    );
                    """
                )
                cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cur.fetchall()
                if len(tables) >= 2:
                        print("✅ Database tables are ready")
                else:
                        print("⚠️  Database initialization may have issues")
        except Exception as e:
            print(f"❌ Database error: {str(e)}")
    @staticmethod
    def add_product(product_values):
        print(f"\n➕ Adding product: {product_values['name'][:40]}...")
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute(
                    """
                    INSERT INTO products(product_id,name,url,store,category,target,status) Values(?,?,?,?,?,?,?)""",
                    (
                        product_values["id"],
                        product_values["name"],
                        product_values["url"],
                        product_values["store"],
                        product_values["category"],
                        product_values["target"],
                        product_values["status"],
                    ),
                )
            print(f"   ✅ Product added successfully (ID: {product_values['id']})")
            return True
        except Exception as e:
            print(f"   ❌ Failed to add product: {str(e)}")
            return False
    @staticmethod
    def update_product(product_id,column_name,value):
        print(f"\n✏️  Updating product {product_id}...")
        print(f"   📝 Setting {column_name} = {value}")
        try:
            with sqlite3.connect(DB_PATH) as conn :
                cur=conn.cursor()

                cur.execute(f"""
                    UPDATE products
                    SET {column_name} = ?
                    WHERE product_id= ?""",(value,product_id,),)
        except Exception as e:
            print(f"   ❌ Update failed: {str(e)}")

    @staticmethod
    def remove_product(product_id):
        print(f"\n🗑️  Removing product ID: {product_id}")
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()

                # Get product name before deleting
                cur.execute("SELECT name FROM products WHERE product_id = ?", (product_id,))
                product = cur.fetchone()

                if product:
                    print(f"   📛 Product: {product[0]}")

                    # Delete from products table
                    cur.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
                    products_deleted = cur.rowcount

                    # Delete from price history
                    cur.execute("DELETE FROM product_prices WHERE product_id = ?", (product_id,))
                    prices_deleted = cur.rowcount

                    conn.commit()
                    print(f"   ✅ Removed {products_deleted} product(s) and {prices_deleted} price record(s)")
                else:
                    print(f"   ⚠️  No product found with ID: {product_id}")

        except Exception as e:
            print(f"   ❌ Failed to remove product: {str(e)}")
    @staticmethod
    def get_all_data():
        data=None
        try :
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()

                # Select all rows
                cur.execute("SELECT * FROM products")

                # Fetch all results
                rows = cur.fetchall()
                data=rows
                if rows:
                        print(f"   📊 Retrieved {len(rows)} product(s) from database")
                else:
                        print("   📭 No products found in database")
                return  data
        except Exception as e:
            print(f"   ❌ Database error: {str(e)}")
            return []

    def get_product_data(product_id):
        tpl=None
        try:
            with sqlite3.connect(DB_PATH) as conn :
                cur=conn.cursor()
                cur.execute("""
                    Select *
                    From products
                    where  product_id = ?""",(product_id,))
                row=cur.fetchall()
                tpl=row
            return tpl[0]
        except Exception as e:
            print(f"   ❌ Database error: {str(e)}")
            return None
class PriceDatabase:
    @staticmethod
    def save_price(product_id,product_name, price):
        if not price :
            print(f"   ⚠️  Skipping price save - no valid price found")
            return
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO product_prices(product_id,product_name,price)
                    VALUES(?,?,?)
                """, (product_id, product_name, price))
            print(f"   💾 Price saved to history: ${price}")
        except Exception as e:
            print(f"   ❌ Failed to save price: {str(e)}")
        # Store price in history
    @staticmethod
    def get_price_history(product_id):
        print(f"\n📈 Retrieving price history for product {product_id}...")

        data=PriceDatabase.get_all_price_data()
        price_history=[]
        for tuple in data :
            if tuple[2] == product_id :
                # tuple(name,price ,date)
                tpl=(tuple[1],tuple[3],tuple[4])
                price_history.append(tpl)
        print(f"   📊 Found {len(price_history)} price record(s)")
        return price_history
        # Get historical prices
    def get_all_price_data():
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM product_prices ORDER BY timestamp DESC")
                rows = cur.fetchall()
                return rows
        except Exception as e:
            print(f"   ❌ Database error: {str(e)}")
            return []



