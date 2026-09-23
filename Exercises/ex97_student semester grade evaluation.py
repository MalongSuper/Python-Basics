# 97. Student Semester Grade Evaluation

def get_subject_scores(subjects):
    first_list, mid_list, final_list = [], [], []
    print("Enter your scores below (First Term, Mid Term, Final Term):")

    for i in subjects:
        first, mid, final = eval(input(f"  + {i}: "))
        first_list.append(first)
        mid_list.append(mid)
        final_list.append(final)
    pe = input("+ PE: Pass or Fail? ")

    return first_list, mid_list, final_list, pe


def validate_scores(first_list, mid_list, final_list, pe_input):
    pe_status_valid = ["Pass", "P", "PASS", "pass", "p",
                       "Fail", "F", "FAIL", "fail", "f"]

    if pe_input not in pe_status_valid:
        print("Error: Invalid PE Input. Please proceed and try again.")
        return False

    elif (any(fir > 10 or fir < 0 for fir in first_list) or
          any(mid > 10 or mid < 0 for mid in mid_list) or
          any(fin > 10 or fin < 0 for fin in final_list)):
        print("Error: Invalid Score Input (scores must be between 0 and 10). Please proceed and try again.")
        return False

    return True


def calculate_averages(first_list, mid_list, final_list):
    average_list = []

    for i in range(len(first_list)):
        average = (first_list[i] + mid_list[i] * 2 + final_list[i] * 3) / 6
        average_list.append(average)

    return average_list


def determine_academic_status(total_average, average_list, pe):
    status_list = ["EXCELLENT", "GOOD", "INTERMEDIATE", "MARGINAL", "FAIL"]
    status = ""

    if total_average >= 8.0:
        if any(aver < 6.5 for aver in average_list):
            status = status_list[1]
        elif pe.lower() in ["fail", "f"]:
            status = status_list[2]
        else:
            status = status_list[0]

    elif total_average >= 6.5:
        if any(aver < 5.0 for aver in average_list):
            status = status_list[2]
        elif pe.lower() in ["fail", "f"]:
            status = status_list[3]
        else:
            status = status_list[1]

    elif total_average >= 5.0:
        if any(aver < 3.5 for aver in average_list):
            status = status_list[3]
        elif pe.lower() in ["fail", "f"]:
            status = status_list[4]
        else:
            status = status_list[2]

    elif total_average >= 3.5:
        if any(aver < 2.0 for aver in average_list):
            status = status_list[4]
        elif pe.lower() in ["fail", "f"]:
            status = status_list[4]
        else:
            status = status_list[3]

    else:
        status = status_list[4]

    return status


def display_report_card(subjects, first_list, mid_list, final_list, average_list, pe_input, total_average, status):
    print("\n\t\t\t\t\t\t\t\tReport Card\t\t\t\t\t")
    print("=" * 100)
    print('{:<20}{:<15}{:<15}{:<16}{:<20}'.format("Subject", "First Term", "Mid Term", "Final Term", "Average"))
    print("=" * 100)

    for j in range(len(subjects)):
        print('{:<25}{:<15.1f}{:<15.1f}{:<15.1f}{:<15.1f}'.format(subjects[j], first_list[j], mid_list[j], final_list[j], average_list[j]))

    print("{:<25}{:<15}".format("PE", pe_input))
    print("\nTotal Average: ", f"{total_average: .1f}")
    print(f"Status: {status}")


def student_grade():
    subjects = ["Math", "Literature", "English", "Physics",
                "Chemistry", "Biology", "History",
                "Geography", "Civics", "Computer Science",
                "Technology", "Musics & Arts"]

    print("Final Semester")
    first_list, mid_list, final_list, pe_input = get_subject_scores(subjects)

    if validate_scores(first_list, mid_list, final_list, pe_input):
        average_list = calculate_averages(first_list, mid_list, final_list)
        total_average = sum(average_list) / len(subjects)
        status = determine_academic_status(total_average, average_list, pe_input)
        display_report_card(subjects, first_list, mid_list, final_list, average_list, pe_input, total_average, status)


student_grade()
