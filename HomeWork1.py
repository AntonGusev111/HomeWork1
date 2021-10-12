def mean_grades_students (student_list,course):
    grades_result=[]
    for student in student_list:
        for cour in student.grades:
            if cour == course:
                grades_result.append(sum(student.grades[cour])/len(student.grades[cour]))
    return f"Средняя оценка студентов по курсу {cour}: {sum(grades_result)/len(grades_result)}"


def mean_grades_Lecturer(Lecturer_list,course):
    grades_result = []
    for lecturer in Lecturer_list:
        for cour in lecturer.grades:
            if cour == course:
                grades_result.append(sum(lecturer.grades[cour]) / len(lecturer.grades[cour]))
    return f"Средняя оценка преподователей по курсу {cour}: {sum(grades_result) / len(grades_result)}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self,Lect,course,grade):
        if isinstance(Lect,Lecturer)  and course in self.courses_in_progress and course in Lect.courses_attached :
            if course in Lect.grades:
                Lect.grades[course] += [grade]
            else:
                Lect.grades[course] = [grade]
        else:
            return "Something wrong"
    def __str__(self):
        return (f"Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за домашние задания:{self.mean_grade(self.grades)} \nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы{self.finished_courses}") #Дописать функцию средней оценки, вызвать ее в return


    def mean_grade(self,grades):
        summ = 0
        num = 0
        if grades== {}:
            return 0
        else:
            for f_slice in grades:
                for s_slice in grades[f_slice]:
                    summ += s_slice
                    num += 1
            return summ / num

    def __lt__(self, other):
        return self.mean_grade(self.grades)<self.mean_grade(other.grades)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name,surname):
        Mentor.__init__(self,name,surname)
        self.grades={}

    def __str__(self):
        if self.grades == {}:
            r=0
        else:
            r=Student.mean_grade(None,self.grades)
        return (f"Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции:{r}")

    def __lt__(self, other):
        return Student.mean_grade(None,self.grades)<Student.mean_grade(None,other.grades)




class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя:{self.name} \nФамилия:{self.surname}")

f_student=Student('First',"ST","male")
s_student=Student('Second','ST','female')

f_rev=Reviewer('First','RV')
s_rev=Reviewer('Second','RV')

f_lect=Lecturer('First','LC')
s_lect=Lecturer('Second','LC')

f_student.courses_in_progress += ['Python']
s_student.courses_in_progress += ['Python']
f_rev.courses_attached += ['Python']
s_rev.courses_attached +=['Python']
f_lect.courses_attached +=['Python']
s_lect.courses_attached +=['Python']

f_student.rate_lecturer(f_lect,'Python',10)
f_student.rate_lecturer(f_lect,'Python',9)
f_student.rate_lecturer(f_lect,'Python',8)
f_student.rate_lecturer(f_lect,'Python',7)
print(f_lect.grades)
print("")

f_student.rate_lecturer(s_lect,'Python',1)
f_student.rate_lecturer(s_lect,'Python',2)
f_student.rate_lecturer(s_lect,'Python',3)
f_student.rate_lecturer(s_lect,'Python',4)
print(s_lect.grades)
print("")

f_rev.rate_hw(f_student,'Python',10)
f_rev.rate_hw(f_student,'Python',9)
f_rev.rate_hw(f_student,'Python',8)
f_rev.rate_hw(f_student,'Python',7)
print(f_student.grades)
print("")

f_rev.rate_hw(s_student,'Python',1)
f_rev.rate_hw(s_student,'Python',2)
f_rev.rate_hw(s_student,'Python',3)
f_rev.rate_hw(s_student,'Python',4)
print(s_student.grades)
print("")

print(f_lect>s_lect)
print("")
print(f_student>s_student)
print("")


print(f_student)
print("")
print(s_student)
print("")
print(f_lect)
print("")
print(s_lect)
print("")
print(f_rev)
print("")
print(s_rev)
print("")

print(mean_grades_students([f_student,s_student],'Python'))
print("")
print(mean_grades_Lecturer([f_lect,s_lect],'Python'))