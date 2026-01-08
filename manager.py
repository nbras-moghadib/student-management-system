from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, major):
        student = Student(student_id, name, age, major)
        self.students.append(student)
        print("تمت إضافة الطالب بنجاح")

    def list_students(self):
        if not self.students:
            print("لا يوجد طلاب")
            return

        for s in self.students:
            print(f"ID: {s.student_id} | الاسم: {s.name} | العمر: {s.age} | التخصص: {s.major}")

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("تم حذف الطالب")
                return
        print("الطالب غير موجود")
