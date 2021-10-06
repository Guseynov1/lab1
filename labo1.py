import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math as math
import colorama as color

def choise():
    inertialessUnitName = "Безынерционное звено"
    aperiodicUnitName = "Апериодическое звено"
    realdifferUnitName = "Реальное дифференцирующее звено"
    integratingUnitName = "Интегрирующее звено"
    idealdifferUnitName = "Идеальное дифференцирующее звено"


    needNewChoise = True

    while needNewChoise:
        print(color.Style.RESET_ALL)
        userInput = input("Введите номер команды: \n"
                          "1 - " + inertialessUnitName + ";\n"
                          "2 - " + aperiodicUnitName + ";\n"
                          "3 - " + realdifferUnitName + ";\n"
                          "4 - " + idealdifferUnitName + ";\n"
                          "5 - " + integratingUnitName + ".\n")


        if userInput.isdigit():
            needNewChoise = False
            userInput = int(userInput)
            if userInput == 1:
                name = "Безынерционное звено"
            elif userInput == 2:
                name = "Апериодическое звено"
            elif userInput == 3:
                name = "Реальное дифференцирующее звено"
            elif userInput == 4:
                name = "Идеальное дифференцирующее звено"
            elif userInput == 5:
                name = "Интегрирующее звено"

            else:
                print(color.Fore.RED + "\nНедопустимое значение!")
                needNewChoise = True


        else:
            print(color.Fore.RED + "\nПожалуйста, введите числовое значение!")
            needNewChoise = True
    return name

def getUnit(name):

    needNewChoise = True
    while needNewChoise:
        print(color.Style.RESET_ALL)
        needNewChoise = False
        k = input('пожалуйста, введите коэффициент "k": ')
        t = input('пожалуйста, введите коэффициент "t": ')

        if k.isdigit() and t.isdigit():
            k = int(k)
            t = int(t)
            if name == "Безынерционное звено":
                unit = matlab.tf([k], [1])
            elif name == "Апериодическое звено":
                unit = matlab.tf([k], [t, 1])
            elif name == "Реальное дифференцирующее звено":
                unit = matlab.tf([k, 0], [t, 1])
            elif name == "Идеальное дифференцирующее звено":
                unit = matlab.tf([k, 0], [1 / 100000, 1])
            elif name == "Интегрирующее звено":
                unit = matlab.tf([1], [t, 0])

        else:
            print(color.Fore.RED + "\nПожалуйста, введите числовое значение!")
            needNewChoise = True
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2,1, num)
    pyplot.grid(True)
    if title == "Переходная характеристика":
        pyplot.plot(x, y, "purple")
    elif title == "Импульсная характеристика":
        pyplot.plot(x, y, "green")


    pyplot.title(title)
    pyplot.ylabel("Амплитуда")
    pyplot.xlabel("Время (с)")


unitName = choise()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)

[y, x] = matlab.step(unit, timeLine)
graph(1, "Переходная характеристика", y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, "Импульсная характеристика", y, x)


pyplot.show()
matlab.bode(unit, dB=False)
pyplot.plot()
pyplot.xlabel("Частота, Гц")
pyplot.show()
