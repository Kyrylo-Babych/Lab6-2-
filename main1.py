#  Словник з даними 

student_db = {
    "Петренко Петро Петрович": {
        "group": "ІТ-21",
        "course": 2,
        "scholarship": True,
        "subjects": {
            "Програмування": 95,
            "Математичний аналіз": 88,
            "Англійська мова": 90
        }
    },
    "Іваненко Іван Іванович": {
        "group": "ІТ-21",
        "course": 2,
        "scholarship": True,
        "subjects": {
            "Програмування": 77,
            "Математичний аналіз": 75,
            "Англійська мова": 81
        }
    },
    "Сидоренко Марія Олегівна": {
        "group": "БП-21",
        "course": 2,
        "scholarship": False,
        "subjects": {
            "Програмування": 65,
            "Економіка": 70,
            "Англійська мова": 85
        }
    },
    "Коваленко Андрій Сергійович": {
        "group": "ІТ-21",
        "course": 2,
        "scholarship": True,
        "subjects": {
            "Програмування": 82,
            "Математичний аналіз": 80,
            "Фізика": 78
        }
    },
    "Бондаренко Олена Вікторівна": {
        "group": "БП-21",
        "course": 2,
        "scholarship": True,
        "subjects": {
            "Економіка": 95,
            "Менеджмент": 92,
            "Англійська мова": 98
        }
    },
    "Ткаченко Олег Ігорович": {
        "group": "ФМ-22",
        "course": 1,
        "scholarship": False,
        "subjects": {
            "Вища математика": 60,
            "Історія України": 75,
            "Правознавство": 70
        }
    },
    "Мельник Ірина Василівна": {
        "group": "ФМ-22",
        "course": 1,
        "scholarship": True,
        "subjects": {
            "Вища математика": 88,
            "Історія України": 82,
            "Правознавство": 90
        }
    },
    "Шевченко Тарас Григорович": {
        "group": "ІТ-21",
        "course": 2,
        "scholarship": True,
        "subjects": {
            "Програмування": 100,
            "Математичний аналіз": 95,
            "Англійська мова": 92
        }
    }
}

# Функції для роботи зі словником 

def add_new_student(db: dict):
    try:
        full_name = input("Введіть ПІБ студента: ")
        if not full_name:
            print("Помилка: ПІБ не може бути порожнім.")
            return
        if full_name in db:
            print(f"Помилка: Студент з ПІБ '{full_name}' вже існує в базі.")
            return

        group = input(f"Введіть номер групи для {full_name}: ")
        
        try:
            course = int(input(f"Введіть курс (1-6): "))
            if not 1 <= course <= 6:
                print("Помилка: Курс має бути в діапазоні 1-6. Встановлено 1.")
                course = 1
        except ValueError:
            print("Помилка введення. Курс має бути числом. Встановлено 1.")
            course = 1

        scholarship_input = input(f"Чи отримує стипендію? (так/ні): ").strip().lower()
        scholarship = True if scholarship_input == 'так' else False

        subjects = {}
        while True:
            subject_name = input("Введіть назву предмету (або 'стоп' для завершення): ")
            if subject_name.lower() == 'стоп':
                break
            if not subject_name:
                print("Назва предмету не може бути порожньою.")
                continue

            try:
                grade = int(input(f"Введіть оцінку за '{subject_name}' (0-100): "))
                if not 0 <= grade <= 100:
                    print("Помилка: Оцінка має бути в діапазоні 0-100.")
                    continue
                subjects[subject_name] = grade
            except ValueError:
                print("Помилка: Оцінка має бути цілим числом.")

        db[full_name] = {
            "group": group,
            "course": course,
            "scholarship": scholarship,
            "subjects": subjects
        }
        print(f"\nУспішно додано студента: {full_name}")

    except Exception as e:
        print(f"Під час додавання сталася непередбачена помилка: {e}")

def delete_student(db: dict):
    try:
        full_name = input("Введіть ПІБ студента для видалення: ")
        
        if full_name not in db:
            raise KeyError(f"Студента '{full_name}' не знайдено в базі.")
        
        del db[full_name]
        print(f"Студента '{full_name}' успішно видалено.")
        
    except KeyError as e:
        print(f"Помилка видалення: {e}")

def display_student_info(db: dict):
    try:
        full_name = input("Введіть ПІБ студента для пошуку: ")
        student = db[full_name]
        
        print(f"\n Інформація про студента: {full_name} ")
        print(f"Група: \t\t{student['group']}")
        print(f"Курс: \t\t{student['course']}")
        
        scholarship_status = "Так" if student['scholarship'] else "Ні"
        print(f"Стипендія: \t{scholarship_status}")
        
        print("Успішність:")
        if not student['subjects']:
            print("\t(Немає даних про предмети)")
        else:
            for subject, grade in student['subjects'].items():
                print(f"\t- {subject}: {grade}")
        print("-" * (30 + len(full_name)))

    except KeyError:
        print(f"\nПомилка: Студента з ПІБ '{full_name}' не знайдено в базі даних.")
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")

def get_sorted_by_average(db: dict):
    averages_list = []
    
    for full_name, details in db.items():
        grades = details.get('subjects', {})
        
        average_grade = 0.0
        if grades:
            total_sum = sum(grades.values())
            count = len(grades)
            average_grade = total_sum / count
        
        averages_list.append((full_name, average_grade))

    try:
        sorted_list = sorted(averages_list, key=lambda item: item[1], reverse=True)
        return sorted_list
    except Exception as e:
        print(f"Сталася помилка під час сортування: {e}")
        return []

def show_rating(db: dict):
    print("\n Рейтинг студентів за середнім балом ")
    rating = get_sorted_by_average(db)
    
    if not rating:
        print("Немає даних для відображення.")
        return
        
    print(f"{"№":<3} | {"Середній бал":<12} | {"ПІБ":<30}")
    print("-" * 50)
    for i, (name, avg) in enumerate(rating, 1):
        print(f"{i:<3} | {avg:<12.2f} | {name:<30}")

def list_all_students(db: dict):
    print("\n Загальний список студентів ")
    if not db:
        print("База даних порожня.")
        return
    
    for i, name in enumerate(db.keys(), 1):
        print(f"{i}. {name}")

#  Головне меню та цикл програми 

def print_menu():
    print("\n Меню бази даних студентів ")
    print("1. Вивести список всіх студентів")
    print("2. Знайти деталі про студента (за ПІБ)")
    print("3. Показати рейтинг (сортування за середнім балом)")
    print("4. Додати нового студента")
    print("5. Видалити студента")
    print("0. Вихід")

def main():
    while True:
        print_menu()
        choice = input("Оберіть пункт меню (0-5): ")

        if choice == '1':
            list_all_students(student_db)
        elif choice == '2':
            display_student_info(student_db)
        elif choice == '3':
            show_rating(student_db)
        elif choice == '4':
            add_new_student(student_db)
        elif choice == '5':
            delete_student(student_db)
        elif choice == '0':
            print("Завершення роботи програми. До побачення!")
            break
        else:
            print("Помилка: Невірний вибір. Будь ласка, введіть число від 0 до 5.")

if __name__ == "__main__":
    main()