def user_input_and_search():
    n = int(input("Enter how many numbers you will input : "))

    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    x = int(input("Enter the number to search for : "))

    if x in numbers:
        print(numbers.index(x) + 1)
    else:
        print(-1)


user_input_and_search()
