# minMax returns two functional values
def minMaxGrades(gradeM):
    min = 200  # large value
    max = 0  # small value
    for grade in gradeM:
        if grade < min:
            min = grade
        if grade > max:
            max = grade
    return min, max  # returns 2 values


grades = [100, 90, 95, 75]
low, high = minMaxGrades(grades)
print("low is", low, "high is", high)
