# Brief:
# Create a program that calculates the area and perimeter of common shapes like rectangles, circles, and triangles based on user input.

def triangle():
  
    def perimeter_triangle(a, b, c):
        perimeter = a + b + c
        return perimeter

    def area_triangle(base, height):
        area = 0.5 * base * height
        return area 
  
    operation = input("Area or perimeter? ").lower()
    if operation == 'area':
        base = int(input("Enter value for triangle base: "))
        height = int(input("Enter value for height: "))
        print("Area of the triangle:", area_triangle(base, height))
    elif operation == 'perimeter':
      a = int(input("Enter value a (side length): "))
      b = int(input("Enter value b (side length): "))
      c = int(input("Enter value c (side length): "))
      print("Perimeter of the triangle:", perimeter_triangle(a, b, c))

def square():
  side = int(input("Enter value any side: "))


  def perimeter_square(side):
    perimeter = 4 * side
    return perimeter

  def area_square(side):
    area = side ** 2
    return area

  operation = input("Area or perimeter? ").lower()
  if operation == 'area':
    print(f"Area of the square: {area_square(side)}")
  elif operation == 'perimeter':
    print(f"Perimeter of the square: {perimeter_square(side)}")

def main():
    shape = input("Enter your shape (e.g., 'square' or 'triangle'): ")
  
    if shape == 'triangle':
        triangle()
    elif shape == 'square':
        square()
    else:
        print("Invalid shape. This program supports triangle and square only.")

if __name__ == '__main__':
    main()
