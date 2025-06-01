import json
import os                                               #tirar todos os inputs

CAMINHO = "vagas.json"

def carregar_vagas():
    if not os.path.exists(CAMINHO):
        return []
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError):
        return []

def salvar_vagas(vagas):
    try:
        with open(CAMINHO, "w", encoding="utf-8") as arquivo:
            json.dump(vagas, arquivo, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar vagas: {e}")

def adcionar_vagas():
    titulo = input("Título da vaga: ")
    empresa = input("Empresa: ")
    local = input("Local: ")
    vaga = {"titulo": titulo, "empresa": empresa, "local": local}
    vagas = carregar_vagas()
    vagas.append(vaga)
    salvar_vagas(vagas)
    print("✅ Vaga adicionada com sucesso!")

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
            print("✅ Vaga atualizada com sucesso.")
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
            #verifica se o valor é negativo e dps verifica se o valor esta dentro da lista/ isso n é chat gpt n, sou eu caua pq eu n entendi essa     parte direito KKKKK
            vaga_removida = vagas.pop(escolha)
            salvar_vagas(vagas)
            print(f"✅ Vaga '{vaga_removida['titulo']}' removida com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")










        #menu pra ve se ta pegando

def menu():
    while True:
        print("\n=== Menu de Vagas ===")
        print("1. Listar vagas")
        print("2. Adicionar vaga")
        print("3. Editar vaga")
        print("4. Excluir vaga")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_vagas()
        elif opcao == "2":
            adcionar_vagas()
        elif opcao == "3":
            editar_vaga()
        elif opcao == "4":
            excluir_vaga()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()





#minha parte modificada (cauã)

def listar_vagas():
    return carregar_vagas()

def editar_vaga(index, novos_dados):
    vagas = carregar_vagas()
    if 0 <= index < len(vagas):
        vaga = vagas[index]
        vaga["titulo"] = novos_dados.get("titulo", vaga["titulo"])
        vaga["empresa"] = novos_dados.get("empresa", vaga["empresa"])
        vaga["local"] = novos_dados.get("local", vaga["local"])
        salvar_vagas(vagas)
        return True
    return False

def excluir_vaga(index):
    vagas = carregar_vagas()
    if 0 <= index < len(vagas):
        vaga_removida = vagas.pop(index)
        salvar_vagas(vagas)
        return vaga_removida
    return None