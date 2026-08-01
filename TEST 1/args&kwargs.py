def student_report(name ,*subjects  , **details):
    print(name + ": " + ", "    .join(subjects))
    print(details)
student_report("John", "Math", "Science", age=15, grade="10th")