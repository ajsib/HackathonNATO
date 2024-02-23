from openai import AzureOpenAI

class WinLossCorrelate:
    def __init__(self, client: AzureOpenAI, action_name: str, action_type: str, win_loss_conditions: dict):
        self.client = client
        self.action_name = action_name
        self.action_type = action_type
        self.win_loss_conditions = win_loss_conditions

    def correlate_win_loss_conditions(self):
        # Crafting a more detailed prompt that explains the context, action, and asks for alignment with win/loss conditions
        prompt = self.generate_detailed_prompt()

        response = self.client.chat.completions.create(
            model="gpt-35-uncensored",
            temperature=0.5,  # Adjusting temperature for a balance between creativity and accuracy
            messages=[
                {"role": "system", "content": "Given the action description and its type, evaluate its alignment with specific win/loss conditions, considering the strategic objectives of each team."},
                {"role": "user", "content": prompt}
            ]
        )
        alignment = response.choices[0].message.content.strip().lower()
        
        # Updated logic to compare the alignment response directly with win/loss conditions
        self.update_conditions_based_on_alignment(alignment)

    def generate_detailed_prompt(self):
        # Creating a detailed prompt that includes the context of win/loss conditions
        conditions_summary = self.format_conditions_for_prompt()
        prompt = (f"Given the action '{self.action_name}' of type '{self.action_type}', and considering the following win/loss conditions for each team:\n{conditions_summary}\n"
                  f"Determine if this action aligns more closely with any team's win or loss conditions. Provide the team name and whether it aligns with a 'win' or 'loss' condition.")
        return prompt

    def format_conditions_for_prompt(self):
        # Formatting the win/loss conditions for inclusion in the prompt
        formatted_conditions = ""
        for team, conditions in self.win_loss_conditions.items():
            formatted_conditions += f"\nTeam {team}:\n"
            for outcome, actions in conditions.items():
                formatted_actions = ', '.join(actions.keys())
                formatted_conditions += f"  {outcome.capitalize()} conditions: {formatted_actions}\n"
        return formatted_conditions

    def update_conditions_based_on_alignment(self, alignment):
        # Parsing the alignment to find matches within win/loss conditions
        for team, conditions in self.win_loss_conditions.items():
            for outcome, actions in conditions.items():
                for action in actions.keys():
                    if action.lower() in alignment:
                        # Assuming the alignment response contains the team name and outcome ('win' or 'loss')
                        if team.lower() in alignment and outcome in alignment:
                            self.win_loss_conditions[team][outcome][action] = True
