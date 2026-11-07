def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(find_gcd(a, b))