def main():
    array1 = [10, 8, 32, 25, 1, 92, 40, 51, 7] # list
    print(array1) # print

    name = input("Enter your name: ") # input
    print("Hello, " + name) # using user input variable

    x, y, z = str(5), int(5), float(5) # multiple declarations
    print(type(x))
    print(type(y))
    print(type(z))

    a = b = c = "Poop" # multiple delcarations with same value
    fruits = ["mango", "banana", "watermelon"]
    f1, f2, f3 = fruits
    print(f1, f2, f3)

    global victoryMa # global variable


if __name__ == '__main__':
    main()