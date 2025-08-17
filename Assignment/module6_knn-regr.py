import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = None

    def fit(self, x, y):
        self.points = np.column_stack((x, y))

    def predict(self, x_query):
        if self.points is None:
            raise ValueError("No training data available.")
        distances = np.abs(self.points[:, 0] - x_query)
        nearest_indices = np.argsort(distances)[:self.k]
        return np.mean(self.points[nearest_indices, 1])

def main():
    try:
        n = int(input("Enter n(number of points): "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Error: n must be a positive integer.")
        return

    try:
        k = int(input("Enter k (number of neighbors): "))
        if k <= 0:
            raise ValueError
    except ValueError:
        print("Error: k must be a positive integer.")
        return

    x, y = [], []
    for i in range(n):
        try:
            x_val = float(input(f"Enter x value for point {i+1}: "))
            y_val = float(input(f"Enter y value for point {i+1}: "))
        except ValueError:
            print("Error: x and y must be real numbers.")
            return
        x.append(x_val)
        y.append(y_val)

    x, y = np.array(x), np.array(y)

    try:
        x_query = float(input("Enter the query x value: "))
    except ValueError:
        print("Error: x must be a real number.")
        return

    if k > n:
        print("Error: k cannot be greater than n.")
        return

    model = KNNRegressor(k)
    model.fit(x, y)
    y_pred = model.predict(x_query)

    print(f"Predicted y for x={x_query} is: {y_pred:.4f}")


if __name__ == "__main__":
    main()
