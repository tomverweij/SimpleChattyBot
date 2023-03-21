x = int(input())
y = int(input())
z = int(input())
TRIANGLE_TOTAL_DEGREES_ANGLES = 180

def is_triangle(a, b, c):
    return a + b + c == TRIANGLE_TOTAL_DEGREES_ANGLES

if is_triangle(x, y, z):
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
