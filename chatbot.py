from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def ask_gemini(context, question):

    prompt = f"""
    Context:

    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text