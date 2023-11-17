
import re

def respostas(ask):
    if ask == " crédito ?":
        print(f'não, faz o L')
    else:
        print('faz o L')

    # Dicionário de intenções para enviar o robô para um ponto
intent_dict = {
    r"\b(?:(?:[Cc]omo)|(?:posso atualizar meu cartão de crédito [?]))\s(.+)": "Atualizar_pagamento",
    r"\b(?:[Pp]reciso mudar a forma de pagamento, o que fazer [?])\s(.+)": "Atualizar_pagamento",
    r"\b(?:[Qq]uero atualizar minhas informações de pagamento)\s(.+)": "Atualizar_pagamento",
    r"\b(?:[Mm][ée]todo de pagamento desatualizado, como proceder para atualizar [?])\s(.+)": "Atualizar_pagamento",
    r"\b(?:[Oo]nde vejo o status do meu pedido [?])\s(.+)": "Acompanhar_pedido",
    r"\b(?:[Cc]omo faço para rastrear meu pedido [?])\s(.+)": "Acompanhar_pedido",  
    r"\b(?:[Qq]uero saber onde está meu pedido, como faço [?])\s(.+)": "Acompanhar_pedido",
    r"\b(?:[Ss]tatus de entrega, como consultar [?])\s(.+)": "Acompanhar_pedido",     
    r"([Tt]chau|[Aa]té logo|[Aa]té mais|[Aa]deus| [Ss]air)": "turn_off",  
}

# Dicionário de ações do robô
action_dict = {
    "Atualizar_pagamento": respostas,
    "Acompanhar_pedido": respostas,
}



def chatbot_prompt():
    while True:
        comando = input("Olá, como posso te mandar fazer o L hoje?: ").lower().strip()
        action = chatbot_action(comando)
        if action == "Atualizar_pagamento" | "Acompanhar_pedido":
            chat_responses(action, comando)
        else:
            chat_responses(action, None)

def chat_responses(intent, command):
    if intent:
        if intent == 'Atualizar_pagamento' | 'Acompanhar_pedido':
            for key, value in intent_dict.items():
                pattern = re.compile(key)
                groups = pattern.findall(command)
                if groups:
                    print(f'{action_dict[value](groups[0])} ', end = "")
                    return  # Sai da função após o movimento

        elif intent == 'turn_off':
            print('Até logo')
            exit()

    else:
        print('Desculpa ai, não entendi oq vc disse, faz o L')


def chatbot_action(command):
    for pattern, action in intent_dict.items():
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            return action
    return None


def main(args=None):

    chatbot_prompt()

if __name__ == '__main__':
    main()