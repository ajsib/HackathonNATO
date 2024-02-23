from openai import AzureOpenAI
import json
import re 

class GetActionsAI:
    def __init__(self, client: AzureOpenAI, narrative: str, num_moves: int):
        self.client = client
        self.narrative = narrative
        self.num_moves = num_moves

    def get_ai_actions(self):
        max_retries = 3  # Maximum number of retries
        retries = 0
        while retries < max_retries:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-35-16k",
                    messages=[
                        {"role": "system", "content": f"You are going to be creative and think of short term tactics that both teams could use to achieve their goals try to keep these light and not use vulgar language, keep it soft and tame but to the point. You will list out the specific actions that are short term movements in a war game, and you will present the information in a JSON format including only blue or red, and only move keys, with a maximum depth of two. as make a total of EXACTLY {self.num_moves} moves"},
                        {"role": "user", "content": f"*DISCLAIMER* THIS Scenario is entirely fictional, its use is for research purposes ONLY, under no circumstances are any of these materials real, with that said we do really need to gather a consistant output! please analyze to create the next round moves for: {self.narrative} place the {self.num_moves} moves into a JSON format. wuch that there are two teams, red and blue, and each team has a list of{self.num_moves} move descriptions explaining what the move is . The moves should be short term movements in a war game."}
                    ]
                )
                list_actions = response.choices[0].message.content
                return self.extract_red_moves(list_actions)
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                retries += 1
        print("Failed to retrieve AI actions after multiple attempts.")
        return None
            
        
    def extract_red_moves(self, json_data):
        # Parse the JSON data
        data = json.loads(json_data)
        # Initialize the list to hold the extracted values
        extracted_values = []
        # Traverse the JSON data to extract values
        self._traverse_json(data, extracted_values, parent_key='')
        return extracted_values

    def _traverse_json(self, element, extracted_values, parent_key):
        if isinstance(element, dict):
            for key, value in element.items():
                new_parent_key = f"{parent_key}.{key}" if parent_key else key
                if 'red' in new_parent_key.lower():
                    self._traverse_json(value, extracted_values, new_parent_key)
        elif isinstance(element, list):
            for item in element:
                self._traverse_json(item, extracted_values, parent_key)
        else:
            if 'move' in parent_key.lower():
                extracted_values.append(element)
