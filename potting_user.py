class User:
  def __init__(self, name, age):
    #Tu código aquí 👇
    self._name = name
    self._age = age
    self._friends = []
    self._messages = []

  @property
  def name(self):
    return self._name

  @property
  def age(self):
    return self._age

  @property
  def friends(self):
    return self._friends

  @property
  def messages(self):
    return self._messages

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @age.setter
  def age(self, new_age):
    self._age = new_age
  
  @friends.setter
  def friends(self, new_list):
    self._friends = new_list

  @messages.setter
  def messages(self, new_list):
    self._messages = new_list

  def addFriend(self, friend):
    self._friends.append(friend)

  def sendMessage(self, message, friend):
    self._messages.append(message)
    friend._messages.append(message)

  def showMessages(self):
    return self._messages


"""
Ejemplo 1:

Input:

usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario1.addFriend(usuario2)
usuario1.sendMessage("Hola Maria!", usuario2)

usuario1.showMessages()

Output:

["Hola Maria!"]

Ejemplo 2:

Input:

usuario1 = User("Juan", 20)
usuario1.name = "Pepito"
print(usuario1.name)

Output:

"Pepito"
"""