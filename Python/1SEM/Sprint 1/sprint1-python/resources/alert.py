from decorators.auth import verify_session

@verify_session
def send_alert(string):
    print(f"\n----------------- ALERTA -----------------\n"
          + string +
          f"\n----------------- ALERTA -----------------\n")
