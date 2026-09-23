# 84. Hypothesis Testing

def length(x):
    count = 0
    for i in range(len(x)):
        count += 1
    return count


def sample_mean(x):
    return sum(x) / len(x)


def sample_sd(x):
    mean = sample_mean(x)
    total = 0
    for i in range(len(x)):
        total += (x[i] - mean) ** 2

    return (total / (len(x) - 1)) ** 0.5


def alpha(conf):  # Confidence = 1 - alpha
    a = 1 - conf
    return a


def score_both_bounds(conf):  # Find Z score
    a = float(alpha(conf) / 2)
    x = round(1 - a, 4)  # Get up to four decimal places
    # Load Table A1 values
    table = {}

    with open("table a1.txt", "r") as file:
        for line in file:
            z_score, prob = map(float, line.strip().split(","))
            table[prob] = z_score

    # Find the closest probability to x
    closest_prob = min(table.keys(), key=lambda p: abs(p - x))
    z = table[closest_prob]

    return z


def ratio(n, x):  # Estimate point (or ratio)
    # n: total number of samples
    # x: the number of elements that satisfy sample
    f = length(x) / length(n)
    return f


def hypothesis_testing_average(n, x, s, u0, sig):
    t = ((n ** 0.5) / s) * abs(x - u0)  # Find t
    z = score_both_bounds(1 - sig)  # Find the z score using the parameter module

    print(f"t = {t}")
    print(f"z({sig}/2) = {z}")

    if t <= z:  # Not Reject / Accept H0 (u0)
        return True
    else:  # t > z -> Reject H0 / Accept H1: u ≠ u0
        return False


def hypothesis_testing_ratio(n, f, p0, sig):
    t = (n / (p0 * (1 - p0))) ** 0.5 * abs(f - p0)  # Find t
    z = score_both_bounds(1 - sig)  # Find the z score using the parameter module

    print(f"t = {t}")
    print(f"z({sig}/2) = {z}")

    if t <= z:  # Not Reject / Accept H0 (p0)
        return True
    else:  # t > z -> Reject H0 / Accept H1: u ≠ u0
        return False


print("Random Sample Table (Hypothesis Testing Average)")
sequence = []
n = int(input("Enter the length of the table: "))
for i in range(n):
    # Input a value and its frequency
    x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
    for j in range(f):
        sequence.append(x)

# Display the results for the random sample values
n = length(sequence)
x = sample_mean(sequence)
sd = sample_sd(sequence)

# Enter u0 for hypothesis testing problem
print("n:", n)
print("sample mean x:", x)
print("s:", sd)
u0 = float(input("Enter u0: "))

significance = float(input("Enter significance level: "))
t = hypothesis_testing_average(n, x, sd, u0, significance)

if t:  # If is True
    print(f"=> Not Reject H0 / Accept H0: u = {u0}")
else:  # If is False
    print(f"=> Reject H0: u = {u0} / Accept H1: u ≠ {u0}")
    if x < u0:
        print(f"=> Accept u < {u0}")
    else:  # >= 0
        print(f"=> Accept u ≥ {u0}")
# Input table
print("Random Sample Table (Hypothesis Testing Ratio)")
sequence = []
n = int(input("Enter the length of the table: "))

for i in range(n):
    # Input a value and its frequency
    x, f = eval(input(f"Enter x{i + 1} and its frequency: "))
    for j in range(f):
        sequence.append(x)

# Display the results for the random sample values
n = length(sequence)
print("n:", n)

number = int(input("Enter the satisfied number: "))
bound = int(input("Choose bound (0 - Lower; Any key - Higher): "))
x = []

if bound == 0:  # Lower
    for k in range(len(sequence)):
        # Get the number of events satisfying the satisfied number (higher case)
        if sequence[k] < number:
            x.append(sequence[k])
else:  # Higher
    for k in range(len(sequence)):
        # Get the number of events satisfying the satisfied number (lower case)
        if sequence[k] >= number:
            x.append(sequence[k])

print("Number of satisfied elements:", length(x))
f = ratio(sequence, x)  # Get the ratio f
# Enter p0 for hypothesis testing problem
p0 = float(input("Enter p0: "))
significance = float(input("Enter significance level: "))
t = hypothesis_testing_ratio(n, f, p0, significance)

if t:  # If is True
    print(f"=> Not Reject H0 / Accept H0: p = {p0}")
else:  # If is False
    print(f"=> Reject H0: p = {p0} / Accept H1: u ≠ {p0}")
    if f < p0:
        print(f"=> Accept p < {p0}")
    else:  # >= 0
        print(f"=> Accept p ≥ {p0}")
