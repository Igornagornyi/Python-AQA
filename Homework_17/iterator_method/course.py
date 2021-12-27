from typing import List
from stud import Student


class Course:
    def __init__(self, start_index: int, end_index: int, students: List[Student] = None) -> None:
        self.__students = [] if not students else students
        self.__start_index = start_index
        self.__end_index = end_index

    def add_student(self, student: Student) -> None:
        return self.__students.append(student)

    def add_students(self, students: List[Student]) -> None:
        self.__students.extend(students)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__end_index <= len(self.__students):
            student = self.__students[self.__start_index]
        while self.__start_index <= self.__end_index:
            self.__start_index += 1
            return student
        else:
            raise StopIteration
