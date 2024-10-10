from resources.maintenance import maintenance_menu
from utils.cls import cls
from resources.auth import login, logout, session
from resources.analysis import analysis_menu




def mainmenu():
    print(f"\n----------------- RailAI v0.1 -----------------\n"
          f"1. {'Logout' if session.active else 'Login'}\n"
          f"2. Análises{' - Login Necessário' if not session.active else ''}\n"
          f"3. Manutenção {' - Login Necessário' if not session.active else ''}\n"
          "4. Sair\n"
          "---------------------------------------------")
    control = int(input('Digite a opção desejada: '))

    match control:
        case 1:
            if session.active:
                logout()
            else:
                login()
        case 2:
            analysis_menu()
        case 3:
            maintenance_menu()
        case 4:
            print('Encerrando...')
            quit()
        case _:
            cls()
            print('Opção Inválida')
    mainmenu()






mainmenu()






