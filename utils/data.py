import json
from entities.match_data import MatchData


def save_match_data(data: MatchData) -> None:
    with open('./data/match_data.json', 'w') as data_file:
        json.dump(data, data_file)


def load_match_data() -> MatchData:
    with open('./data/match_data.json', 'r') as data_file:
        match_data = json.load(data_file)
    return match_data


def save_replay_script(text: str) -> None:
    with open('./data/replay/run.sh', 'w') as data_file:
        data_file.write(text)
