import pandas as pd

student_grades = pd.read_csv('student_grades.csv')

# Calculate the average of the student marks
student_avgGrades = pd.DataFrame(columns=['Roll No', 'Student Name', 'Average Marks'])
student_avgGrades['Roll No'] = student_grades['Roll No']
student_avgGrades['Student Name'] = student_grades['Student Name']
student_avgGrades['Average Marks'] = student_grades.iloc[:, 2:].mean(axis=1)

# Writing Average Marks to a new CSV file
student_avgGrades.to_csv('student_average_grades_with_pandas.csv', index=False)