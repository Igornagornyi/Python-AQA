from stud import Student
from Homework_17.class_iterator.course import Course


if __name__ == '__main__':
    john = Student("John", "male", 18, "Python")
    mary = Student("Mary", "female", 23, "Javascript")
    tom = Student("Tom", "male", 30, "Ruby")
    kat = Student("Kat", "female", 29, "QA Automation")
    mike = Student("Mike", "male", 45, "DevOps")

    course_students = Course(1, 3, [john, mary, tom, kat])
    for student in course_students:
        print(student)
