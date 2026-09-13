# Store each student's grades in a dictionary
student_grades = {
    "Jacob": [90, 88, 82],
    "Boone": [79, 84, 89],
    "Greg": [80, 85, 94]
}

# Calculate the average grade for each student and store it in a new dictionary
student_averages = {}

for student_name, grade_list in student_grades.items():
    average_score = sum(grade_list) / len(grade_list)
    student_averages[student_name] = average_score

# Calculate the letter grade for each student based on their average score and store it in a new dictionary
student_letter_grades = {}

for student_name, average_score in student_averages.items():
    if average_score >= 90:
        letter_grade = "A"
    elif average_score >= 80:
        letter_grade = "B"
    elif average_score >= 70:
        letter_grade = "C"
    elif average_score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    student_letter_grades[student_name] = letter_grade

# Find the student with the highest average score
top_student = ""
highest_average = 0

for student_name, average_score in student_averages.items():
    if average_score > highest_average:
        highest_average = average_score
        top_student = student_name

# Calculate the overall class average  
class_average = sum(student_averages.values()) / len(student_averages)

# Calculate how many students passed the class (received a letter grade of A, B, or C)
passing_count = 0

for letter_grade in student_letter_grades.values():
    if letter_grade == "A" or letter_grade == "B" or letter_grade == "C":
        passing_count = passing_count + 1

# Display the results
print("Top student:", top_student, "-", round(highest_average, 2))
print("Class average:", round(class_average, 2))
print("Number of students who passed:", passing_count)