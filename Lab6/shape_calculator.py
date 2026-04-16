import geometry_utils

x = input("'R': Rectange\n'T': Triagle\n'C': Circle\nPlease provide a shape type: ")

shapeDict = {"R": geometry_utils.rectangle_area,
             "T": geometry_utils.triangle_area,
             "C": geometry_utils.circle_area}

if x == "R":
    width = int(input("Please provide width of the rectange: "))
    height = int(input("Please provide height of the rectange: "))
    print(shapeDict.get(x)(width,height))
elif x == "T":
    base = input("Please provide base of the triangle: ")
    height = input("Please provide height of the triangle: ")
    print(shapeDict.get(x)(base,height))

elif x == "C":
    radius = input("Please provide radius of the circle: ")
    print(shapeDict.get(x)(radius))


