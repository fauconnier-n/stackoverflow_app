import re

def remove_code(text):
    """Retire les parties de code du post marquées par les bornes html <code>

    Args:
        text (string): text
    """
    re.sub('<code>(.*?)</code>', ' ', text, flags=re.MULTILINE|re.DOTALL)