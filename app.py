from openai import AzureOpenAI
from config.settings import AZURE_OPENAI_CONFIG
from classifiers import TeamClassifier
from utils.team_iterator import TeamIterator
import os
from game import GameManager

# Defining the client for the Azure OpenAI
client = AzureOpenAI(
    api_key=AZURE_OPENAI_CONFIG['api_key'],
    azure_endpoint=AZURE_OPENAI_CONFIG['endpoint'],
    api_version="2023-05-15"
)

# Path to the scenario file
scenario_path = os.path.join('.', 'scenario.txt')

# open the file and read the scenario
with open(scenario_path, 'r') as file:
    scenario = file.read()

# create test instance of the TeamClassifier found in ./classifiers/main_classifier.py
# teams = TeamClassifier(client, scenario).classify_teams()
# team_iterator = TeamIterator(teams)

# # iterate through the teams and print the name and description
# for team in team_iterator:
#     team_data = TeamIterator.extract_team_data(team)
#     # print(team)
#     print(team_data['name'])
#     print(team_data['lossConditions'])
#     print('\n')
    
g1 = GameManager(client, scenario)
g1.run_game()


