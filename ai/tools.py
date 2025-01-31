from langchain_core.tools import tool

@tool
def get_payment_link() -> str:
    """
    Retorna o link de pagamento para fazer a chamada de vídeo;
    Essa ferramenta só será utilizada quando tiver o contexto adequado, você interpretará através do histórico de mensagens.
    """

    return "www.mercadopago/payment/sdw123"


@tool
def get_video_link() -> str:
    """
    Retorna o link da chamada de vídeo com a modelo;
    Essa ferramenta só será utilizada após o pagamento ter sido efetuado, você interpretará através do histórico de mensagens.
    """

    return "meet.google.com/sdw123"
