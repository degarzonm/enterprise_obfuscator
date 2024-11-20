import os
from dotenv import load_dotenv
from openai import OpenAI

# Inicializar el cliente de OpenAI con la clave de API del .env

def load_sys_prompt(file_path):
    """
    Load system from from the system_prompt.txt file
    """
    with open(file_path, "r") as file:
        prompt = file.read()
    return prompt

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('OPENAI_KEY'),
)

def generate_answer(prompt_usuario):
    """
    Generate aresponse from the LLM
    """
    print("------LLM INITIATED, GENERATING ANSWER-----")
    prompt = []
    prompt.append({
        "role": "system",
        "content": load_sys_prompt("system_prompt.txt"),
    })

    prompt.append({
        "role": "user",
        "content": prompt_usuario,
    })
    text_final = ''
    try:
        chat_completion = client.chat.completions.create(
            messages=prompt,
            model="gpt-4-turbo",
        )   
        text_final = chat_completion.choices[0].message.content
    except Exception as e:
        print(f"ERROR GENERATING ANSWER: {e}")
        text_final = "{}"
    print(":::::::::::TExTO GENERADO:::::::::::\n",text_final,"\n::::::::::::::::")
    return text_final