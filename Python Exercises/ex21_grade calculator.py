# 21. Grade Calculator
# Calculate the average grade across
# three semesters and display the final grade category.

def grade(sem1, sem2, sem3):
    if any(grade > 100 or grade < 0 for grade in [sem1, sem2, sem3]):
        return "Invalid Input"

    mean = (sem1 + sem2 + sem3) / 3

    if any(grade < 25 for grade in [sem1, sem2, sem3]):
        print("Grade = Fail")
    elif mean >= 95:
        print("Grade = Excellent")
    elif mean >= 80:
        print("Grade = Great")
    elif mean >= 65:
        print("Grade = Good")
    elif mean >= 50:
        print("Grade = Pass")

    else:
        print("Grade = Fail")

    return f"{mean:.2f}"


sem1 = float(input("Enter semester 1 grade: "))
sem2 = float(input("Enter semester 2 grade: "))
sem3 = float(input("Enter semester 3 grade: "))
print("Mean:", grade(sem1, sem2, sem3))
