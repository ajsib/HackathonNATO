from openai import AzureOpenAI
import json

class TeamClassifier:
    def __init__(self, client: AzureOpenAI, scenario: str):
        self.client = client
        self.scenario = scenario
        self.teams = {}

    def classify_teams(self): 
        prompt = self.get_prompt()
        try:
            response = self.client.chat.completions.create(
                model="gpt-35-16k",
                temperature=0.2,
                messages=[
                    {
                        "role": "system", 
                        "content": """As an adjudicator coordinating a war-game scenario exercise, your task is to provide structured JSON data with the following key-value pairs for the exactly two teams involved in the exercise.: 
                                    {
                                        "name": "NAME",  
                                        "description": "DESCRIPTION",  
                                        "winConditions": "[LIST, OF, WIN, CONDITIONS]",  
                                        "lossConditions": "[LIST, OF, LOSS, CONDITIONS]"
                                    }
                                    Ensure that the provided JSON adheres strictly to this format."""
                    },
                    {"role": "user", "content": prompt}
                ]
            )
            self.teams = self.format_results(response)
            return self.teams
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return {}

    def get_prompt(self) -> str:
        #
        return f"""You are an adjudicator working to coordinate a war-game scenario exercise. 
                    Analyze the following scenario: {self.scenario}. Ensure you only have name, description, winConditions and lossConditions in key value pairs for the exactly two teams red and blue in JSON format."""

    def format_results(self, response):
        # since the response is in JSON format, we can just convert it to a dictionary, removing the top level key
        return json.loads(response.choices[0].message.content)