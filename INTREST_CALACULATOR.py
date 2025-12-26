# Interest Calculator in Python

def simple_interest(principal, rate, time):
    """
    Calculate Simple Interest

    Formula: SI = (P * R * T) / 100
    """
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, n=1):
    """
    Calculate Compound Interest
    Formula: CI = P * (1 + R/(100*n))^(n*T) - P
    n = number of times interest is compounded per year (default = 1)
    """
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return amount - principal


# Example usage
P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (%): "))
T = float(input("Enter the time (in years): "))

print("\n--- Results ---")
print(f"Simple Interest: {simple_interest(P, R, T):.2f}")
print(f"Compound Interest (compounded annually): {compound_interest(P, R, T):.2f}")
print(f"Compound Interest (compounded quarterly): {compound_interest(P, R, T, n=4):.2f}")