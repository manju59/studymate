# backend/watsonx_client.py

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watsonx import GenerativeServiceV1
from .config import Settings

class WatsonXClient:
    def __init__(self):
        auth = IAMAuthenticator(Settings.MISTRAL_API_KEY)
        self.client = GenerativeServiceV1(
            version="2023-10-01",
            authenticator=auth
        )
        self.client.set_service_url(Settings.MISTRAL_API_URL)

    def generate_answer(self, query: str, context: list[str]) -> str:
        prompt = (
            "You are an academic assistant. Use the context below:\n\n"
            + "\n---\n".join(context)
            + f"\n\nQuestion: {query}\nAnswer concisely, citing context."
        )
        try:
            resp = self.client.create_completion(
                model="mixtral-8x7b-instruct",
                prompt=prompt,
                max_tokens=300,
                temperature=0.2
            ).get_result()
            # Adjust key access if SDK version differs
            return resp["choices"][0]["text"].strip()
        except Exception as e:
            return f"Error generating answer: {e}"