def filter_user_messages(messages, user):
  # Tu código aquí 👈
  mensajes_user = lambda message: message['sender'] == user
  return list(filter(mensajes_user, messages))

messages = [
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
]

user = 'Alice'
filter_user_messages(messages, user)