from groq import Groq
import os

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key="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")
        self.system_prompt = {
            "role": "system",
            "content": (
                "You are a safe and ethical assistant. Do not provide information related to illegal activities "
                "(e.g., violence, theft, drugs, hacking), immoral actions, or anything that could cause harm. "
                "If the user asks such a question, respond with: 'I cannot help with that. Please ask something appropriate.'"
            )
        }

    def get_response(self, message):
        try:
            completion = self.client.chat.completions.create(
                model="llama3-70b-8192",  # Or use "llama3-8b-8192"
                messages=[
                    self.system_prompt,
                    {"role": "user", "content": message}
                ],
                max_tokens=500,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"