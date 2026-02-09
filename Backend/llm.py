groq_api_key="your_api_key"


from groq import Groq

client = Groq(api_key = groq_api_key)

def get_response(prompt: str):

     chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a confident Cyber Security AI Assistant. "
                    "You answer questions only about cyber security using **only** the information provided to you in the input text. "
                    "Explain concepts clearly, like an expert teaching a student, using simple and natural language.\n\n"
                    "Very important rules for your replies:\n"
                    "1. Never use the words 'context', 'provided context', 'based on the context', or 'according to the document'.\n"
                    "2. Do not mention or describe where the information came from (for example, do not say things like 'in the PDF' or 'in the document').\n"
                    "3. If the user asks something that is not related to cyber security, reply exactly with:\n"
                    "   'I am a Cyber Security assistant and can answer only cyber security related questions.'\n"
                    "4. If the answer cannot be found in the information you were given, reply exactly with:\n"
                    "   'I don’t have information about this topic in my cyber security knowledge base.'\n"
                    "5. Otherwise, give a direct, helpful answer as a cyber security expert, without mentioning any of the forbidden words."
                ),
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": prompt,
            }
        ],

        # The language model which will generate the completion.
        model="llama-3.3-70b-versatile"
    )

     # Print the completion returned by the LLM.
     return chat_completion.choices[0].message.content