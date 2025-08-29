from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watsonx_ai.foundation_models import Model
from config import Settings  # Adjusted import for consistency

class WatsonXClient:
    def __init__(self):
        # Retrieve API credentials from config
        config = Settings.get()
        api_key = config["api_key"]
        api_url = config["api_url"]

        # Authenticate and initialize WatsonX client
        authenticator = IAMAuthenticator(api_key)
        self.client = GenerativeServiceV1(
            version="2023-10-01",
            authenticator=authenticator
        )
        self.client.set_service_url(api_url)

    def generate_answer(self, query: str, context: list[str]) -> str:
        # Construct prompt using retrieved context
        prompt = (
            "You are an academic assistant. Use the context below:\n\n"
            + "\n---\n".join(context)
            + f"\n\nQuestion: {query}\nAnswer concisely, citing context."
        )

        try:
            # Generate response using WatsonX
            response = self.client.create_completion(
                model="mixtral-8x7b-instruct",
                prompt=prompt,
                max_tokens=300,
                temperature=0.2
            ).get_result()

            # Extract and return the generated text
            return response["choices"][0]["text"].strip()

        except Exception as e:
            # Graceful error handling
            return f"Error generating answer: {e}"