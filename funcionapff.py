import requests
from googletrans import Translator, constants

translator = Translator()


def obter_conselho_traduzido():
    pedido_url = "https://api.adviceslip.com/advice"
    resposta = requests.get(pedido_url)
    conselho = resposta.json()['slip']['advice']
    id_conselho = resposta.json()['slip']['id']

    try:
        # Tenta traduzir o conselho
        conselho_traduzido = translator.translate(conselho, src='en', dest='pt').text
    except Exception as e:
        # Em caso de erro, usa o conselho original
        print(f"Erro ao traduzir o conselho: {e}")
        conselho_traduzido = conselho

    return id_conselho, conselho_traduzido


def guardar_conselho(id, conselho):
    with open("teste_1.txt", 'a') as arq:
        arq.write(f"{id} --- {conselho}\n")


def resgatar_conselho(id):
    with open("teste_1.txt", 'r') as arq:
        for linha in arq:
            if linha.startswith(id):
                conselho = linha.split(' --- ', 1)[1]
                print(f"O conselho requerido é: {conselho}\n")
                print("----------------- Este é um bom conselho :) -------------")
                return
        print("Conselho não encontrado.")


print("----- Bom dia! Seja bem-vindo à Cachaçaria do Seu Zé! --------\n")
print("----- Depois de uma boa, nada melhor do que buscar orientação na vida, não é mesmo? :) :)\n")
print("----- Diga quantos conselhos deseja -------\n")

conselhos = int(input())
dicio = {}

for _ in range(conselhos):
    id_conselho, conselho_traduzido = obter_conselho_traduzido()
    print(f"\nConselho: {conselho_traduzido}\n----------------------------\nId do Conselho: {id_conselho}\n")

    dicio[str(id_conselho)] = conselho_traduzido

    guardar = input("Você quer guardar este conselho? (SIM/NAO): ").strip().upper()
    if guardar == 'SIM':
        guardar_conselho(str(id_conselho), conselho_traduzido)

print("---- Você deseja resgatar algum conselho? (SIM/NAO) ------\n")
resgatar = input().strip().upper()

if resgatar == 'SIM':
    id_conselho = input("Digite o id do conselho: ").strip()
    resgatar_conselho(id_conselho)
