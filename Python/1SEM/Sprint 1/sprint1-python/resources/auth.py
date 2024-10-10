from utils.cls import cls

# Simulação de banco de dados
user_list = [{"username": "U", "password": "S"}]

class Session:
    def __init__(self, name, active):
        self.name = name
        self.active = active

# Simulação do banco de dados para secao
session = Session(None, False)

def login():
    username = input('Digite o usuário: ')
    password = input('Digite o senha: ')

    matching_users = []

    for x in user_list:
        if x["username"] == username and x["password"] == password:
            matching_users.append(x)

    if not len(matching_users):
        cls()
        print('Usuário ou senha incorretos.')
        return False

    global session
    session.name = username
    session.active = True
    return True

def logout():
    global session
    session.name = None
    session.active = False