import json
import re

def obfuscate_text(text, dictionary):
    # Sort keys by length of their values in descending order to replace longer matches first
    sorted_items = sorted(dictionary.items(), key=lambda x: len(x[1]), reverse=True)
    for key, value in sorted_items:
        pattern = re.escape(value)
        # Use word boundaries to match whole words
        text = re.sub(r'\b{}\b'.format(pattern), key, text)
    return text

def deobfuscate_text(obfuscated_text, dictionary):
    # Sort keys by length in descending order to replace longer matches first
    sorted_keys = sorted(dictionary.keys(), key=lambda x: len(x), reverse=True)
    for key in sorted_keys:
        pattern = re.escape(key)
        # Replace the placeholder with the original value
        obfuscated_text = re.sub(r'\b{}\b'.format(pattern), dictionary[key], obfuscated_text)
    return obfuscated_text

def extract_dictionary(text):
    """
    Extracts a JSON dictionary from the given text and returns it as a Python dictionary.

    Parameters:
    text (str): The text containing the JSON dictionary.

    Returns:
    dict: The parsed dictionary to be used for obfuscation.
    """
    # Use a regular expression to find the JSON object in the text
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        json_text = match.group(0)
        try:
            # Parse the JSON text into a Python dictionary
            obfuscation_dict = json.loads(json_text)
            return obfuscation_dict
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
            return {}
    else:
        print("No JSON dictionary found in the text.")
        return {}
