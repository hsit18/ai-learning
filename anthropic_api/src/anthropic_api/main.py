def greeting():
    print("Hi there for text tool editor")


def calculate_pi():
    """
    Calculate pi to the 5th decimal place (3.14159) using the
    Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    Iterates until the result is accurate to 5 decimal places.
    """
    pi_estimate = 0
    denominator = 1
    sign = 1

    for _ in range(1_000_000):
        pi_estimate += sign * (4 / denominator)
        denominator += 2
        sign *= -1

    return round(pi_estimate, 5)