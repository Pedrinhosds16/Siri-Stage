import json
import os

ARQUIVO_VAGAS = "vagas.json"


def carregar_vagas():
    if os.path.exists(ARQUIVO_VAGAS):
        with open(ARQUIVO_VAGAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_vagas(vagas):
    with open(ARQUIVO_VAGAS, "w", encoding="utf-8") as f:
        json.dump(vagas, f, indent=4, ensure_ascii=False)

def listar_vagas():
    vagas = carregar_vagas()
    if not vagas:
        print("Nenhuma vaga cadastrada.")
    else:
        print("=== Lista de Vagas ===")
        for i, vaga in enumerate(vagas, 1):
            print(f"{i}. {vaga['titulo']} - {vaga['empresa']} ({vaga['local']})")

def editar_vaga():
    vagas = carregar_vagas()
    listar_vagas()
    try:
        escolha = int(input("Digite o número da vaga que deseja editar: ")) - 1
        if 0 <= escolha < len(vagas):
            titulo = input("Novo título (deixe em branco para manter o atual): ")
            empresa = input("Nova empresa (deixe em branco para manter o atual): ")
            local = input("Novo local (deixe em branco para manter o atual): ")

            if titulo:
                vagas[escolha]["titulo"] = titulo
            if empresa:
                vagas[escolha]["empresa"] = empresa
            if local:
                vagas[escolha]["local"] = local

            salvar_vagas(vagas)
            print("Vaga atualizada com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def excluir_vaga():
    vagas = carregar_vagas()
    listar_vagas()
    try:
        escolha = int(input("Digite o número da vaga que deseja excluir: ")) - 1
        if 0 <= escolha < len(vagas):
            vaga_removida = vagas.pop(escolha)
            salvar_vagas(vagas)
            print(f"Vaga '{vaga_removida['titulo']}' removida com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n1. Listar vagas")
        print("2. Editar vaga")
        print("3. Excluir vaga")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_vagas()
        elif opcao == "2":
            editar_vaga()
        elif opcao == "3":
            excluir_vaga()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
