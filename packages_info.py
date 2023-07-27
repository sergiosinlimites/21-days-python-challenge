def get_packages_info(packages):
  # Tu código aquí 👈
  output = {
    "total_weight": 0.0,
    "destinations": {}
  }
  for package in packages:
    output["total_weight"] += package[1]
    if(package[2] in output["destinations"]):
      output["destinations"][package[2]] += 1
    else:
      output["destinations"][package[2]] = 1
  output["total_weight"] = round(output["total_weight"], 2)
  return output

res = get_packages_info([
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
])

print(res)