import requests
import random
import argparse
import json

parser = argparse.ArgumentParser(description='Process tournament info.')
parser.add_argument('--tournament-id', dest='tournament_id',
                    help='ID of the Lichess tournament')
parser.add_argument('--num-drawings', dest='num_drawings', type=int,
                    help='The number of drawings to choose')
args = parser.parse_args()

def draw(tournament_id, num_drawings):
  players = list()
  scores = list()
  page = 1
  url = f'https://lichess.org/api/tournament/{tournament_id}'
  while True:
    response = requests.get(url, params={'page': page})
    competitors = response.json().get('standing').get('players')
    if len(competitors) == 0:
      break

    for player in competitors:
      players.append(player.get('name'))
      scores.append(player.get('score'))
    page += 1

  drawings = random.choices(players, scores, k=num_drawings)
  print(f"Winners are: {', '.join(drawings)}")

if __name__ == '__main__':
  draw(args.tournament_id, args.num_drawings)
