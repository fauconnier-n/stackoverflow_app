import re

def remove_code(text):
    """Retire les parties de code du post marquées par les bornes html <code></code>

    Args:
        text (string): texte à 

    Returns:
        string: texte sans code
    """
    cleaned_text = re.sub('<code>(.*?)</code>', ' ', text, flags=re.MULTILINE|re.DOTALL)

    return cleaned_text