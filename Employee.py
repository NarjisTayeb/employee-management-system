# ________________________________________
# Employee Management System (Boss / Manager / Employee)
# Console-Based Version | Cleaned for GitHub

# ====== Sample Data ======

# Create tables for Boss, Managers, and Employees
bosses = [
    {
        "name": "Alice Johnson",
        "id": 1,
        "designation": "CEO",
        "address": "123 Corporate Blvd, Suite 100, Business City, BC 12345",
        "salary": 150000,
        "email": "alice.johnson@company.com",
        "username": "alicej",
        "password": "SecurePass123"
    }
]

managers = [
    {
        "name": "Carol White",
        "id": 2,
        "designation": "Sales Manager",
        "address": "789 Sales St, Commerce Town, CT 23456",
        "salary": 90000,
        "email": "carol.white@company.com",
        "username": "carolw",
        "password": "SecurePass789"
    },
    {
        "name": "David Brown",
        "id": 3,
        "designation": "HR Manager",
        "address": "321 HR Rd, People City, PC 34567",
        "salary": 85000,
        "email": "david.brown@company.com",
        "username": "davidb",
        "password": "SecurePass101"
    }
]

employees = [
    {
        "name": "Emily Davis",
        "id": 4,
        "designation": "Sales Executive",
        "address": "555 Sales Blvd, Commerce Town, CT 23456",
        "salary": 50000,
        "email": "emily.davis@company.com",
        "username": "emilyd",
        "password": "SecurePass202"
    },
    {
        "name": "Frank Harris",
        "id": 5,
        "designation": "Sales Associate",
        "address": "666 Sales Ln, Commerce Town, CT 23456",
        "salary": 45000,
        "email": "frank.harris@company.com",
        "username": "frankh",
        "password": "SecurePass203"
    },
    {
        "name": "Grace Lee",
        "id": 6,
        "designation": "HR Assistant",
        "address": "777 HR Blvd, People City, PC 34567",
        "salary": 40000,
        "email": "grace.lee@company.com",
        "username": "gracelee",
        "password": "SecurePass204"
    },
    {
        "name": "Henry King",
        "id": 7,
        "designation": "HR Intern",
        "address": "888 Intern Rd, People City, PC 34567",
        "salary": 30000,
        "email": "henry.king@company.com",
        "username": "henryk",
        "password": "SecurePass205"
    },
    {
        "name": "Isla Martin",
        "id": 8,
        "designation": "Sales Trainee",
        "address": "999 Trainee Blvd, Commerce Town, CT 23456",
        "salary": 35000,
        "email": "isla.martin@company.com",
        "username": "islam",
        "password": "SecurePass206"
    },
    {
        "name": "Jack Wilson",
        "id": 9,
        "designation": "Sales Representative",
        "address": "1010 Rep Rd, Commerce Town, CT 23456",
        "salary": 48000,
        "email": "jack.wilson@company.com",
        "username": "jackw",
        "password": "SecurePass207"
    }
]


# ====== Utility Functions ======

def print_sample_data():
    """Display all sample data."""
    print("Bosses:")
    for boss in bosses:
        print(boss)

    print("\nManagers:")
    for manager in managers:
        print(manager)

    print("\nEmployees:")
    for employee in employees:
        print(employee)


# ====== Login Function ======

def login():
    """Login function that authenticates a user."""
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Boss Login
        for boss in bosses:
            if boss['username'] == username and boss['password'] == password:
                print(f"Welcome {boss['name']} (Boss)")
                return "boss", boss

        # Manager Login
        for manager in managers:
            if manager['username'] == username and manager['password'] == password:
                print(f"Welcome {manager['name']} (Manager)")
                return "manager", manager

        # Employee Login
        for employee in employees:
            if employee['username'] == username and employee['password'] == password:
                print(f"Welcome {employee['name']} (Employee)")
                return "employee", employee

        attempts += 1
        print(f"Login failed. You have {3 - attempts} attempts left.")

    print("Too many failed attempts. System terminating.")
    exit()


# ====== Boss Functions ======

