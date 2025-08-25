import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    try:
        n = int(input("Enter number of data points (n): "))
        if n <= 0:
            raise ValueError("n must be a positive integer.")

        k = int(input("Enter number of neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")

        print(f"Enter {n} data points (x then y):")

        points = np.zeros((n, 2), dtype=float)

        for i in range(n):
            x_val = float(input(f"Enter x value for point {i+1} - x: "))
            y_val = float(input(f"Enter y value for point {i+1} - y: "))
            points[i, 0] = x_val
            points[i, 1] = y_val

        x_train = points[:, 0].reshape(-1, 1)
        y_train = points[:, 1]

        label_var = np.var(y_train)
        print(f"Variance of labels: {label_var:.4f}")

        if k > n:
            print("Error: k cannot be greater than n.")
            return

        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(x_train, y_train)

        x_query = float(input("Enter the value of X to predict: "))
        y_pred = model.predict(np.array([[x_query]]))
        print(f"Predicted Y for X={x_query}: {y_pred[0]:.4f}")

    except ValueError as err:
        print(f"Invalid input: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")

if __name__ == "__main__":
    main()
