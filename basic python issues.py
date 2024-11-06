def calculate_area(length, width):
    area = length * width
    return area

length = input("Waffle stuff:\n")
width = input("Waffle more stuff:\n")

try:
    length = int(length)
    width = int(width)
except:
    length,width = 0,0

print(calculate_area(length,width))
