import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

students = []

with open("student_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        students.append([row[0], int(row[1])])

marks = [student[1] for student in students]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

doc = SimpleDocTemplate("student_report.pdf")
elements = []

styles = getSampleStyleSheet()

elements.append(Paragraph("<b>Student Report</b>", styles["Title"]))
elements.append(Paragraph(f"Average Marks: {average:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest}", styles["Normal"]))

table_data = [["Name", "Marks"]]

for student in students:
    table_data.append(student)

table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
]))

elements.append(table)

doc.build(elements)

print("PDF Report Generated Successfully!")