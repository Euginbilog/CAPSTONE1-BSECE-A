# Student class to store information about a single student
class Student:
    def __init__(self, student_id, name, course, grade1, grade2, grade3, grade4):
        """Initialize a new Student instance with ID, name, course, and grades for four subjects."""
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = [grade1, grade2, grade3, grade4]

    def update_grades(self, new_grades):
        """Update the student's grades."""
        if len(new_grades) == 4 and all(0 <= grade <= 100 for grade in new_grades):
            self.grades = new_grades
            print(f"\nGrades for {self.name} updated successfully!\n")
        else:
            print("\nInvalid grades. Please enter four numbers between 0 and 100.\n")

    def calculate_average(self):
        """Calculate and return the student's average grade."""
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """Return a string representation of the student details."""
        grades_str = ', '.join(f'{grade:.2f}' for grade in self.grades)
        return (f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, "
                f"Grades: [{grades_str}], Average: {self.calculate_average():.2f}")


# GradeManagementSystem class to manage multiple Student objects
class GradeManagementSystem:
    def __init__(self):
        """Initialize an empty list to store student records."""
        self.students = []

    def add_student(self, student_id, name, course, grade1, grade2, grade3, grade4):
        """Add a new student to the system."""
        new_student = Student(student_id, name, course, grade1, grade2, grade3, grade4)
        self.students.append(new_student)
        print(f"\nStudent '{name}' added successfully!\n")

    def update_student_grade(self, student_id, new_grades):
        """Update a student's grades by their student ID."""
        for student in self.students:
            if student.student_id == student_id:
                student.update_grades(new_grades)
                return
        print(f"\nNo student found with ID '{student_id}'.\n")

    def display_students(self):
        """Display all students and their grades."""
        if not self.students:
            print("\nNo student records available.\n")
        else:
            print("\nStudent Records:")
            for idx, student in enumerate(self.students, start=1):
                print(f"{idx}. {student}")
            print("\n")

    def calculate_class_average(self):
        """Calculate and display the class average grade."""
        if not self.students:
            print("\nNo student records available to calculate the class average.\n")
        else:
            total_average = sum(student.calculate_average() for student in self.students) / len(self.students)
            print(f"\nThe class average grade is: {total_average:.2f}\n")


def main():
    """Main function to run the Student Grade Management System."""
    system = GradeManagementSystem()
    
    while True:
        print("Student Grade Management System")
        print("1. Add a new student")
        print("2. Update a student's grades")
        print("3. Display all student records")
        print("4. Calculate the class average grade")
        print("5. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.\n")
            continue
        
        if choice == 1:
            student_id = input("\nEnter student ID: ")
            name = input("Enter student name: ")
            course = input("Enter course (e.g., BSECE, BSCS): ")
            
            try:
                grades = [
                    float(input(f"Enter grade 1 (0-100): ")),
                    float(input(f"Enter grade 2 (0-100): ")),
                    float(input(f"Enter grade 3 (0-100): ")),
                    float(input(f"Enter grade 4 (0-100): "))
                ]
                
                if all(0 <= grade <= 100 for grade in grades):
                    system.add_student(student_id, name, course, *grades)
                else:
                    print("\nAll grades must be between 0 and 100.\n")
            except ValueError:
                print("\nInvalid input. Grades must be numbers between 0 and 100.\n")
        
        elif choice == 2:
            student_id = input("\nEnter the student ID to update grades: ")
            try:
                new_grades = [
                    float(input(f"Enter new grade 1 (0-100): ")),
                    float(input(f"Enter new grade 2 (0-100): ")),
                    float(input(f"Enter new grade 3 (0-100): ")),
                    float(input(f"Enter new grade 4 (0-100): "))
                ]
                
                system.update_student_grade(student_id, new_grades)
            except ValueError:
                print("\nInvalid input. Grades must be numbers between 0 and 100.\n")
        
        elif choice == 3:
            system.display_students()
        
        elif choice == 4:
            system.calculate_class_average()
        
        elif choice == 5:
            print("\nExiting the Student Grade Management System. Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
