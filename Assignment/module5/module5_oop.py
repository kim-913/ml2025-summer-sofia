class InputProcessor:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def search_number(self, x):
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1

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
