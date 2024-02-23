class TurnManager:
    def __init__(self):
        self.record = {}
        self.payoff_matrix = {
            ('cooperate', 'cooperate'): (3, 3),
            ('cooperate', 'defect'): (0, 5),
            ('defect', 'cooperate'): (5, 0),
            ('defect', 'defect'): (1, 1)
        }

    def record_turn(self, round_number, round_action_data):
        # Record the details of each turn including the decisions and outcomes
        self.record[round_number] = round_action_data

    def evaluate_moves(self, type_move_player, type_move_ai):
        return self.payoff_matrix.get((type_move_player, type_move_ai), (0, 0))

        
