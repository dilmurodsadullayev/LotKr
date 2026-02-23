import re

def is_valid_text(text: str, lang: str) -> bool:
    text = text.strip()
    if not text:
        return False

    lang = lang.lower()

    if lang == "kril":
        pattern = r"^[a-zA-Z‘’'\".,!? \-]+$"
    elif lang == "lotin":
        pattern = r"^[а-яА-Яўғҳиёшчнг‘’'\".,!? \-]+$"
    else:
        return False

    return bool(re.match(pattern, text))