from turtle import *


def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 3.0
    
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def create_snowflake(sides, length):
    colors = ["green", "blue", "red", "purple" ]
    
    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)

left(60)
create_snowflake(4, 200)

mainloop()
