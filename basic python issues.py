def calculate_area(length, width):
    area = length * width
    return area
        
def calculate_triangle_area(height, width):
    area = height * width * 0.5 
    return area

length = input("Waffle stuff:\n")
width = input("Waffle more stuff:\n")

try:
    length = int(length)
    width = int(width)
except:
    length,width = 0,0

print("Area is: ", calculate_area(length,width))
print("Triangle are is: ", calculate_triangle_area(length,width))
