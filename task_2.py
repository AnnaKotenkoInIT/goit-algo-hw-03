import turtle

def koch_side(t, order, size):
    if order==0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_side(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_side(t, order, size)
        t.right(120)

def draw_koch_snowflake(order, size=400):
    screen = turtle.Screen()
    
    t = turtle.Turtle()
    t.speed(0)

    # вирівнюємо по центру
    t.penup()
    t.goto(-size / 2, size / 3)  # вліво і вгору
    t.pendown()

    koch_snowflake(t, order, size)

    screen.mainloop()

if __name__ == "__main__":
    try: 
        order = int(input("Enter recursion level: "))
        draw_koch_snowflake(order)
    except ValueError:
        print("Invalid input. Please, enter the number for the recursion level of Koch snowflake.")