import tkinter as tk
from tkinter import messagebox, ttk
from part1 import Student, Course, Instructor
import json

class SchoolApp:
    def __init__(self, root):
        """
        Initializes the SchoolApp.

        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("900x600")

        self.students = []
        self.instructors = []
        self.courses = []

        # ========================== Student Form ==========================
        student_frame = tk.Frame(root)
        student_frame.grid(row=0, column=0, padx=20, pady=20)

        tk.Label(student_frame, text="Add Student").grid(row=0, column=0, columnspan=2)
        tk.Label(student_frame, text="Name:").grid(row=1, column=0)
        self.student_name_entry = tk.Entry(student_frame)
        self.student_name_entry.grid(row=1, column=1)

        tk.Label(student_frame, text="Age:").grid(row=2, column=0)
        self.student_age_entry = tk.Entry(student_frame)
        self.student_age_entry.grid(row=2, column=1)

        tk.Label(student_frame, text="Email:").grid(row=3, column=0)
        self.student_email_entry = tk.Entry(student_frame)
        self.student_email_entry.grid(row=3, column=1)

        tk.Label(student_frame, text="Student ID:").grid(row=4, column=0)
        self.student_id_entry = tk.Entry(student_frame)
        self.student_id_entry.grid(row=4, column=1)

        self.add_student_button = tk.Button(student_frame, text="Add Student", command=self.add_student)
        self.add_student_button.grid(row=5, column=0, columnspan=2)

        # ========================== Instructor Form ==========================
        instructor_frame = tk.Frame(root)
        instructor_frame.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(instructor_frame, text="Add Instructor").grid(row=0, column=0, columnspan=2)
        tk.Label(instructor_frame, text="Name:").grid(row=1, column=0)
        self.instructor_name_entry = tk.Entry(instructor_frame)
        self.instructor_name_entry.grid(row=1, column=1)

        tk.Label(instructor_frame, text="Age:").grid(row=2, column=0)
        self.instructor_age_entry = tk.Entry(instructor_frame)
        self.instructor_age_entry.grid(row=2, column=1)

        tk.Label(instructor_frame, text="Email:").grid(row=3, column=0)
        self.instructor_email_entry = tk.Entry(instructor_frame)
        self.instructor_email_entry.grid(row=3, column=1)

        tk.Label(instructor_frame, text="Instructor ID:").grid(row=4, column=0)
        self.instructor_id_entry = tk.Entry(instructor_frame)
        self.instructor_id_entry.grid(row=4, column=1)

        self.add_instructor_button = tk.Button(instructor_frame, text="Add Instructor", command=self.add_instructor)
        self.add_instructor_button.grid(row=5, column=0, columnspan=2)

        # ========================== Course Form ==========================
        course_frame = tk.Frame(root)
        course_frame.grid(row=0, column=2, padx=20, pady=20)

        tk.Label(course_frame, text="Add Course").grid(row=0, column=0, columnspan=2)
        tk.Label(course_frame, text="Course Name:").grid(row=1, column=0)
        self.course_name_entry = tk.Entry(course_frame)
        self.course_name_entry.grid(row=1, column=1)

        tk.Label(course_frame, text="Course ID:").grid(row=2, column=0)
        self.course_id_entry = tk.Entry(course_frame)
        self.course_id_entry.grid(row=2, column=1)

        self.add_course_button = tk.Button(course_frame, text="Add Course", command=self.add_course)
        self.add_course_button.grid(row=3, column=0, columnspan=2)

        # ========================== Registration Form ==========================
        registration_frame = tk.Frame(root)
        registration_frame.grid(row=0, column=3, padx=20, pady=20)

        tk.Label(registration_frame, text="Student Registration for Courses").grid(row=0, column=0, columnspan=4)
        tk.Label(registration_frame, text="Select Student:").grid(row=1, column=0)
        self.selected_student = tk.StringVar()
        self.student_dropdown = ttk.Combobox(registration_frame, textvariable=self.selected_student, state="readonly")
        self.student_dropdown.grid(row=1, column=1)

        tk.Label(registration_frame, text="Select Course:").grid(row=2, column=0)
        self.selected_course = tk.StringVar()
        self.course_dropdown = ttk.Combobox(registration_frame, textvariable=self.selected_course, state="readonly")
        self.course_dropdown.grid(row=2, column=1)

        self.register_button = tk.Button(registration_frame, text="Register", command=self.register_student_to_course)
        self.register_button.grid(row=3, column=0, columnspan=2)

        # ========================== Instructor Assignment Form ==========================
        instructor_assignment_frame = tk.Frame(root)
        instructor_assignment_frame.grid(row=0, column=4, padx=20, pady=20)

        tk.Label(instructor_assignment_frame, text="Instructor Assignment to Courses").grid(row=0, column=0, columnspan=4)
        tk.Label(instructor_assignment_frame, text="Select Instructor:").grid(row=1, column=0)
        self.selected_instructor = tk.StringVar()
        self.instructor_dropdown = ttk.Combobox(instructor_assignment_frame, textvariable=self.selected_instructor, state="readonly")
        self.instructor_dropdown.grid(row=1, column=1)

        tk.Label(instructor_assignment_frame, text="Select Course:").grid(row=2, column=0)
        self.selected_assignment_course = tk.StringVar()
        self.assignment_course_dropdown = ttk.Combobox(instructor_assignment_frame, textvariable=self.selected_assignment_course, state="readonly")
        self.assignment_course_dropdown.grid(row=2, column=1)

        self.assign_instructor_button = tk.Button(instructor_assignment_frame, text="Assign Instructor", command=self.assign_instructor_to_course)
        self.assign_instructor_button.grid(row=3, column=0, columnspan=2)

        # Update dropdowns after initialization
        self.update_student_dropdown()
        self.update_instructor_dropdown()
        self.update_course_dropdown()
        
        # ========================== Treeview to Display Records ==========================
        display_frame = tk.Frame(root)
        display_frame.grid(row=2, column=0, columnspan=5, padx=20, pady=20)
        
        # Create a Treeview widget
        self.tree = ttk.Treeview(display_frame, columns=("ID", "Name", "Age/Info", "Email"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age/Info", text="Age/Info")
        self.tree.heading("Email", text="Email")
        self.tree.column("ID", width=100)
        self.tree.column("Name", width=200)
        self.tree.column("Age/Info", width=150)
        self.tree.column("Email", width=250)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Buttons to switch between Students, Instructors, and Courses
        button_frame = tk.Frame(root)
        button_frame.grid(row=3, column=0, columnspan=5, padx=20, pady=20)

        self.show_students_button = tk.Button(button_frame, text="Show Students", command=self.show_students)
        self.show_students_button.grid(row=0, column=0, padx=10)

        self.show_instructors_button = tk.Button(button_frame, text="Show Instructors", command=self.show_instructors)
        self.show_instructors_button.grid(row=0, column=1, padx=10)

        self.show_courses_button = tk.Button(button_frame, text="Show Courses", command=self.show_courses)
        self.show_courses_button.grid(row=0, column=2, padx=10)
        
        self.show_students()

        # ========================== Search Functionality ==========================
        search_frame = tk.Frame(root)
        search_frame.grid(row=1, column=0, columnspan=5, padx=20, pady=10)

        tk.Label(search_frame, text="Search:").grid(row=0, column=0)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1)

        self.search_type = tk.StringVar()
        self.search_type.set("Student")  # Default search type

        search_type_dropdown = ttk.Combobox(search_frame, textvariable=self.search_type, values=["Student", "Instructor", "Course"], state="readonly")
        search_type_dropdown.grid(row=0, column=2)

        search_button = tk.Button(search_frame, text="Search", command=self.search_records)
        search_button.grid(row=0, column=3)
        
         # Add Edit and Delete buttons below the Treeview
        action_frame = tk.Frame(root)
        action_frame.grid(row=4, column=0, columnspan=5, padx=20, pady=10)

        self.edit_button = tk.Button(action_frame, text="Edit", command=self.edit_record)
        self.edit_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(action_frame, text="Delete", command=self.delete_record)
        self.delete_button.grid(row=0, column=1, padx=10)

        # Keep track of the currently selected student, instructor, or course
        self.selected_item = None
    
    def add_student(self):
        """
        Adds a student to the system.

        Validates the input fields, creates a Student object, and appends it to the students list. Updates the student dropdown.

        Returns:
            None
        """
        name = self.student_name_entry.get()
        age = self.student_age_entry.get()
        email = self.student_email_entry.get()
        student_id = self.student_id_entry.get()

        if name and age and email and student_id:
            try:
                student = Student(name, int(age), email, student_id)
                self.students.append(student)
                messagebox.showinfo("Student Added", f"Added student: {student.name}")
                self.update_student_dropdown()  # Update the student dropdown
                print(f"Added student {name}")
                self.show_students()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in all fields")
            

    def add_instructor(self):
        """
        Adds an instructor to the system.

        Validates the input fields, creates an Instructor object, and appends it to the instructors list. Updates the instructor dropdown.

        Returns:
            None
        """
        name = self.instructor_name_entry.get()
        age = self.instructor_age_entry.get()
        email = self.instructor_email_entry.get()
        instructor_id = self.instructor_id_entry.get()

        if name and age and email and instructor_id:
            try:
                instructor = Instructor(name, int(age), email, instructor_id)
                self.instructors.append(instructor)
                messagebox.showinfo("Instructor Added", f"Added instructor: {instructor.name}")
                self.update_instructor_dropdown()  # Update the instructor dropdown
                print(f"Added instructor {name}")
                self.show_instructors()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def add_course(self):
        """
        Adds a course to the system.

        Validates the input fields, creates a Course object, and appends it to the courses list. Updates the course dropdown.

        Returns:
            None
        """
        course_name = self.course_name_entry.get()
        course_id = self.course_id_entry.get()

        if course_name and course_id:
            course = Course(course_id, course_name)
            self.courses.append(course)
            messagebox.showinfo("Course Added", f"Added course: {course.course_name}")
            self.update_course_dropdown()  # Update the course dropdown
            print(f"Added course {course_name}")
            self.show_courses()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def update_student_dropdown(self):
        """
        Updates the student dropdown with the current list of students.

        Returns:
            None
        """
        student_names = [student.name for student in self.students]
        self.student_dropdown['values'] = student_names

    def update_instructor_dropdown(self):
        """
        Updates the instructor dropdown with the current list of instructors.

        Returns:
            None
        """
        instructor_names = [instructor.name for instructor in self.instructors]
        self.instructor_dropdown['values'] = instructor_names

    def update_course_dropdown(self):
        """
        Updates the course dropdown with the current list of courses.

        Returns:
            None
        """
        course_names = [course.course_name for course in self.courses]
        self.course_dropdown['values'] = course_names  # For student registration
        self.assignment_course_dropdown['values'] = course_names  # For instructor assignment

    def register_student_to_course(self):
        """
        Registers a selected student to a selected course.

        Checks if the selected student and course are valid, adds the registration, and updates the student dropdown.

        Returns:
            None
        """
        selected_student_name = self.selected_student.get()
        selected_course_name = self.selected_course.get()

        if selected_student_name and selected_course_name:
            student = next((student for student in self.students if student.name == selected_student_name), None)
            course = next((course for course in self.courses if course.course_name == selected_course_name), None)

            if student and course:
                student.register_course(course)
                messagebox.showinfo("Success", f"Registered {student.name} to {course.course_name}")
            else:
                messagebox.showerror("Error", "Student or Course not found")
        else:
            messagebox.showerror("Error", "Please select a student and a course")

    def assign_instructor_to_course(self):
        """
        Assigns a selected instructor to a selected course.

        Checks if the selected instructor and course are valid, assigns the instructor to the course, and updates the instructor dropdown.

        Returns:
            None
        """
        selected_instructor_name = self.selected_instructor.get()
        selected_course_name = self.selected_assignment_course.get()

        if selected_instructor_name and selected_course_name:
            instructor = next((instructor for instructor in self.instructors if instructor.name == selected_instructor_name), None)
            course = next((course for course in self.courses if course.course_name == selected_course_name), None)

            if instructor and course:
                instructor.assign_course(course)
                messagebox.showinfo("Success", f"Assigned {instructor.name} to {course.course_name}")
            else:
                messagebox.showerror("Error", "Instructor or Course not found")
        else:
            messagebox.showerror("Error", "Please select an instructor and a course")
            
# Method to show students in the Treeview
    def show_students(self):
        """
        Displays the list of students in the Treeview.

        Returns:
            None
        """
        self.clear_treeview()

        # Update column headings
        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Student Name")
        self.tree.heading("Age/Info", text="Age")
        self.tree.heading("Email", text="Email")

        # Add student records to the tree
        for student in self.students:
            print(f"Adding student {student.name} to the treeview")  # Debugging print
            self.tree.insert("", "end", values=(student.student_id, student.name, student.age, student._email))

    # Method to show instructors in the Treeview
    def show_instructors(self):
        """
        Displays the list of instructors in the Treeview.

        Returns:
            None
        """
        print(f"Showing {len(self.instructors)} instructors")  # Debugging print
        self.clear_treeview()

        # Update column headings
        self.tree.heading("ID", text="Instructor ID")
        self.tree.heading("Name", text="Instructor Name")
        self.tree.heading("Age/Info", text="Age")
        self.tree.heading("Email", text="Email")

        # Add instructor records to the tree
        for instructor in self.instructors:
            print(f"Adding instructor {instructor.name} to the treeview")  # Debugging print
            self.tree.insert("", "end", values=(instructor.instructor_id, instructor.name, instructor.age, instructor._email))

    # Method to show courses in the Treeview
    def show_courses(self):
        """
        Displays the list of courses in the Treeview.

        Returns:
            None
        """
        print(f"Showing {len(self.courses)} courses")  # Debugging print
        self.clear_treeview()

        # Update column headings
        self.tree.heading("ID", text="Course ID")
        self.tree.heading("Name", text="Course Name")
        self.tree.heading("Age/Info", text="Number of Students")
        self.tree.heading("Email", text="Instructor Name")

        # Add course records to the tree
        for course in self.courses:
            print(f"Adding course {course.course_name} to the treeview")  # Debugging print
            num_students = len(course.enrolled_students)  # Number of students registered in the course
            instructor_name = course.instructor.name if course.instructor else "Not Assigned"
            self.tree.insert("", "end", values=(course.course_id, course.course_name, num_students, instructor_name))
            
    # Clear the Treeview before updating it with new data
    def clear_treeview(self):
        self.tree.delete(*self.tree.get_children())
        
    # Method to search records based on search query and type
    def search_records(self):
        """
        Searches for records based on the search term and type.

        Updates the Treeview to display only matching records.

        Returns:
            None
        """
        search_query = self.search_entry.get().lower()
        search_type = self.search_type.get()

        if search_type == "Student":
            filtered_students = [student for student in self.students if search_query in student.name.lower() or search_query in student.student_id.lower()]
            self.show_filtered_students(filtered_students)
        
        elif search_type == "Instructor":
            filtered_instructors = [instructor for instructor in self.instructors if search_query in instructor.name.lower() or search_query in instructor.instructor_id.lower()]
            self.show_filtered_instructors(filtered_instructors)

        elif search_type == "Course":
            filtered_courses = [course for course in self.courses if search_query in course.course_name.lower() or search_query in course.course_id.lower()]
            self.show_filtered_courses(filtered_courses)

    # Method to show filtered students
    def show_filtered_students(self, students):
        self.clear_treeview()

        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Student Name")
        self.tree.heading("Age/Info", text="Age")
        self.tree.heading("Email", text="Email")

        for student in students:
            self.tree.insert("", "end", values=(student.student_id, student.name, student.age, student._email))

    # Method to show filtered instructors
    def show_filtered_instructors(self, instructors):
        self.clear_treeview()

        self.tree.heading("ID", text="Instructor ID")
        self.tree.heading("Name", text="Instructor Name")
        self.tree.heading("Age/Info", text="Age")
        self.tree.heading("Email", text="Email")

        for instructor in instructors:
            self.tree.insert("", "end", values=(instructor.instructor_id, instructor.name, instructor.age, instructor._email))

    # Method to show filtered courses
    def show_filtered_courses(self, courses):
        self.clear_treeview()

        self.tree.heading("ID", text="Course ID")
        self.tree.heading("Name", text="Course Name")
        self.tree.heading("Age/Info", text="Number of Students")
        self.tree.heading("Email", text="Instructor Name")

        for course in courses:
            num_students = len(course.enrolled_students)
            instructor_name = course.instructor.name if course.instructor else "Not Assigned"
            self.tree.insert("", "end", values=(course.course_id, course.course_name, num_students, instructor_name))

    def clear_treeview(self):
        self.tree.delete(*self.tree.get_children())
        
    # Retrieve the selected record from the Treeview
    def get_selected_item(self):
        selected = self.tree.focus()  # Get the selected item
        if selected:
            values = self.tree.item(selected, 'values')
            print("Selected item:", values)  # Debugging aid
            return values
        else:
            print("No item selected")  # Debugging aid
        return None

    # Method to edit a selected record
    def edit_record(self):
        """
        Edits the selected record in the Treeview.

        Opens an appropriate editing interface based on the selected record type (Student, Instructor, Course).

        Returns:
            None
        """
        self.selected_item = self.get_selected_item()
        if self.selected_item:
            # Assuming we are editing a student for this example:
            if self.tree.heading("ID", text="Student ID"):
                student_id = self.selected_item[0]
                student = next((student for student in self.students if student.student_id == student_id), None)
                if student:
                    # Populate the entry fields with the student's data
                    self.student_name_entry.delete(0, tk.END)
                    self.student_name_entry.insert(tk.END, student.name)
                    self.student_age_entry.delete(0, tk.END)
                    self.student_age_entry.insert(tk.END, student.age)
                    self.student_email_entry.delete(0, tk.END)
                    self.student_email_entry.insert(tk.END, student._email)
                    self.student_id_entry.delete(0, tk.END)
                    self.student_id_entry.insert(tk.END, student.student_id)

                    # Update Add button text to "Save"
                    self.add_student_button.config(text="Save Student", command=self.save_edited_student)

                else:
                    messagebox.showwarning("Error", "No matching student found!")  # Debugging aid
        else:
            messagebox.showwarning("Error", "No student selected!")  # User feedback

    def save_edited_student(self):
        if self.selected_item:
            student_id = self.selected_item[0]
            student = next((student for student in self.students if student.student_id == student_id), None)
            if student:
                # Update the student's data with the new values from the entry fields
                student.name = self.student_name_entry.get()
                student.age = int(self.student_age_entry.get())
                student._email = self.student_email_entry.get()
                student.student_id = self.student_id_entry.get()

                messagebox.showinfo("Student Updated", f"Updated student: {student.name}")
                self.show_students()  # Refresh the student list in the Treeview

                # Reset the Add button to its original state
                self.add_student_button.config(text="Add Student", command=self.add_student)
                self.clear_entry_fields()
            else:
                messagebox.showwarning("Error", "No matching student found for editing!")  # Debugging aid
        else:
            messagebox.showwarning("Error", "No student selected for editing!")  # Debugging aid

    # Method to delete a selected record
    def delete_record(self):
        """
        Deletes the selected record in the Treeview.

        Removes the selected student, instructor, or course from the lists and updates the Treeview.

        Returns:
            None
        """
        self.selected_item = self.get_selected_item()
        if self.selected_item:
            if self.tree.heading("ID", text="Student ID"):
                student_id = self.selected_item[0]
                self.students = [student for student in self.students if student.student_id != student_id]
                messagebox.showinfo("Student Deleted", f"Deleted student ID: {student_id}")
                self.show_students()  # Refresh the Treeview to remove the deleted student
            else:
                messagebox.showwarning("Error", "No student ID selected!")  # Debugging aid
        else:
            messagebox.showwarning("Error", "No student selected for deletion!")  # User feedback

    # Helper method to clear entry fields
    def clear_entry_fields(self):
        self.student_name_entry.delete(0, tk.END)
        self.student_age_entry.delete(0, tk.END)
        self.student_email_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)

# Root window setup
root = tk.Tk()
app = SchoolApp(root)
root.mainloop()
