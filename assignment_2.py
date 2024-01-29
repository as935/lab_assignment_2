# Name: Akshay Sharma Roll no: 2110110083
class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


def sort_employees(employees, key):
    # Sort employees based on the chosen key
    if key == 1:  # Sort by Age
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:  # Sort by Name
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:  # Sort by Salary
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting key")


def main():
    # Employee data
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    print("Employee Table:")
    for emp in employees:
        print(emp)

    # Get user input for sorting parameter
    print("\nSorting Parameters: 1. Age, 2. Name, 3. Salary")#changed line
    sorting_key = int(input("\nChoose sorting parameter (1. Age, 2. Name, 3. Salary): "))

    try:
        # Sort and print the sorted employee data
        sorted_employees = sort_employees(employees, sorting_key)
        # print(sorted_employees)
        print("\nSorted Employee Data:")
        for emp in sorted_employees:
            print(emp)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
