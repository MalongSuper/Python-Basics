# Grading System Using a 3-Dimensional List
scores = [
    [[11.5, 20.5], [11.0, 22.5], [15, 33.5], [13, 21.5], [15, 2.5]],
    [[4.5, 21.5], [11.0, 22.5], [15, 34.5], [12, 20.5], [14, 11.5]],
    [[6.5, 30.5], [11.4, 11.5], [11, 33.5], [11, 23.5], [10, 2.5]],
    [[6.5, 23.5], [11.4, 32.5], [13, 34.5], [11, 20.5], [16, 11.5]],
    [[8.5, 26.5], [11.4, 52.5], [13, 36.5], [13, 24.5], [16, 2.5]],
    [[11.5, 20.5], [11.4, 42.5], [13, 31.5], [12, 20.5], [16, 6.5]]
]


student_names = ["Student A", "Student B", "Student C",
                 "Student D", "Student E", "Student F"]

for i in range(len(scores)):
    mc_total = 0
    essay_total = 0

    for exam in scores[i]:
        mc_total += exam[0]
        essay_total += exam[1]

    mc_average = mc_total / len(scores[i])
    essay_average = essay_total / len(scores[i])

    overall_average = (mc_total + essay_total) / (len(scores[i]) * 2)

    print(student_names[i])
    print("Multiple Choice:", round(mc_average, 2))
    print("Essay:", round(essay_average, 2))
    print("Overall:", round(overall_average, 2))
    print()
