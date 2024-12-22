from factorial import factorial
from exp_root import exp3, exp2, root3, root2
from logarithm import log, ln, lg

def main():
    print("Виберіть функцію для виконання:")
    print("1. Факторіал")
    print("2. Піднесення до квадрату")
    print("3. Піднесення до кубу")
    print("4. Квадратний корінь")
    print("5. Кубічний корінь")
    print("6. Логарифм з основою")
    print("7. Натуральний логарифм")
    print("8. Десятковий логарифм")
    print("9. Вихід")

    choice = input("Ваш вибір:  ")

    try:

        if choice == "1":
            n = int(input("Введіть натуральне число: "))
            print("Результат:", factorial(n))
        elif choice == "2":
            x = float(input("Введіть число: "))
            print("Результат:", exp2(x))
        elif choice == "3":
            x = float(input("Введіть число: "))
            print("Результат:", exp3(x))
        elif choice == "4":
            x = float(input("Введіть додатне число: "))
            print("Результат:", root2(x))
        elif choice == "5":
            x = float(input("Введіть число: "))
            print("Результат:", root3(x))
        elif choice == "6":
            base = float(input("Введіть основу (більше 0, але не 1): "))
            num = float(input("Введіть число (більше 0): "))
            print("Результат:", log(base, num))
        elif choice == "7":
            num = float(input("Введіть число (більше 0): "))
            print("Результат:", ln(num))
        elif choice == "8":
            num = float(input("Введіть число (більше 0): "))
            print("Результат:", lg(num))
        elif choice == "9":
            print("Гарного дня")
            return
        else:
            print("Неправильний вибір!")
        print("\n")
        main()
    except ValueError as e:
        print("Помилка:", e)
        main()


main()