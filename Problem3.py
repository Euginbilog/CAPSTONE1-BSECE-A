# Employee class to store information about a single employee
class Employee:
    def __init__(self, employee_id, name, organization):
        """Initialize an Employee with ID, name, organization, and an empty attendance record."""
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = []

    def mark_attendance(self, is_present):
        """Mark attendance for the day (True for present, False for absent)."""
        self.attendance.append(is_present)
        status = "Present" if is_present else "Absent"
        print(f"\nAttendance marked as '{status}' for {self.name}.\n")

    def calculate_attendance_percentage(self):
        """Calculate and return the percentage of days present."""
        if not self.attendance:
            return 0
        total_days = len(self.attendance)
        days_present = sum(self.attendance)
        return (days_present / total_days) * 100

    def __str__(self):
        """Return a string representation of the employee's details and attendance percentage."""
        percentage = self.calculate_attendance_percentage()
        return (f"ID: {self.employee_id}, Name: {self.name}, Organization: {self.organization}, "
                f"Total Days: {len(self.attendance)}, Present: {sum(self.attendance)}, "
                f"Attendance Percentage: {percentage:.2f}%")


# AttendanceTracker class to manage multiple Employee objects
class AttendanceTracker:
    def __init__(self):
        """Initialize an empty list to store employee records."""
        self.employees = []

    def add_employee(self, employee_id, name, organization):
        """Add a new employee to the system."""
        new_employee = Employee(employee_id, name, organization)
        self.employees.append(new_employee)
        print(f"\nEmployee '{name}' added successfully!\n")

    def mark_attendance(self, employee_id, is_present):
        """Mark attendance for an employee by their employee ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.mark_attendance(is_present)
                return
        print(f"\nNo employee found with ID '{employee_id}'.\n")

    def display_employees(self):
        """Display all employees and their attendance records."""
        if not self.employees:
            print("\nNo employee records available.\n")
        else:
            print("\nEmployee Attendance Records:")
            for idx, employee in enumerate(self.employees, start=1):
                print(f"{idx}. {employee}")
            print("\n")

    def display_attendance_percentage(self):
        """Display the percentage of attendance for each employee."""
        if not self.employees:
            print("\nNo employee records available.\n")
        else:
            print("\nEmployee Attendance Percentage:")
            for employee in self.employees:
                percentage = employee.calculate_
