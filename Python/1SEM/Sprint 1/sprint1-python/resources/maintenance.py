import utils.cls
from decorators.auth import verify_session
from resources.alert import send_alert

# Dados Teste
work_orders = [{"location": "km75", "id": 1},{"location": "km76", "id": 2}]
pending_occurrences = [{"failure_type": "ferrugem", "location": "km35", "id": 1},{"failure_type": "trinco","location": "km31", "id": 2}]

@verify_session
def maintenance_menu():
    print(f"\n----------------- Análises -----------------\n"
          f"1. Ver manutenções programadas\n"
          f"2. Ver ocorrências pendentes\n"
          f"3. Marcar manutenção\n"
          "4. Voltar\n"
          "---------------------------------------------")
    control = int(input('Digite a opção desejada: '))

    match control:
        case 1:
            show_work_orders()
        case 2:
            show_pending_occurrences()
        case 3:
            schedule_work_order()
        case 4:
            return
        case _:
            utils.cls.cls()
            print('Opção Inválida')

    maintenance_menu()

@verify_session
def show_work_orders():
    print(work_orders)

@verify_session
def show_pending_occurrences():
    print(pending_occurrences)

@verify_session
def schedule_work_order():
    control = int(input('Digite o ID da ocorrência: '))
    found_occurrence= []

    for x in pending_occurrences:
        if x["id"] == control:
            found_occurrence.append(x)

    if not len(found_occurrence):
        print("Ocorrencia nao encontrada")
        return None

    new_work_order = {"location": found_occurrence[0]["location"], "id": len(work_orders) + 1}
    work_orders.append(new_work_order)
    send_alert("NOVA ORDEM DE MANUTENCAO: " + new_work_order.__str__())
    pending_occurrences.remove(found_occurrence[0])