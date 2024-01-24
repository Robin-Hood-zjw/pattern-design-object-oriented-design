from abc import ABC


class Student(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def get_name(self):
        return self.name
        
    def get_ID(self):
        return self.id


class Iterator(ABC):
    def check_next(self):
        pass
    
    def get_next(self):
        pass

class StudentIterator(Iterator):
    def __init__(self, students):
        self.students = students
        self.cur_index = 0
        
    def check_next(self):
        return self.cur_index < len(self.students)
        
    def get_next(self):
        if self.check_next():
            result = self.students[self.cur_index]
            self.cur_index += 1
            return result
        
        return None


class Collection(ABC):
    def iterate(self):
        pass
    
class StudentCollection(Collection):
    def __init__(self):
        self.students = list()
        
    def add_student(self, student):
        self.students.append(student)

    def get_iterater(self):
        return StudentIterator(self.students)

if __name__ == '__main__':
    collection = StudentCollection()

    collection.add_student(Student('Ada', '010'))
    collection.add_student(Student('Brian', '020'))
    collection.add_student(Student('Estelle', '030'))
    collection.add_student(Student('Fiona', '040'))
    collection.add_student(Student('Gabrinda', '050'))

    iterator = collection.get_iterater()

    for _ in range(5):
        student = iterator.get_next()
        print(f'{student.get_name()} {student.get_ID()}')