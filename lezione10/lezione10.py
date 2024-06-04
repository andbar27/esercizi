# Exercise 1: Creating an Abstract Class with Abstract Methods

from abc import ABC, abstractmethod

class AbcProva(ABC):

    @abstractmethod
    def prova(self):
        pass


# Create an abstract class Shape with an abstract method area and another abstract method perimeter. Then, create two subclasses Circle 
# and Rectangle that implement the area and perimeter methods.
# Exercise 2: Implementing Static Methods

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


import math

class Circle(Shape):

    def __init__(self, radius: float) -> None:
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return math.pi * self.radius * 2
    

class Rettangle(Shape):

    def __init__(self, width, heigh) -> None:
        super().__init__()
        self.width = width
        self.heigh = heigh

    def area(self) -> float:
        return self.width * self.heigh
    
    def perimeter(self):
        return (self.width + self.heigh) * 2
    

# Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
# and another static method multiply that takes two numbers and returns their product.
# Exercise 3: Library Management System 

class MathOperations:

    @staticmethod
    def add(n1, n2):
        return n1 + n2
    
    @staticmethod
    def multiply(n1, n2):
        return n1 * n2


# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

#     __str__ method to return a string representation of the book.

#     @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
#         It means that you must use the class reference cls to create a new object of the Book class using a string.

class Book:

    def __init__(self, title: str, author: str, isbn: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    @classmethod
    def from_string(cls, book_str: str) -> Book:
        parameters = [param.strip() for param in book_str.split(",")]
        if len(parameters) != 2:
            print("Wrong string format")
            return
        return Book(parameters[0], parameters[1], int(parameters[2]))

    def __str__(self) -> str:
        return f"title = {self.title}, author = {self.author}, isbn = {self.isbn}"

# Example: 

# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 

# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:

#     borrow_book(book) to add a book to the borrowed_books list.

#     return_book(book) to remove a book from the borrowed_books list.

#     __str__ method to return a string representation of the member.

#     @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

class Member:

    def __init__(self, name: str, member_id: int, borrowed_books: list[Book] = None) -> None:
        self.name = name
        self.member_id = member_id
        if borrowed_books != None:
            self.borrowed_books = borrowed_books
        else:
            self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book not in self.borrowed_books and book.borrowed == False:
            self.borrowed_books.append(book)
            book.borrowed = True

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.borrowed = False

    @classmethod
    def from_string(cls, member_str):
        params = [param.strip() for param in member_str.split(",")]
        if len(params) != 2:
            print("Wrong string format")
            return
        return Member(params[0], int(params[1]))
    
    def __str__(self) -> str:
        return f"name = {self.name}, member_id = {self.member_id}, borrowed_books: {self.borrowed_books}"


# Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.

class Library:

    total_books = 0 # Logicamente non ha molto senso che sia un attributo di classe, ma ok

    def __init__(self, books: list[Book] = None, members: list[Member] = None, total_books: int = 0) -> None:
        self.books = []
        if books != None:
            self.books = books
        
        self.members = []
        if members != None:
            self.members = members
        
        Library.total_books = len(self.books)

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)
            Library.total_books = len(self.books)

    def remove_book(self, book: Book) -> None:
        if book in self.books:
            self.books.remove(book)
            Library.total_books = len(self.books)

    def register_member(self, member) -> None:
        if member not in self.members:
            self.members.append(member)
            
    def lend_book(self, book: Book, member: Member) -> bool:
        if member in self.members and book.borrowed == False:
            return True
        
        return False
    
    @classmethod 
    def library_statistics(cls):
        return cls.total_books
    
    def __str__(self) -> str:
        return f"List of Books = {self.books}\nList of Members = {self.members}"


# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library. 
# Lend books to members and display the state of the library before and after lending.

"Poi lo faccio"


# Exercise 4: University Management System


# Create a system to manage a university with departments, courses, professors, and students. 

# Create an abstract class Person:
# Attributes:

#     name (string)
#     age (int)

# Methods:

#     __init__ method to initialize the attributes.
#     Abstract method get_role to be implemented by subclasses.
#     __str__ method to return a string representation of the person.

class Person(ABC):

    def __init__(self, name: str, age: int) -> None:
        super().__init__()
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self) -> str: 
        pass

    def __str__(self) -> str:
        return f"name = {self.name}, age = {self.age}"

# Create subclasses Student and Professor that inherit from Person and implement 
# the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
# Professor:
# Additional attributes: professor_id (string), department (string), courses 
# (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.

class Student(Person):

    def __init__(self, name: str, age: int, student_id: str, courses: list[Course]) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
        if courses and courses != []:
            self.courses = courses
    
    def get_role(self) -> str:
        return("Student")

    def enroll(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)


class Professor(Person):

    def __init__(self, name: str, age: int, professor_id: str, department: str, courses: list[Course]) -> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses = []
        if courses and courses != []:
            self.courses = courses

    def assign_to_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)

    def get_role(self) -> str:
        return "Professor"

# Create a class Course:
# Attributes:

#     course_name (string)
#     course_code (string)
#     students (list of Student instances)
#     professor (Professor instance)

# Methods:

#     __init__ method to initialize the attributes.
#     add_student(student) to add a student to the course.
#     set_professor(professor) to set the professor for the course.
#     __str__ method to return a string representation of the course.

class Course:

    def __init__(self, course_name: str, course_code: str, students: list[Student], professor: Professor) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        if students and students != []:
            self.students = students

        self.professor = professor

    def add_student(self, student: Student): 
        if student not in self.students:
            self.students.append(student)
            student.enroll(self)

    def set_professor(self, professor: Professor):
        self.professor = professor
        professor.assign_to_course(self)

    def __str__(self) -> str:
        return f"course_name = {self.course_name}, course_code = {self.course_code}, students = {self.students}, professor = {self.professor}"

# Create a class Department:

# Attributes:

#     department_name (string)
#     courses (list of Course instances)
#     professors (list of Professor instances)


# Methods:

#     __init__ method to initialize the attributes.
#     add_course(course) to add a course to the department.
#     add_professor(professor) to add a professor to the department.
#     __str__ method to return a string representation of the department.

class Department:

    def __init__(self, department_name, courses, professors) -> None:
        self.department_name = department_name
        self.courses = []
        if courses and courses != []:
            self.courses = courses
        if professors and professors != []:
            self.professors = professors
        
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor):
        if professor not in self.professors:
            self.professors.append(professor)

    def __str__(self) -> str:
        return f"department_name = {self.department_name}, courses = {self.courses}, professors = {self.professors}"


# Create a class University:

# Attributes:

#     name (string)
#     departments (list of Department instances)
#     students (list of Student instances)


# Methods:

#     __init__ method to initialize the attributes.
#     add_department(department) to add a department to the university.
#     add_student(student) to add a student to the university.
#     __str__ method to return a string representation of the university.

class University:

    def __init__(self, name: str, departments: list[Department], students: list[Student]) -> None:
        self.name = name
        self.departments = []
        if departments and departments != []:
            self.departments = departments
        
        self.students = []
        if students and students != []:
            self.students = students

    def add_department(self, department: Department):
        if department not in self.departments:
            self.departments.append(department)

    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)   

    def __str__(self) -> str:
        return f"name = {self.name}, departments = {self.departments}, students = {self.students}"

# Create a script:

# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.

"Magari dopo"