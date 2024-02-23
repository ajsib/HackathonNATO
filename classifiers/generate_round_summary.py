from openai import AzureOpenAI
import json

class GenerateRoundSummary:
    def __init__(self, client: AzureOpenAI, player_decision_text: str, ai_actions: str, round_action_data: dict, narrative: str):
        self.client = client
        self.player_decision_text = player_decision_text
        self.ai_actions = ai_actions
        self.round_action_data = round_action_data
        self.narrative = narrative

    def get_round_summary(self):
        prompt = f"""The round has been completed we have several metrics for you to look over for you to determine what has changed from the initial narrative. Your job is to take the previous rounds narrative, and look at the actions of the AI, and the actions of the player_decision_text to determine what the motivations for each round were. From there we will look at the round_action_data. The round action data will tell us which of the moves performed by the AI and moves performed by the player were successful, and: {self.player_decision_text}, 
                        AI's actions: {self.ai_actions}, 
                        and the round's action data: {json.dumps(self.round_action_data)}."""
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "Provide a summary of the round's key events."},
                {"role": "user", "content": prompt}
            ]
        )
        round_summary = response.choices[0].message.content
        return round_summary

