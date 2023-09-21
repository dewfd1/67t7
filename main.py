import math

def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("0. Выход")

        choice = input("Введите номер операции: ")

        if choice == '0':
            print("До свидания!")
            break
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == '1':
                    result = num1 + num2
                    print("Результат: ", result)
                elif choice == '2':
                    result = num1 - num2
                    print("Результат: ", result)
                elif choice == '3':
                    result = num1 * num2
                    print("Результат: ", result)
                elif choice == '4':
                    if num2 == 0:
                        print("Ошибка! Деление на 0 невозможно.")
                    else:
                        result = num1 / num2
                        print("Результат: ", result)
            except ValueError:
                print("Ошибка! Введите числа.")

        elif choice in ['5', '6', '7', '8', '9', '10']:
            try:
                num = float(input("Введите число: "))

                if choice == '5':
                    exponent = float(input("Введите степень для возведения: "))
                    result = math.pow(num, exponent)
                    print("Результат: ", result)
                elif choice == '6':
                    result = math.sqrt(num)
                    print("Результат: ", result)
                elif choice == '7':
                    result = math.factorial(int(num))
                    print("Результат: ", result)
                elif choice == '8':
                    result = math.sin(num)
                    print("Результат: ", result)
                elif choice == '9':
                    result = math.cos(num)
                    print("Результат: ", result)
                elif choice == '10':
                    result = math.tan(num)
                    print("Результат: ", result)
            except ValueError:
                print("Ошибка! Введите число.")
        else:
            print("Неверный выбор. Попробуйте снова.")

calculator()