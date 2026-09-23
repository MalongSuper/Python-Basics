# 63. Vietnamese Lunar Year

def get_vietnamese_lunar_year(year):
    lunar_year = []

    # Using dictionary to store the values
    thap_can = {"Giáp": 4, "Ất": 5, "Bính": 6, "Đinh": 7, "Mậu": 8,
               "Kỷ": 9, "Canh": 0, "Tân": 1, "Nhâm": 2, "Quý": 3}

    thap_nhichi = {"Tý": 0, "Sửu": 1, "Dần": 2, "Mão": 3, "Thìn": 4, "Tỵ": 5,
                   "Ngọ": 6, "Mùi": 7, "Thân": 8, "Dậu": 9, "Tuất": 10, "Hợi": 11}

    # Retrieve the corresponding value for Thap Can
    nam_can = (year - 1900) % 10

    for i, j in thap_can.items():
        if j == nam_can:
            lunar_year.append(i)

    # Retrieve the corresponding value for Thap Nhi Chi
    nam_chi = (year - 1900) % 12

    for m, n in thap_nhichi.items():
        if n == nam_chi:
            lunar_year.append(m)

    return lunar_year


year = int(input("Enter a year: "))
print("Vietnamese Lunar Year:", ' '.join(get_vietnamese_lunar_year(year)))
