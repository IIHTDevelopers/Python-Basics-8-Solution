# Static Dataset of Students
students = {
    101: {'name': 'Alice Johnson', 'class': '10th Grade'},
    102: {'name': 'Bob Smith', 'class': '10th Grade'},
    103: {'name': 'Charlie Brown', 'class': '10th Grade'},
    104: {'name': 'David Lee', 'class': '10th Grade'},
    105: {'name': 'Eve Miller', 'class': '10th Grade'}
}

# Attendance Records (student_id: list of (date, status) tuples)
attendance = {
    101: [('2025-02-25', 'Absent'), ('2025-02-26', 'Absent') ,('2025-02-27', 'Absent')],
    102: [('2025-02-25', 'Absent'), ('2025-02-26', 'Present'),('2025-02-27', 'Present')],
    103: [('2025-02-25', 'Present'), ('2025-02-26', 'Absent'),('2025-02-27', 'Present')],
    104: [('2025-02-25', 'Present'), ('2025-02-26', 'Present'),('2025-02-27', 'Present')],
    105: [('2025-02-25', 'Absent'), ('2025-02-26', 'Present'),('2025-02-27', 'Absent')]
}


# Function 1: Count Number of Days Using Dates
def count_number_of_days_using_dates():
    """
    Counts the number of unique dates across all attendance records.
    """
    unique_dates = set()

    # Collect all unique dates from attendance records
    for records in attendance.values():
        for record in records:
            unique_dates.add(record[0])  # Add the date to the set

    # Count the number of unique dates
    total_days = len(unique_dates)

    return total_days




# Function 3: Find Most Absent Student
def find_most_absent_student():
    """
    Finds the student with the most absent days.
    """
    # Dictionary to store the count of absent days for each student
    absent_count = {}

    for student_id, records in attendance.items():
        absences = sum(1 for record in records if record[1] == 'Absent')
        absent_count[student_id] = absences

    # Find the student with the maximum absences
    most_absent_student = max(absent_count, key=absent_count.get)

    # Return student name and number of absences
    student_name = students[most_absent_student]['name']
    absent_days = absent_count[most_absent_student]

    return (student_name, absent_days)


# Main Function to Execute and Display Results
def main():
    # Count number of days using dates
    print("\n--- Count Number of Days Using Dates ---")
    total_days = count_number_of_days_using_dates()
    print(f"Total Number of Days: {total_days}")


    # Find the student with the most absent days
    print("\n--- Most Absent Student ---")
    most_absent = find_most_absent_student()
    print(f"Most Absent Student: {most_absent[0]} with {most_absent[1]} days absent.")

    # Return all calculated values
    return {
        "total_days": total_days,

        "most_absent_student": most_absent
    }


if __name__ == "__main__":
    result = main()
    print("\n--- Final Result ---")
    print(result)
