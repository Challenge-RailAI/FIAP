from resources.auth import session

def verify_session(func):
    def wrapper(*args, **kwargs):
        if session.active:
            return func(*args, **kwargs)
        else:
            print("Acesso Negado: Por favor realize o login para acessar esta ferramenta.")
            return None
    return wrapper