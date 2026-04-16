def circle_area(radius):
    if radius <= 0 :
        print("Radius cant be 0 or lesser!")
        return
    return 3.14 * radius**2

def circle_perimeter(radius):
    if radius <= 0 :
        print("Radius cant be 0 or lesser!")
        return
    return 2*3.14*radius

def rectangle_area(width, height):
    if width <= 0 or height <= 0 :
        print("Height or width cant be 0 or lesser!")
        return
    return width * height

def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0 :
        print("Height or width cant be 0 or lesser!")
        return
    return width*2 + height*2

def triangle_area(base, height):
    if base <= 0 or height <= 0 :
        print("Height or base cant be 0 or lesser!")
        return
    return height*base/2

