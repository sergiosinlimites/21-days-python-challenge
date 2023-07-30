def createTaskPlanner():
  # Tu código aquí 👇
  tasks = []

  def addTask(task):
    # Tu código aquí 👇
    task["completed"] = False
    tasks.append(task)

  def removeTask(value):
    # Tu código aquí 👇
    for task in tasks:
      if(task["id"] == value or task["name"] == value):
        tasks.remove(task)

  def getTasks():
    return tasks
  
  def getPendingTasks():
    # Tu código aquí 👇
    return [task for task in tasks if task["completed"] == False]
  
  def getCompletedTasks():
    # Tu código aquí 👇
    return [task for task in tasks if task["completed"] == True]
  
  def markTaskAsCompleted(value):
    # Tu código aquí 👇
    task_found = [task for task in tasks if task["id"] == value or task["name"] == value]
    task_found[0]["completed"] = True
  
  def getSortedTasksByPriority():
    # Tu código aquí 👇
    copy_tasks = [task for task in tasks]
    copy_tasks.sort(key=lambda e: e["priority"])
    return copy_tasks
  
  def filterTasksByTag(tag):
    # Tu código aquí 👇
    tasks_by_tag = lambda task: tag in task["tags"]
    return list(filter(tasks_by_tag, tasks))
  
  def updateTask(taskId, updates):
    # Tu código aquí 👇
    tasks_found = [task for task in tasks if task["id"] == taskId]
    task_found = tasks_found[0]
    for key, value in updates.items():
      task_found[key] = value
  
  return {
    'addTask': addTask,
    'removeTask': removeTask,
    'getTasks': getTasks,
    'getPendingTasks': getPendingTasks,
    'getCompletedTasks': getCompletedTasks,
    'markTaskAsCompleted': markTaskAsCompleted,
    'getSortedTasksByPriority': getSortedTasksByPriority,
    'filterTasksByTag': filterTasksByTag,
    'updateTask': updateTask
  }

## ---------------------------- Example 1

"""planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

planner['markTaskAsCompleted']('Llamar a Juan')

print(planner['getCompletedTasks']())"""

"""
Output:

[{
  'id': 2,
  'name': 'Llamar a Juan',
  'completed': True,
  'priority': 3,
  'tags': ['personal']
}]
"""

# --------------------------------- Example 2
"""
planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

print(planner['filterTasksByTag']('shopping'))

Output:

[{
    'id': 1,
    'name': 'Comprar leche',
    'completed': False,
    'priority': 1,
    'tags': ['shopping', 'home']
}]
"""