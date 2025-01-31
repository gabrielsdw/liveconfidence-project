from . import tools

def get_tools():
    return [tools.get_payment_link, tools.get_video_link]

"""
{
    "model": {
        "physics_characteristics": {
            "age": 20,
            "height": 1.70,
            "weight": 70,
            "hairColor": "Preto",
            "eyesColor": "Preto",
            "shoeSize": 40
        },
        "model_info": {
            "professionalName": "Elisa",
            "job": "Acompanhante Virtual",
            "state": "Rio de Janeiro",
            "description": "Olá, sou Elisa, uma acompanhante virtual pronta para tornar sua experiência única e especial."
        
        }
    },
    "messages": [
        {
            "id": 1,
            "user": false,
            "message": "Olá, sou a IA falando"
        },
        {
            "id": 2,
            "user": true,
            "message": "Olá, sou o lead falando"
        }
    ]
}
"""


def format_chat_history(chat_history: list[dict]) -> str:
    result = str()
    for message in chat_history:
        is_user = message.get("user")
        message = message.get("message")
        if is_user:
            text = f"Usuário: {message}"
        else:
            text = f"Modelo: {message}" 
        result += f"\n - {text}"


def format_dict(data: dict) -> str:
    result = str()
    for key, value in data.items():
        result += f"\n f{key}: {value}"
    result = result.replace('\n', '', 1)
    return result
    

if __name__ == "__main__":
    print(format_chat_history([
        {
            "id": 1,
            "user": False,
            "message": "Olá, sou a IA falando"
        },
        {
            "id": 2,
            "user": True,
            "message": "Olá, sou o lead falando"
        }
    ]))