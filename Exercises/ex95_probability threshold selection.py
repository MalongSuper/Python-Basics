# 95. Probability Threshold Selection

def find_min_selections(maximum, p):
    n = 1  # Initialize n (number of trials)

    # We need P(X >= 1) >= maximum, where P(X >= 1) is the probability of at least one success.
    # P(X >= 1) = 1 - P(X = 0)
    # P(X = 0) is the probability of zero successes in n trials, which is (1-p)^n.
    while True:
        prob_at_least_one_success = 1 - ((1 - p) ** n)

        if prob_at_least_one_success >= maximum:
            return n, prob_at_least_one_success
        n += 1


maximum = float(input("Enter target probability (between 0 and 1): "))

if not (0 <= maximum <= 1):
    print("Error: Target probability must be between 0 and 1.")
else:
    p = float(input("Enter probability of one trial p (between 0 and 1): "))
    if not (0 <= p <= 1):
        print("Error: Probability of one trial p must be between 0 and 1.")
    elif p == 0:
        print("Error: Probability of success cannot be zero.")
    else:
        n_min, actual_prob = find_min_selections(maximum, p)
        print("The maximum probability is reached when:")
        print(f"n = {n_min} => P(at least one success) = {actual_prob:.6f}")
