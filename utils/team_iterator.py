import json

class TeamIterator:
    def __init__(self, teams_json):
        self.teams = self._normalize_teams(teams_json)

    def __str__(self):
        return json.dumps(self.teams, indent=4)

    def _normalize_teams(self, teams_json):
        """
        Normalizes teams data into a consistent list format, navigating through nested JSON structures.
        """
        normalized_teams = []
        self._extract_teams(teams_json, normalized_teams)
        return normalized_teams

    def _extract_teams(self, element, normalized_teams):
        """
        Recursively searches and extracts team dicts from any JSON structure.
        """
        if isinstance(element, dict):
            if all(key in element for key in ['name', 'description', 'lossConditions', 'winConditions']):
                normalized_teams.append(element)
            else:
                for value in element.values():
                    self._extract_teams(value, normalized_teams)
        elif isinstance(element, list):
            for item in element:
                self._extract_teams(item, normalized_teams)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.teams):
            result = self.extract_team_data(self.teams[self._index])
            self._index += 1
            return result
        else:
            raise StopIteration

    @staticmethod
    def extract_team_data(team):
        """
        Extracts specified attributes from a team entry.
        """
        return {
            'name': team.get('name', 'Unknown Team'),
            'description': team.get('description', 'No description available.'),
            'lossConditions': team.get('lossConditions', []),
            'winConditions': team.get('winConditions', [])
        }
