from time import time

# illa skrifað recursive fall til að sýna alla listana og lætin á lesanlegan hátt
def pretty_format(arg, indent = 0):
    s = " " * indent
    if type(arg) is dict:
        r = ""
        for i,x in arg.items():
            if type(x) is dict or type(x) is list:
                r = f"{r}\n{s}{i}:{pretty_format(x, indent + 4)}"
            else:
                r = f"{r}\n{s}{i}: {x}"
        return r
    elif type(arg) is list:
        r = ""
        for i,x in enumerate(arg):
            if ((i + 1) >= len(arg)):
                if type(x) is list or type(x) is dict:
                    r = f"{s}{r}{pretty_format(x, indent)}"
                else:
                    r = f"{s}{r}{x}"
            else:
                if type(x) is list or type(x) is dict:
                    r = f"{s}{r}{pretty_format(x, indent)}\n{s}---"
                else:
                    r = f"{s}{r}{x}"
        return r
    else:
        raise TypeError

def pretty_print(arg):
    print(pretty_format(arg))

class Student:
    def __init__(self, student_id, student_track, student_courses):
        self.id = student_id
        self.track = student_track
        self.courses = student_courses
    def student_info(self):
        return {
            "student_id": self.id,
            "student_track": self.track,
            "student_courses": self.courses
        }
    def list_courses(self):
        return [i for i in self.courses]
    def add_course(self, new_course):
        self.courses.append(new_course)

def main():
    student = Student(f'IS-{int(time())}', 'K2', [{"name": "ÍSLE2GO05BK", "long_name": "ÍSLE2GO05BK Íslenskt mál og menningarsaga", "credit": 3, "teacher": "Katrín Jóna Svavarsdóttir"}])
    pretty_print(student.student_info())
    pretty_print(student.list_courses())
    student.add_course({"name": "FORR2KT05BK", "long_name": "FORR2KT05BK Forritun 2", "credit": 3, "teacher": "Sigurður R Ragnarsson"})
    pretty_print(student.student_info())
    pretty_print(student.list_courses())

if __name__ == '__main__':
    main()