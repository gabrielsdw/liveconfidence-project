from . import tools

def get_tools():
    return [tools.get_payment_link, tools.get_video_link]

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
    # result = result.replace('\n', '', 1)
    return result

def format_dict(data: dict) -> str:
    result = str()
    for key, value in data.items():
        result += f"\n {key}: {value}"
    result = result.replace('\n', '', 1)
    return result
