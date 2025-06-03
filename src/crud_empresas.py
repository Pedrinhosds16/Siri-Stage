# Pedro Vinicius e Sérgio Gonçalves - CRUD de Empresas

import json # Importa o módulo JSON para manipulação de arquivos JSON
import os # Importa o módulo OS para interações com o sistema operacional

CAMINHO = "data/empresas.json" 

def carregar_empresas(): # Carrega as empresas do arquivo JSON
    if not os.path.exists(CAMINHO): # Verifica se o arquivo existe
        return [] # Se não existir, retorna uma lista vazia
    with open(CAMINHO, "r") as arquivo: # Abre o arquivo em modo leitura
        return json.load(arquivo) # Carrega o conteúdo do arquivo JSON e retorna como uma lista de dicionários

def salvar_empresas(empresas): # Salva a lista de empresas no arquivo JSON
    with open(CAMINHO, "w") as arquivo: # Abre o arquivo em modo escrita
        json.dump(empresas, arquivo, indent=4) # Converte a lista de empresas em JSON e escreve no arquivo com indentação de 4 espaços

def adicionar_empresa(empresa): # Adiciona uma nova empresa à lista de empresas
    empresas = carregar_empresas() # Carrega as empresas existentes
    empresas.append(empresa) # Adiciona a nova empresa à lista
    salvar_empresas(empresas) # Salva a lista atualizada de empresas no arquivo JSON

def listar_empresas(): # Lista todas as empresas cadastradas
    return carregar_empresas() # Retorna a lista de empresas carregadas do arquivo JSON

def obter_empresa_por_indice(indice): # Obtém uma empresa específica pelo índice
    empresas = carregar_empresas() # Carrega as empresas existentes
    if 0 <= indice < len(empresas): # Verifica se o índice está dentro do intervalo válido
        return empresas[indice] # Retorna a empresa correspondente ao índice
    return None

def atualizar_empresa(indice, empresa_atualizada): # Atualiza uma empresa existente pelo índice
    empresas = carregar_empresas() # Carrega as empresas existentes
    if 0 <= indice < len(empresas): # Verifica se o índice está dentro do intervalo válido
        empresas[indice] = empresa_atualizada # Atualiza a empresa no índice especificado
        salvar_empresas(empresas) # Salva as alterações
        return True
    return False

def remover_empresa(indice): # Remove uma empresa existente pelo índice
    empresas = carregar_empresas() # Carrega as empresas existentes
    if 0 <= indice < len(empresas): # Verifica se o índice está dentro do intervalo válido
        empresas.pop(indice) # Remove a empresa do índice especificado
        salvar_empresas(empresas) # Salva as alterações
        return True
    return False

def obter_empresa_mais_recente(): # Obtém a última empresa cadastrada
    empresas = carregar_empresas() # Carrega as empresas existentes
    if empresas: # Verifica se há empresas cadastradas
        return empresas[-1] # Retorna a última empresa da lista
    return None

def editar_empresa(novos_dados):
    empresas = carregar_empresas() # Carrega as empresas
    if empresas: # Verifica se há empresas cadastradas
        empresas[-1] = novos_dados # Atualiza a última empresa cadastrada
        salvar_empresas(empresas) # Salva as alterações
        return True
    return False