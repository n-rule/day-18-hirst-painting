#import colorgram

# extract = colorgram.extract('image.jpg', 20)
# colors = []
#
# for color in extract:
#     color_rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors.append(color_rgb)
#
# print(colors)

colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
          (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
          (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]
import random
import turtle


raf = turtle.Turtle()
raf.hideturtle()
raf.pensize(20)
turtle.colormode(255)
y = -200

for _ in range(10):
    raf.penup()
    raf.setpos(-250, y)
    for _ in range(10):
        raf.pendown()
        raf.dot(30, random.choice(colors))
        raf.penup()
        raf.forward(50)
    y += 50


my_screen = turtle.Screen()
my_screen.exitonclick()
