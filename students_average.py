def get_student_average(students):
  # Tu código aquí 👈
  newList = {
    "class_average": 0.0,
    "students": []
  }
  for student in students:
    generalGrade = 0.0
    for grade in student["grades"]:
      generalGrade += grade
    generalGrade = generalGrade / len(student["grades"])
    thisStudent = {
      "name": student["name"],
      "average": round(generalGrade, 2)
    }
    newList["class_average"] += generalGrade / len(students)
    newList["students"].append(thisStudent)
  newList["class_average"] = round(newList["class_average"], 2)
  return newList

get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
])