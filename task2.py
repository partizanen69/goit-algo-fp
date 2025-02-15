# Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала 
# “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач 
# повинен мати можливість вказати рівень рекурсії.
# - Код виконується. Програма візуалізує фрактал “дерево Піфагора”.
# -Користувач має можливість вказати рівень рекурсії.

import turtle
import math

def pythagorean_tree(level, length):
	if level == 0:
		turtle.forward(length)
		turtle.backward(length)
		return

	turtle.forward(length)

	turtle.left(30)
	pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
	turtle.right(30)

	turtle.right(30)
	pythagorean_tree(level - 1, length * math.sqrt(2) / 2)
	turtle.left(30)

	turtle.backward(length)

if __name__ == "__main__":
	turtle.speed('fastest')
	turtle.left(90)
	turtle.color("black")

	pythagorean_tree(6, 200)

	turtle.done()
