import matplotlib.pyplot as plt

def plot_regression(df, predictions, axis):
    plt.figure(figsize=(10,5))
    plt.scatter(df["seconds_from_start"], df[axis], s=10, label="Actual")
    plt.plot(df["seconds_from_start"], predictions, color="red", label="Regression")
    plt.legend()
    plt.title(f"Regression for {axis}")
    plt.show()