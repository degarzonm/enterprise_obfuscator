from obfuscation import obfuscate_text, deobfuscate_text, extract_dictionary
from ai import generate_answer

# Example usage
if __name__ == "__main__":
    # Sample text
    text = """
    El cliente Juan Pérez reportó un error al realizar una transacción desde la cuenta 1234567890.
    Al intentar transferir $5,000 a la cuenta de María García (número de cuenta 0987654321), el sistema arrojó una excepción NullPointerException en el método processTransaction() de la clase TransactionService.java.
    Según los registros en la base de datos, la transacción con ID TXN-20231015-0001 no se completó y los fondos permanecen retenidos.
    Se requiere una revisión del registro de transacciones en la tabla transactions de la base de datos finance_db para identificar la causa raíz del problema.
    """

    # Sample dictionary
    obfuscation_dict = {
        "Nombre_1": "Juan Pérez",
        "Nombre_2": "María García",
        "cuenta_1": "1234567890",
        "cuenta_2": "0987654321",
        "transaccion_1": "TXN-20231015-0001",
        "saldo_1": "$5,000",
        "fecha_1": "15/10/2023",
        "base_datos_1": "finance_db",
        "tabla_1": "transactions",
        "clase_1": "TransactionService.java",
        "metodo_1": "processTransaction()",
        "excepcion_1": "NullPointerException"
    }

    # Obfuscate the text
    obfuscated = obfuscate_text(text, obfuscation_dict)
    print("Texto Ofuscado:\n", obfuscated)

    # Deobfuscate the text
    original = deobfuscate_text(obfuscated, obfuscation_dict)
    print("\nTexto Original:\n", original)
    
    
    ## Example extracting dict from text
    dictionary_text = """
    {
        "Nombre_1": "Juan Pérez",
        "Nombre_2": "María García",
        "cuenta_1": "1234567890",
        "cuenta_2": "0987654321",
        "transaccion_1": "TXN-20231015-0001",
        "monto_1": "$5,000"
    }
    """
    
    # Extract the dictionary from the text
    obfuscation_dict_extracted = extract_dictionary(dictionary_text)
    print("Extracted Dictionary:")
    print(obfuscation_dict_extracted)
    # Obfuscate the text
    obfuscated = obfuscate_text(text, obfuscation_dict_extracted)
    print("Texto Ofuscado:\n", obfuscated)

    # Deobfuscate the text
    original = deobfuscate_text(obfuscated, obfuscation_dict_extracted)
    print("\nTexto Original:\n", original)
    
    ## probando llm
    print("TEST LLM:::::::::::::\nObteniendo diccionario por llm\n")
    #text_dict_from_llm = generate_answer(text)
    text_dict_from_llm = generate_answer('hola como estás? soy danny y tu como estás?')
    print("Diccionario de Ofuscación dado por LLM:\n",text_dict_from_llm)
    # Extract the dictionary from the text
    obj_dict_from_llm = extract_dictionary(text_dict_from_llm)
    print("Extracted Dictionary:")
    print(obj_dict_from_llm)
    # Obfuscate the text
    obfuscated = obfuscate_text(text, obj_dict_from_llm)
    print("Texto Ofuscado LLM:\n", obfuscated)
    # Deobfuscate the text
    original = deobfuscate_text(obfuscated, obfuscation_dict_extracted)
    print("\nTexto Original LLM:\n", original)

    ##########################################################################################
    ## New test block: Load text from 'example_sensitive_text.txt' and obfuscate using LLM ###
    ##########################################################################################
    
    ##print("\nNew Test Block: Obfuscate text from 'example_sensitive_text.txt' using LLM\n")
    # Load the text from 'example_sensitive_text.txt'
    #try:
    #    with open('example_sensitive_text.txt', 'r', encoding='utf-8') as file:
    #        sensitive_text = file.read()
    #except FileNotFoundError:
    #    print("Error: 'example_sensitive_text.txt' not found.")
    #    sensitive_text = ""
#
    #if sensitive_text:
    #    # Generate the obfuscation dictionary using the LLM
    #    generated_dictionary_text = generate_answer(sensitive_text)
    #    print("Generated Obfuscation Dictionary:\n", generated_dictionary_text)
    #    
    #    # Extract the dictionary from the LLM's response
    #    generated_obfuscation_dict = extract_dictionary(generated_dictionary_text)
    #    print("\nExtracted Obfuscation Dictionary:")
    #    print(generated_obfuscation_dict)
    #    
    #    # Obfuscate the sensitive text
    #    obfuscated_text = obfuscate_text(sensitive_text, generated_obfuscation_dict)
    #    #print("\nObfuscated Text:\n", obfuscated_text)
    #    
    #    # Deobfuscate the text
    #    deobfuscated_text = deobfuscate_text(obfuscated_text, generated_obfuscation_dict)
    #    #print("\nDeobfuscated Text:\n", deobfuscated_text)
    #else:
    #    print("No text to process.")