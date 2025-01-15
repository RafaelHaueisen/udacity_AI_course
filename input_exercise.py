"""Exercise to practice input."""

names = input("Insert students names separated by commas: \n")
assignments = input("Insert missing assignments separated by commas: \n")
grades = input("Insert grades separated by commas: \n")

names = names.split(",")
assignments = assignments.split(",")
grades = grades.split(",")

for name, assignment, grade in zip(names, assignments, grades):
    print(f"Hi {name.title()},\n\nThis is a reminder that you have {int(assignment)} assignments left to \
    submit before you can graduate. Your current grade is {int(grade)} and can increase \
    to {int(grade) + 2*int(assignment)} if you submit all assignments before the due date.\n\n")