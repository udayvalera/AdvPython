import csv

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    return sum(grades) / len(grades)

def validate_grades(grades):
    """Validate that all grades are within the valid range (0-100)."""
    for grade in grades:
        if grade < 0 or grade > 100:
            raise ValueError(f"Grade {grade} is out of valid range (0-100).")

def main():
    # Dictionary to store student names and their average scores
    student_averages = {}
   
    # Read the data from 'student_grades.csv'
    with open('student_grades.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            name = row['Student Name']
            # Extract grades and validate them
            grades = [float(row['Math']), float(row['Science']), float(row['English']),
                      float(row['History']), float(row['Geography'])]
            
            try:
                validate_grades(grades)
                average_score = calculate_average(grades)
                student_averages[name] = average_score
            except ValueError as e:
                print(f"Skipping student {name} due to error: {e}")

    # Write the average scores to 'student_average_grades.csv'
    with open('student_average_grades.csv', mode='w', newline='') as outfile:
        fieldnames = ['Name', 'Average']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for name, average in student_averages.items():
            writer.writerow({'Name': name, 'Average': average})

    print("Average scores have been written to 'student_average_grades.csv'.")

if __name__ == "__main__":
    main()
