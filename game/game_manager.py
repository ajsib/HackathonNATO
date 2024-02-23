from utils.get_user_move import get_user_decision
from game.turn_manager import TurnManager
from classifiers import *
from utils import TeamIterator
import random
import json


class GameManager:
    def __init__(self, client, scenario):
        self.client = client
        self.scenario = scenario
        self.previous_summaries = []
        self.turn_manager = TurnManager()
        self.teams = {}
        self.win_loss_conditions = {}
        self.game_over = False
        self.round = 0
        self.start_game()
        print("Game started!")

    def start_game(self):
        # getting the teams and their details
        try:
            teams_ = TeamClassifier(self.client, self.scenario).classify_teams()
            self.teams = TeamIterator(teams_)

            for team in self.teams:
                team_data = TeamIterator.extract_team_data(team)
                win_conditions = team_data.get('winConditions', [])
                loss_conditions = team_data.get('lossConditions', [])
                team_conditions = {
                    'win': {condition: False for condition in win_conditions},
                    'loss': {condition: False for condition in loss_conditions}
                }

                # Store team's win and loss conditions in win_loss_conditions dictionary
                self.win_loss_conditions[team_data['name']] = team_conditions

            # Check for missing values
            if not teams_ or not self.teams or not self.win_loss_conditions:
                raise ValueError("Missing values in teams or win_loss_conditions")

        except ValueError as ve:
            print(f"Error occurred while starting the game: {ve}")
            print("Restarting the game...")
            self.start_game()

        except Exception as e:
            print(f"Error occurred while starting the game: {e}")

    def play_round(self):

        # narrative is scenario when the round count is 0, otherwise it is the previous round summary
        narrative = self.scenario if self.round == 0 else self.previous_summaries[-1]


        # Debugging Lines
        print(f"Round {self.round + 1}!\n")
        print(f"Narrative: {narrative}\n")
        print(f"Teams: {self.teams}\n")
        print(f"Win/Loss Conditions: {json.dumps(self.win_loss_conditions, indent=4)}\n")


        # Helper function to simulate success or failure of an action
        random_success = lambda: random.choice([True, False])

        round_action_data = {'player': [], 'ai': []}

        player_decision_text = get_user_decision()
        # player_decision_text = """As Team Blue, our initial move strategy is to fortify key strategic locations in the Baltic States to establish a strong defensive perimeter. This includes securing major cities, critical infrastructure such as airports and seaports, and key transportation routes. We will deploy our forces to bolster border defenses and establish forward operating bases to enhance our situational awareness and response capabilities. This will allow us to quickly detect and respond to any hostile incursions by Team Red and Orange. Additionally, we will conduct joint exercises and training with our allies from Team Green to ensure seamless coordination and interoperability between our forces. This will enable us to effectively deter and repel any aggressive actions by the invading forces. Furthermore, we will engage in diplomatic efforts to garner international support and solidarity for our defensive efforts in the Baltic States. This includes highlighting the importance of upholding territorial integrity and sovereignty, and the need to prevent further escalation of the conflict."""
        player_actions = ActionAnalyzer(self.client, player_decision_text).analyze_potential_actions()
        print(f"\nPlayer actions: {json.dumps(player_actions, indent=4)}\n")

        for action in player_actions:
            type_move_player = ActionClassifier(self.client, action).classify_action()
            round_action_data['player'].append({action: type_move_player, 'success': random_success()})

        print(f"Player actions with type: {json.dumps(round_action_data['player'], indent=4)}\n")

        ai_actions = GetActionsAI(self.client, narrative, num_moves=len(player_actions)).get_ai_actions()
        print(f"AI actions: {json.dumps(ai_actions, indent=4)}\n")
        for action in ai_actions:
            print(action)
            type_move_ai = ActionClassifier(self.client, action).classify_action()
            print(type_move_ai)
            round_action_data['ai'].append({action: type_move_ai, 'success': random_success()})
        print(f"AI actions with type: {json.dumps(round_action_data['ai'], indent=4)}")

        print(f"Round action data: {json.dumps(round_action_data, indent=4)}\n")
        for team_actions in round_action_data.values():
            print(team_actions, '↨')
            for action in team_actions:
                print(action)
                action_name, action_type = next(iter(action.items()))
                if action['success']:
                    WinLossCorrelate(self.client, action_name, action_type, self.win_loss_conditions).correlate_win_loss_conditions()

        print(f"Round action data: {json.dumps(round_action_data, indent=4)}\n")

        round_summary = GenerateRoundSummary(self.client, player_decision_text, ai_actions, round_action_data, narrative).get_round_summary()

        print(round_summary)

        self.previous_summaries.append(round_summary)
        self.turn_manager.record_turn(self.round, round_action_data)
        self.check_game_over()
        self.round += 1

    def check_game_over(self):
        for team_name, conditions in self.win_loss_conditions.items():
            win_conditions = conditions['win']
            loss_conditions = conditions['loss']
            
            # Check if all win conditions are True for the team
            if all(value for value in win_conditions.values()):
                self.game_over = True
                print(f"Game over! Team '{team_name}' has achieved all win conditions.")
                return
            
            # Check if all loss conditions are True for the team
            if all(value for value in loss_conditions.values()):
                self.game_over = True
                print(f"Game over! Team '{team_name}' has suffered all loss conditions.")
                return

    def run_game(self):
        self.start_game()
        while not self.game_over:
            self.play_round()
        print("Game over!")