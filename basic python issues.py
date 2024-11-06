def calculate_area(length, width):
    area = length * width
    return area

length = input("Waffle:\n")
width = input("Waffle:\n")

try:
    length = int(length)
    width = int(width)
except:
    length,width = 0,0

print(calculate_area(length,width))
