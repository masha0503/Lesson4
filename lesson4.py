class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        self.pensione = value >= 60

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')

# personX = Person(name='unknown_name', surname='unknown_surname', age=30)
# personX.info_person()

class Teacher(Person):
    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()

teacher = Teacher(subject='Pycharm', hours=24, name='unknown_name', surname='unknown_surname', age=30)
teacher.info_all()

class Student(Person):
    def __init__(self, name: str, surname: str, age: int, progress: str, group: 'Group'):
        self.progress = progress
        self.group = group
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_student(self):
        print(f'student:\t{self.progress} | {self.group}')

    def info_all(self):
        self.info_person()
        self.info_student()

class Worker(Person):
    def __init__(self, name: str, surname: str, age: int, position: str, duties: str):
        self.position = position
        self.duties = duties
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_worker(self):
        print(f'worker:\t{self.position} | {self.duties}')

    def info_all(self):
        self.info_person()
        self.info_worker()

class Group:
    def __init__(self, name: str, num_students: int, age_category: str):
        self.name = name
        self.num_students = num_students
        self.age_category = age_category

    def info_group(self):
        print(f'Group: {self.name} | {self.age_category} | {self.num_students} students')

# Создаем экземпляр класса Group
group = Group(name='С2126', num_students=17, age_category='13-15')
group.info_group()

# Информация о студенте
student = Student(name='Mariia', surname='Ruskikh', age=14, progress='good', group=group)
student.info_all()

# Информация о работнике
worker = Worker(name='Mariia', surname='Ruskikh', age=14, position='art designer', duties='advertising brochure design')
worker.info_all()
