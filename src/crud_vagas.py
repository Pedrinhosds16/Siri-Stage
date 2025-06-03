# Paulo Marrocos e Cauã dos Santos - CRUD de Vagas

import json
import os
import uuid

CAMINHO = "data/vagas.json"

def carregar_vagas(): # Carrega as vagas do arquivo JSON
    if not os.path.exists(CAMINHO): # Verifica se o arquivo existe
        return [] # Se não existir, retorna uma lista vazia
    with open(CAMINHO, "r") as arquivo: # Abre o arquivo em modo leitura
        return json.load(arquivo) # Carrega o conteúdo do arquivo JSON e retorna como uma lista de dicionários

def salvar_vagas(vagas): # Salva a lista de vagas no arquivo JSON
    with open(CAMINHO, "w") as arquivo: # Abre o arquivo em modo escrita
        json.dump(vagas, arquivo, indent=4) # Converte a lista de vagas em JSON e escreve no arquivo com indentação de 4 espaços

def adicionar_vaga(vaga): # Adiciona uma nova vaga à lista de vagas
    vagas = carregar_vagas() # Carrega as vagas existentes
    vaga["id"] = str(uuid.uuid4())  # Gera um ID único para a vaga
    vagas.append(vaga) # Adiciona a nova vaga à lista
    salvar_vagas(vagas) # Salva a lista atualizada de vagas no arquivo JSON

def listar_vagas(): # Lista todas as vagas cadastradas
    return carregar_vagas() # Retorna a lista de vagas carregadas do arquivo JSON

def remover_vaga(vaga_id): # Remove uma vaga específica pelo ID
    vagas = carregar_vagas() # Carrega as vagas existentes
    vagas_filtradas = [vaga for vaga in vagas if str(vaga.get("id")) != str(vaga_id)] # Filtra as vagas que não têm o ID fornecido

    if len(vagas) == len(vagas_filtradas): # Verifica se alguma vaga foi removida
        return False
    
    salvar_vagas(vagas_filtradas) # Salva as vagas filtradas no arquivo JSON
    return True

def editar_vaga(vaga_id, novos_dados): # Edita os dados de uma vaga específica pelo ID
    vagas = carregar_vagas() # Carrega as vagas existentes
    vaga_encontrada = False # Variável para verificar se a vaga foi encontrada

    for vaga in vagas: # Itera sobre as vagas para encontrar a vaga com o ID fornecido
        if vaga["id"] == vaga_id: # Verifica se o ID da vaga corresponde ao ID fornecido
            vaga_encontrada = True # Marca que a vaga foi encontrada
            vaga.update(novos_dados) # Atualiza os dados da vaga com os novos dados fornecidos
            break
    
    if vaga_encontrada: # Se a vaga foi encontrada, salva as alterações
        salvar_vagas(vagas)
        return True
    else:
        return False