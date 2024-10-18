# Employee Management System
import mysql.connector as mydb


class EmployeeManagementSystem:
    def __init__(self):
        self.conn = mydb.connect(
            user="root",
            password="your_password",
            database = "database_name"
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INTEGER NOT NULL,
                department VARCHAR(50) NOT NULL,
                salary INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def add_employee(self, name, age, department, salary):
        self.cursor.execute("""
            INSERT INTO employees (name, age, department, salary)
            VALUES (%s, %s, %s, %s)
        """, (name, age, department, salary))
        self.conn.commit()

    def update_employee(self, id, name, department, salary):
        self.cursor.execute("""
            UPDATE employees
            SET name = %s, department = %s, salary = %s
            WHERE id = %s
        """, (name, department, salary, id))
        self.conn.commit()

    def delete_employee(self, id):
        self.cursor.execute("""
            DELETE FROM employees
            WHERE id = %s
        """, (id,))
        self.conn.commit()

    def view_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}, Salary: {row[4]}")

def main():
    ems = EmployeeManagementSystem()
    ems.create_table()
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter Employee name: ")
            age = int(input("Enter Employee age: "))
            department = input("Enter Employee department: ")
            salary = int(input("Enter Employee salary: "))
            ems.add_employee(name, age, department, salary)

        elif choice == 2:
            ems.view_employees()

        elif choice == 3:
            id = int(input("Enter Employee ID: "))
            name = input("Enter Employee name: ")
            department = input("Enter Employee Department: ")
            salary = int(input("Enter Employee Salary: "))
            ems.update_employee(id, name, department, salary)

        elif choice == 4:
            id = int(input("Enter Employee ID: "))
            ems.delete_employee(id)

        elif choice == 5:
            print("Exit the Program...")
            break

        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()