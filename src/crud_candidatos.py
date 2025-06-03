# Luiz Henrique e Pedro Marrocos - CRUD de Candidatos

import json
import os

CAMINHO = "data/candidatos.json"

def carregar_candidatos(): # Carrega os candidatos do arquivo JSON
    if not os.path.exists(CAMINHO): # Verifica se o arquivo existe
        return [] # Se não existir, retorna uma lista vazia
    with open(CAMINHO, "r") as arquivo: # Abre o arquivo em modo leitura
        return json.load(arquivo) # Carrega o conteúdo do arquivo JSON e retorna como uma lista de dicionários

def salvar_candidatos(candidatos): # Salva a lista de candidatos no arquivo JSON
    with open(CAMINHO, "w") as arquivo: # Abre o arquivo em modo escrita
        json.dump(candidatos, arquivo, indent=4) # Converte a lista de candidatos em JSON e escreve no arquivo com indentação de 4 espaços

def adicionar_candidato(candidato): # Adiciona um novo candidato à lista de candidatos
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    candidatos.append(candidato) # Adiciona o novo candidato à lista
    salvar_candidatos(candidatos) # Salva a lista atualizada de candidatos no arquivo JSON

def listar_candidatos(): # Lista todos os candidatos cadastrados
    return carregar_candidatos() # Retorna a lista de candidatos carregados do arquivo JSON

def obter_candidato_por_indice(indice): # Obtém um candidato específico pelo índice
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    if 0 <= indice < len(candidatos): # Verifica se o índice está dentro do intervalo válido
        return candidatos[indice] # Retorna o candidato correspondente ao índice
    return None     