def add_employee():
    """Add new employee."""
    print("\n--- Add Employee ---")
    name = input("Enter name: ")
    emp_id = int(input("Enter ID: "))
    designation = input("Enter designation: ")
    address = input("Enter address: ")
    salary = float(input("Enter salary: "))
    email = input("Enter email: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    new_employee = {
        "name": name,
        "id": emp_id,
        "designation": designation,
        "address": address,
        "salary": salary,
        "email": email,
        "username": username,
        "password": password
    }

    employees.append(new_employee)
    print(f"Employee {name} added successfully.")


def edit_boss_profile(boss):
    """Allow boss to edit their own profile."""
    print("\n--- Edit Boss Profile ---")
    boss['name'] = input(f"Enter new name (current: {boss['name']}): ") or boss['name']
    boss['address'] = input(f"Enter new address (current: {boss['address']}): ") or boss['address']
    new_salary = input(f"Enter new salary (current: {boss['salary']}): ")
    boss['salary'] = float(new_salary) if new_salary else boss['salary']
    print("Profile updated successfully.")


def delete_user(user_type):
    """Delete employee or manager by name, ID, or email."""
    identifier = input(f"Enter {user_type} name, ID, or email to delete: ")
    if user_type == "Employee":
        for emp in employees:
            if str(emp['id']) == identifier or emp['name'] == identifier or emp['email'] == identifier:
                employees.remove(emp)
                print(f"Employee {emp['name']} deleted successfully.")
                return
    elif user_type == "Manager":
        for mgr in managers:
            if str(mgr['id']) == identifier or mgr['name'] == identifier or mgr['email'] == identifier:
                managers.remove(mgr)
                print(f"Manager {mgr['name']} deleted successfully.")
                return
    print(f"No {user_type} found with that identifier.")


def boss_menu(boss):
    """Boss menu options."""
    while True:
        print("\n--- Boss Menu ---")
        print("1. Add Employee")
        print("2. Edit Profile")
        print("3. Delete Employee")
        print("4. Delete Manager")
        print("5. Log Out")
        choice = input("Select an option: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            edit_boss_profile(boss)
        elif choice == '3':
            delete_user("Employee")
        elif choice == '4':
            delete_user("Manager")
        elif choice == '5':
            print("Logging out...")
            return
        else:
            print("Invalid choice, please try again.")


# ====== Manager Functions ======

def reset_password(manager):
    """Allow manager to reset their password."""
    print("\n--- Reset Password ---")
    new_password = input("Enter new password: ")
    manager['password'] = new_password
    print("Password reset successfully.")


def edit_manager_profile(manager):
    """Allow manager to edit their own profile."""
    print("\n--- Edit Manager Profile ---")
    manager['name'] = input(f"Enter new name (current: {manager['name']}): ") or manager['name']
    manager['address'] = input(f"Enter new address (current: {manager['address']}): ") or manager['address']
    new_salary = input(f"Enter new salary (current: {manager['salary']}): ")
    manager['salary'] = float(new_salary) if new_salary else manager['salary']
    print("Profile updated successfully.")


def manager_menu(manager):
    """Manager menu options."""
    while True:
        print("\n--- Manager Menu ---")
        print("1. Reset Password")
        print("2. Add Employee")
        print("3. Edit Profile")
        print("4. Log Out")
        choice = input("Select an option: ")

        if choice == '1':
            reset_password(manager)
        elif choice == '2':
            add_employee()
        elif choice == '3':
            edit_manager_profile(manager)
        elif choice == '4':
            print("Logging out...")
            return
        else:
            print("Invalid choice, please try again.")


# ====== Employee Functions ======

def employee_menu(employee):
    """Placeholder employee menu."""
    print(f"\nWelcome {employee['name']}! Employees have limited access.")
    input("Press Enter to log out.")


# ====== Main Program ======

if __name__ == "__main__":
    print("Welcome to the Employee Management System!\n")
    user_role, user_info = login()

    if user_role == "boss":
        boss_menu(user_info)
    elif user_role == "manager":
        manager_menu(user_info)
    elif user_role == "employee":
        employee_menu(user_info)
