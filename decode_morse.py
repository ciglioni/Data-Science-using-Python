'''
Complementar o projeto para que ele seja capaz de ler frases / textos sendo:
As letras devem ser separadas por um espaço
As palavras devem ser separadas por dois espaços
Executar com pelo menos 3 cenários diferentes, ou seja, 3 textos
Você deve criar estes textos /frases de input
'''

import os
import datetime
import pandas as pd
from config import dict_morse, file_path

#from dotenv import load_dotenv
#load_dotenv()
#file_path = os.getenv("file_path")

#msg = '-.-. .- .-. --- .-.. .. -. .-'

msg = input("Digite seu codigo morse: ")

def decode_morse(msg):
    '''
    input: mensagem em codigo morse com as letras separadas por espacos
    output: palavra escrita em letras e algarismos
    '''
    # msg_lst = msg.split(" ")
    # msg_claro = []
    # for letter in msg_lst:
    #     msg_claro.append(dict_morse[letter])
    # return "".join(msg_claro)

    # Divide a mensagem em palavras usando dois espaços como delimitador
    palavras = msg.split("  ")
    
    # Inicializa uma lista para armazenar as palavras decodificadas
    frase_clara = []

    for palavra in palavras:
        # Divide a palavra em letras usando um único espaço como delimitador
        letras = palavra.split(" ")
        # Decodifica cada letra usando o dicionário morse
        try:
            palavra_clara = ''.join(dict_morse[letra] for letra in letras if letra)
        except KeyError as e:
            print(f"Chave não encontrada para o código Morse: {e}")
            palavra_clara = ''  # Ou algum valor padrão
        # Adiciona a palavra decodificada à lista de palavras
        frase_clara.append(palavra_clara)

    # Junta todas as palavras para formar a frase final
    return ' '.join(frase_clara)

def save_clear_msg_csv_hdr(msg):
    '''
    input: mensagem em codigo morse com as letras separadas por espacos
    output: palavra escrita em letras e algarismos
    '''
    now = datetime.datetime.now()
    frase_clara = decode_morse(msg)
    df = pd.DataFrame([[frase_clara, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode ="a", index = False, header=hdr)

if __name__ == "__main__":
    save_clear_msg_csv_hdr(msg)
    #print(save_clear_msg_csv_hdr)
    #print(pd.to_pickle.__doc__)