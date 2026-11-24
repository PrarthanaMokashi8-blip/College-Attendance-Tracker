def add_attendance(classes_held, classes_attended):
    if classes_held < 0 or classes_attended < 0:
        raise ValueError("Class counts cannot be negative.")
    if classes_attended > classes_held:
        raise ValueError("Attended classes cannot exceed classes held.")
    return classes_held, classes_attended
def calculate_percentage(classes_held, classes_attended):
    add_attendance(classes_held, classes_attended)
    if classes_held == 0:
        return 0.0
    return (classes_attended / classes_held) * 100
def check_eligibility(percentage, required=75):
    return percentage >= required
def display_report(name, classes_held, classes_attended):
    percentage = calculate_percentage(classes_held, classes_attended)
    status = "Eligible" if check_eligibility(percentage) else "Not eligible"
    print("\n--- Attendance Report ---")
    print("Student:", name)
    print("Classes held:", classes_held)
    print("Classes attended:", classes_attended)
    print(f"Attendance: {percentage:.2f}%")
    print("Status:", status)
def main():
    print("COLLEGE ATTENDANCE TRACKER")
    name = input("Enter student name: ")
    try:
        held = int(input("Enter total classes held: "))
        attended = int(input("Enter classes attended: "))
        display_report(name, held, attended)
    except ValueError as error:
        print("Invalid input:", error)
if __name__ == "__main__":
    main()