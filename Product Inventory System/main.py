# Product Inventory System
import mysql.connector as mydb


class Productinventorysystem:
    def __init__(self):
        self.conn = mydb.connect(
            user="root",
            password="your_pass",
            database = "your_database"
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id  INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                price INTEGER NOT NULL,
                quantity_in_stock INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_product(self,product_id, name, price, quantity_in_stock):
        self.cursor.execute("""
            INSERT INTO products (product_id, name, price, quantity_in_stock)
            VALUES (%s, %s, %s, %s)
        """, (product_id, name, price, quantity_in_stock))
        self.conn.commit()

    def update_product(self, product_id, quantity_in_stock):
        self.cursor.execute("""
            UPDATE products
            SET qualntity_in_stock =  %s
            WHERE product_id = %s
        """, (quantity_in_stock, product_id))
        self.conn.commit()

    def delete_products(self, product_id):
        self.cursor.execute("""
            DELETE FROM products
            WHERE product_id = %s
        """, (product_id,))
        self.conn.commit()

    def low_products(self):
        self.cursor.execute("""
            SELECT name FROM products
            WHERE  quantity_in_stock < 5
        """)
        names = self.cursor.fetchall()
        for name in names:
            print(name)

    def total_values(self):
        self.cursor.execute("""
            SELECT SUM(price * quantity_in_stock) FROM products
        """)
        values = self.cursor.fetchall()
        print(values)


def main():
    ems = Productinventorysystem()
    ems.create_table()
    while True:
        print("Product Inventory System")
        print("1. Add Products")
        print("2. Low Products")
        print("3. Update Products")
        print("4. Total Values Products")
        print("5. Delete Products")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = int(input("Enter Product Price: "))
            quantity_in_stock = input("Enter Product Quantity ")
            ems.add_product(product_id,name, price, quantity_in_stock)

        elif choice == 2:
            ems.low_products()

        elif choice == 3:
            product_id = int(input("Enter Product ID: "))
            quantity_in_stock = int(input("Enter Product Quantity: "))
            ems.update_product(product_id, quantity_in_stock)

        elif choice == 4:
            ems.total_values()

        elif choice == 5:
            product_id = int(input("Enter Product ID: "))
            ems.delete_products(product_id)

        elif choice == 6:
            print("Exit the Program...")
            break

        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()



