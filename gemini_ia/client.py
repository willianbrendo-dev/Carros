from google import genai


def get_car_ai_bio(model, brand, year):

    client = genai.Client(api_key="AIzaSyC_zgAe4XXFKS-9MCuMhK9rYMMnJrxmXSE")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Crie uma descrição de venda para o carro {brand} {model} {year} com até 250 caracteres. Destaque características técnicas e benefícios desse modelo.")
    
    return response.text

