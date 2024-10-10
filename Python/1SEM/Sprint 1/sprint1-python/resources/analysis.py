from utils.cls import cls
from decorators.auth import verify_session

# Dados Teste
analysis = [{"failures": [{"id": "falha_teste","confidence": 0.3}], "id": 1, "recording":"file1.mp4"},
            {"failures": [{"id": "falha_teste", "confidence": 0.8}], "id": 2, "recording":"file2.mp4"}]

@verify_session
def analysis_menu():
    print(f"\n----------------- Análises -----------------\n"
          f"1. Ver todas as análises\n"
          f"2. Procurar análise por ID\n"
          "3. Voltar\n"
          "---------------------------------------------")
    control = int(input('Digite a opção desejada: '))

    match control:
        case 1:
            show_analysis()
        case 2:
            show_analysis_by_id()
        case 3:
            return
        case _:
            cls()
            print('Opção Inválida')

    analysis_menu()

@verify_session
def show_analysis():
    print(analysis)
    input('Pressione ENTER para retornar')

@verify_session
def show_analysis_by_id():
    control = int(input('Digite o ID da analise: '))
    found_analysis = []

    for x in analysis:
        if x["id"] == control:
            found_analysis.append(x)

    if not len(found_analysis):
        print("Analise nao encontrada")
        return None
    print(found_analysis)
    input('Pressione ENTER para retornar')
