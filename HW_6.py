class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        '''Оценки лекторам'''
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self, course = ''):
        '''Средняя оценка студента'''
        ag = {}
        if course != [''] and course in self.grades.keys():
            ag = sum(self.grades[course]) / len(self.grades[course])
        else:
            for key, value in self.grades.items():
                ag[key] = round(sum(value) / len(value), 1)
        return ag

    def __str__(self):
        '''Информация о студенте'''
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за домашние задания: {self.average_grades()}\n'\
               f'Курсы в процессе изучения: {self.courses_in_progress}\n'\
               f'Завершенные курсы: {self.finished_courses}'

    def __lt__(self, other):
        '''Сравнение средних оценок между студентами'''
        if not isinstance(other, Student):
            return 'Not a Student!'
        return (sum(self.average_grades().values()) / len(self.average_grades())) < (sum(other.average_grades().values()) / len(other.average_grades()))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        '''Оценки студентам'''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        '''Информация о проверяющем'''
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self, course = ''):
        '''Средняя оценка лектора'''
        ag = {}
        if course != [''] and course in self.grades.keys():
            ag = sum(self.grades[course]) / len(self.grades[course])
        else:
            for key, value in self.grades.items():
                ag[key] = round(sum(value) / len(value), 1)
        return ag

    def __str__(self):
        '''Информация о лекторе'''
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {self.average_grades()}'

    def __lt__(self, other):
        '''Сравнение средних оценок между лекторами'''
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer!'
        return (sum(self.average_grades().values()) / len(self.average_grades())) < (sum(other.average_grades().values()) / len(other.average_grades()))


def average_grades_lecturer(list_of_participants, course):
    numbers = 0
    sum_average_grades = 0
    for i in list_of_participants:
        if course in i.courses_attached:
            numbers +=1
            sum_average_grades += i.average_grades(course)
    return f'Средняя оценка лекторов по курсу {course}: {round(sum_average_grades / numbers, 1)}'


def average_grades_student(list_of_participants, course):
    numbers = 0
    sum_average_grades = 0
    for i in list_of_participants:
        if course in i.courses_in_progress:
            numbers +=1
            sum_average_grades += i.average_grades(course)
    return f'Средняя оценка студентов по курсу {course}: {round(sum_average_grades / numbers, 1)}'


# __Student______________
student_01 = Student('Ruoy', 'Eman', 'This')
student_01.courses_in_progress += ['Python', 'JS']
student_01.finished_courses += ['Введение в программирование']

student_02 = Student('Ruby', 'Elan', 'It')
student_02.courses_in_progress += ['Python']
student_02.finished_courses += ['Введение в программирование']


# __Lecturer______________
lecturer_01 = Lecturer('Somme', 'Buudy')
lecturer_01.courses_attached += ['Python', 'JS']

lecturer_02 = Lecturer('Zoom', 'Bud')
lecturer_02.courses_attached += ['Python']


# __Reviewer______________
reviewer_01 = Reviewer('Some\'s', 'Buddy')
reviewer_01.courses_attached += ['Python', 'JS']

reviewer_02 = Reviewer('Some', 'Buddy')
reviewer_02.courses_attached += ['Python']


# __Grades______________
reviewer_01.rate_hw(student_01, 'JS', 300)
reviewer_01.rate_hw(student_01, 'JS', 4)
reviewer_01.rate_hw(student_01, 'JS', 167)

reviewer_01.rate_hw(student_01, 'Python', 8)
reviewer_01.rate_hw(student_01, 'Python', 4)
reviewer_01.rate_hw(student_01, 'Python', 7)

reviewer_02.rate_hw(student_01, 'Python', 5)
reviewer_02.rate_hw(student_01, 'Python', 1)
reviewer_02.rate_hw(student_01, 'Python', 4)

reviewer_01.rate_hw(student_02, 'Python', 3)
reviewer_01.rate_hw(student_02, 'Python', 4)
reviewer_01.rate_hw(student_02, 'Python', 3)

reviewer_02.rate_hw(student_02, 'Python', 5)
reviewer_02.rate_hw(student_02, 'Python', 4)
reviewer_02.rate_hw(student_02, 'Python', 2)

student_01.rate_hw(lecturer_01, 'Python', 9)
student_01.rate_hw(lecturer_01, 'Python', 10)
student_01.rate_hw(lecturer_01, 'Python', 9)
student_01.rate_hw(lecturer_01, 'JS', 999999)

student_02.rate_hw(lecturer_01, 'Python', 6)
student_02.rate_hw(lecturer_01, 'Python', 7)
student_02.rate_hw(lecturer_01, 'Python', 7)

student_01.rate_hw(lecturer_02, 'Python', 8)
student_01.rate_hw(lecturer_02, 'Python', 7)
student_01.rate_hw(lecturer_02, 'Python', 7)

student_02.rate_hw(lecturer_02, 'Python', 9)
student_02.rate_hw(lecturer_02, 'Python', 7)
student_02.rate_hw(lecturer_02, 'Python', 7)
# ________________



print(student_01)
print()
print(student_02)
print()
print(student_01 < student_02)
print(student_02 < student_01)
print(student_01 < lecturer_01)
print()
print(reviewer_01)
print()
print(reviewer_02)
print()
print(lecturer_01)
print()
print(lecturer_02)
print()
print(lecturer_01 < lecturer_02)
print(lecturer_02 < lecturer_01)
print(lecturer_01 < student_02)
print()
print(average_grades_lecturer([lecturer_01, lecturer_02], 'Python'))
print()
print(average_grades_student([student_01, student_02], 'JS'))
