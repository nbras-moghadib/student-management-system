from manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n--- نظام إدارة الطلاب ---")
        print("1. إضافة طالب")
        print("2. عرض جميع الطلاب")
        print("3. حذف طالب")
        print("4. خروج")

        choice = input("اختر خيار: ")

        if choice == "1":
            student_id = input("رقم الطالب: ")
            name = input("الاسم: ")
            age = input("العمر: ")
            major = input("التخصص: ")
            manager.add_student(student_id, name, age, major)

        elif choice == "2":
            manager.list_students()

        elif choice == "3":
            student_id = input("رقم الطالب للحذف: ")
            manager.delete_student(student_id)

        elif choice == "4":
            print("تم الخروج من البرنامج")
            break

        else:
            print("خيار غير صحيح")

if __name__ == "__main__":
    main()
