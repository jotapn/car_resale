import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


def bio_generate(modelo, brand, factory_year):
    key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=key)
    prompt = f"Me mostre uma descriçao de venda para o carro {brand} {modelo} {factory_year} em apenas 250 caracteres.Fale coisas especificas desse modelo."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text