def compute_sum(X):
    X = str(X)
    total = int(X) + int(X * 2) + int(X * 3) + int(X * 4)
    return total

# Example usage
num = int(input("Enter a number: "))
print("Result:", compute_sum(num))
