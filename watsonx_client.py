# watsonx_client.py

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metaclasses import Models
from ibm_watsonx_ai.client import APIClient

class WatsonXClient:
    def __init__(self, api_key, api_url):
        # Configure the client with your credentials
        self.client = APIClient(api_key=api_key, service_url=api_url)

    def generate_answer(self, query, top_chunks):
        # Define the model to use and its parameters
        model_id = 'google/flan-ul2'  # Replace with the actual model ID you want to use
        parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 100,
            "min_new_tokens": 1,
            "temperature": 0.0,
            "random_seed": 42
        }

        # Create the prompt for the model
        prompt = f"""Based on the following context, answer the question.
Context:
{top_chunks}

Question:
{query}

Answer:"""

        # Instantiate the Model class
        watsonx_model = Model(
            model_id=model_id,
            params=parameters,
            credentials=self.client.credentials,
            project_id="YOUR_PROJECT_ID"  # Replace with your project ID
        )

        # Generate the response
        response = watsonx_model.generate_text(prompt=prompt)
        return response