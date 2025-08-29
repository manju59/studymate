from ibm_watsonx_ai.client import APIClient
from ibm_watsonx_ai.foundation_models import Model

class WatsonXClient:
    def __init__(self, api_key, api_url):
        self.credentials = {
            "url": api_url,
            "apikey": api_key,
            "version": "5.0"  # Added this line to fix the WMLClientError
        }
        self.client = APIClient(self.credentials)

    def generate_answer(self, query, top_chunks):
        # Configure the model and its parameters
        model_id = 'google/flan-t5-xl' # or 'google/flan-ul2' or other models
        project_id = "YOUR_PROJECT_ID" # <-- Replace with your IBM Cloud Project ID
        
        # A simple prompt template for Q&A
        prompt = f"""
        Given the following context from a document, answer the question.
        
        Context:
        {top_chunks}
        
        Question:
        {query}
        
        Answer:
        """

        # Model parameters
        parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 500,
            "min_new_tokens": 50,
        }

        # Instantiate the Model
        model = Model(
            model_id=model_id,
            params=parameters,
            credentials=self.credentials,
            project_id=project_id
        )

        # Generate the text
        response = model.generate_text(prompt)
        return response
