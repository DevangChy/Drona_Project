# Customer Order System 
import mysql.connector as mydb

class Customerordersystem:
    def __init__(self):
        self.conn = mydb.connect(
            user="root",
            password="your_pass",
            database = "your_database"
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id  INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(50) NOT NULL,
                customer_email VARCHAR(50) NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id  INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(50) FOREIGN KEY,
                product_name VARCHAR(50)
                quantity INT NOT NULL,
                order_date DATE
            )
        """)
        self.conn.commit()

    # add new order
    def add_order(self, customer_name, product_name, quantity, order_date):
        self.cursor.execute("""
            INSERT INTO orders (customer_name, product_name, quantity, order_date)
            VALUES (%s, %s, %s, %s)
        """, (customer_name, product_name, quantity, order_date))
        self.conn.commit()
    
    # list all orders 
    def  list_orders(self):
        self.cursor.execute("SELECT * FROM orders")
        return self.cursor.fetchall()
    
    # display all order
    def display_orders(self, start_date, end_date):
        self.cursor.execute("SELECT * FROM orders WHERE order_date BETWEEN %s AND %s", (start_date, end_date))
        return self.cursor.fetchall()
    
    # update orders details 
    def  update_order(self, order_id, product_name, quantity):
        self.cursor.execute("""
            UPDATE orders
            SET product_name = %s, quantity = %s
            WHERE order_id = %s
            """, (product_name, quantity, order_id))
    
    # delete order
    def delete_products(self, order_id):
        self.cursor.execute("""
            DELETE FROM orders
            WHERE order_id = %s
        """, (order_id,))
        self.conn.commit()
        
    
def main():
    ems = Customerordersystem()
    ems.create_table()
    while True:
        print("Customer Order System ")
        print("1. Add New Order")
        print("2. List All Order")
        print("3. Dislpay Order")
        print("4. Update Order")
        print("5. Delete Order")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            
            ems.add_product(customer_name, product_name, quantity, order_date)

    

        elif choice == 6:
            print("Exit the Program...")
            break

        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()

