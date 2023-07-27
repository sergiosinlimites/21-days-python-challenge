def find_famous_cat(cats):
  famosos = []
  maxCount = 0
  for cat in cats:
    count = 0
    for num in cat['followers']:
      count += num
    if(count == maxCount):
      famosos.append(cat['name'])
    elif(count > maxCount):
      maxCount = count
      famosos = []
      famosos.append(cat['name'])
  print(famosos)
  return famosos


find_famous_cat([
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
])