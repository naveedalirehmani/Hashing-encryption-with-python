# main.py
from square import calculate_square
from cube import calculate_cube

def main():
    num = int(input("Enter a number: "))
    square = calculate_square(num)
    cube = calculate_cube(num)
    print(f"The square of {num} is {square}")
    print(f"The cube of {num} is {cube}")

if __name__ == "__main__":
    main()
