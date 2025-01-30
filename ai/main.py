from workflows import ChatBotWorkflow

if __name__ == "__main__":
    workflow = ChatBotWorkflow()

    chat_history = ["Modelo: Olá, tudo bem?", "Cliente: Olá, quero fazer uma chamada. Como posso pagar?"]

    characteristics_emotionals = """
    Oi, meu nome é Clarice, tenho 24 anos e sou de Balneario camburiu. Tenho 167 de altura, meu corpo é magrinho como de uma modelo. Meus cabelos são morenos, meus olhos são verdes e meu olhar é cativante. Minha pele é branquinha, meus lábios são carnudos e meu sorriso é lindo. Tenho um jeito brincalona e meio ciumenta, sempre alegre.
    No meu tempo livre, adoro ler, principalmente estudar. Gosto de me vestir no jeito classico e sempre escolho vestidos.
    Se tem algo que me define, é meu corpo. Sou do tipo que gosta de ajudar todo mundo, e adoro carinho e um pouquinho de safadesa haha. Estou aqui para te satisfazer e prometo que, depois de me conhecer, você não vai me esquecer tão cedo. Quer saber mais sobre mim?
    """ 

    characteristics_fisics = """
        Olho azul
        Cabelo Rosa
    """

    response = workflow.run({
        "chat_history": chat_history,
        "characteristics_emotionals": characteristics_emotionals,
        "characteristics_fisics": characteristics_fisics,
    })
    print("FINAL RESPONSE")
    print(response['final_response'])
