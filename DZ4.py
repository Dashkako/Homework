#Задание 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

#Задание 2

class Rectangle:
    def __init__(self, left_bottom, right_top):
        self.left_bottom = left_bottom
        self.right_top = right_top

    def area (self):
       a = self.right_top.x - self.left_bottom.x
       b = self.right_top.y - self.left_bottom.y
       return a*b

    def perimetr(self):
       a = self.right_top.x - self.left_bottom.x
       b = self.right_top.y - self.left_bottom.y
       return (a + b)*2


point1 = Point(10, 6)
point2 = Point(5, 15)
rectangle = Rectangle(point1, point2)

print(f"Площадь - {rectangle.area()}\nПериметр - {rectangle.perimetr()}")

#Задание 3
def contains(self, point):
    # Проверяем, находится ли точка внутри прямоугольника
    if (self.left_bottom.x <= point.x <= self.right_top.x and
            self.left_bottom.y <= point.y <= self.right_top.y):
        return True
    else:
        return False

#Задание 4
class DecimalCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1
        else:
            print("Не может опускаться ниже нуля")

    def get_counter(self):
        return self.value

if __name__ == "__main__":

decimal_counter = DecimalCounter()
decimal_counter.increment()
decimal_counter.increment()
print(decimal_counter.get_counter())
decimal_counter.decrement()
decimal_counter.decrement()
print(decimal_counter.get_counter())
