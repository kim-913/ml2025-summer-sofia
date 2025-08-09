from module5_mod import InputProcessor

def main():
    N = int(input("Enter a positive integer N: "))

    processor = InputProcessor()

    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        processor.insert_number(num)

    X = int(input("Enter the number to search for: "))

    result = processor.search_number(X)
    print(result)


if __name__ == "__main__":
    main()
