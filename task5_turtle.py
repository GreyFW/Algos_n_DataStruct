import turtle
import random

BROWN_COLOR = "#4D2E10"
GREEN_COLOR = "#66D466"

# 0: Исходная
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()

# 1: Измените толщину ветвей
def tree_1(branchLen, t, width=10):  
    if branchLen > 5:  
        t.pensize(max(1, width))
        t.forward(branchLen)
        t.right(20)
        tree_1(branchLen - 15, t, width=width - 2)
        t.left(40)
        tree_1(branchLen - 15, t, width=width - 2)
        t.right(20)
        t.backward(branchLen)

def main_1():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree_1(75, t)
    myWin.exitonclick()

def change_color(branchLen):
    return GREEN_COLOR if branchLen <= 15 else BROWN_COLOR

# 2: Измените цвет ветвей
def tree_2(branchLen, t, width=10):
    if branchLen > 5:
        # текущий сегмент
        t.color(change_color(branchLen))
        t.pensize(max(1, width))
        t.forward(branchLen)

        # правая ветвь
        child_len = branchLen - 15
        t.right(20)
        prev = t.pencolor()
        t.color(change_color(child_len))
        tree_2(child_len, t, width=width-2)
        t.color(prev)

        # левая ветвь
        child_len = branchLen - 15
        t.left(40)
        prev = t.pencolor()
        t.color(change_color(child_len))
        tree_2(child_len, t, width=width-2)
        t.color(prev)

        t.right(20)
        t.backward(branchLen)


def main_2():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree_2(75, t)
    myWin.exitonclick()

# 3: Случайный угол поворота
def tree_3(branchLen, t, width=10):
    if branchLen > 5:
        t.color(change_color(branchLen))
        t.pensize(max(1, width))
        t.forward(branchLen)

        # правая ветвь со случайным углом
        right_angle = random.randint(15, 45)
        child_len = branchLen - 15
        t.right(right_angle)
        prev = t.pencolor()
        t.color(change_color(child_len))
        tree_3(child_len, t, width=width-2)
        t.color(prev)

        # левая ветвь со случайным углом
        left_angle = random.randint(15, 45)
        child_len = branchLen - 15
        t.left(right_angle + left_angle)
        prev = t.pencolor()
        t.color(change_color(child_len))
        tree_3(child_len, t, width=width-2)
        t.color(prev)

        t.right(left_angle)
        t.backward(branchLen)
   
def main_3():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree_3(75, t)
    myWin.exitonclick()

# 4: Вычитание случайной длины + всё остальное
def tree_4(branchLen, t, width=10):
    if branchLen > 5:
        # текущий сегмент
        t.color(change_color(branchLen))
        t.pensize(max(1, width))
        t.forward(branchLen)

        # правая ветвь
        angle = random.randint(15, 45)
        t.right(angle)
        reduction = random.randint(10, 20)
        next_len = max(5, branchLen - reduction)
        prev = t.pencolor()
        t.color(change_color(next_len))
        tree_4(next_len, t, width=width - 2)
        t.color(prev)

        # левая ветвь
        t.left(angle * 2)
        reduction = random.randint(10, 20)
        next_len = max(5, branchLen - reduction)
        prev = t.pencolor()
        t.color(change_color(next_len))
        tree_4(next_len, t, width=width - 2)
        t.color(prev)

        t.right(angle)
        t.backward(branchLen)

def main_4():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree_4(75, t)
    myWin.exitonclick()

print("Какую версию хотите запустить:")
print(" 0 - Исходная")
print(" 1 - Толщина ветвей")
print(" 2 - Цвет + толщина ветвей")
print(" 3 - Цвет + толщина + угол")
print(" 4 - Цвет + толщина + угол + длина")

choice = int(input("Ваш выбор -> "))
if choice == 0:
    main()
elif choice == 1:
    main_1()
elif choice == 2:
    main_2()
elif choice == 3:
    main_3()
elif choice == 4:
    main_4()
else:
    print("Некорректный ввод.")