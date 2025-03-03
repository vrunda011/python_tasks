class Student:

    # Class Variable
    school = 'Telusko'

    # Instance variables
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

s1 = Student(23,30,38)
s1 = Student(33,34,36)

print(s1.avg())
print(Student.getSchool())