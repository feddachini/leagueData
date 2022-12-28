from riotwatcher import LolWatcher, ApiError
import pandas as pd

LIGHT_BLUE = "\033[1;34m"  # ANSI code

####################
# global variables #
api_key = 'RGAPI-3983c4de-0d2b-4da9-842a-0c40e60d7d11'
watcher = LolWatcher(api_key)
my_region = 'na1'
#                  #
####################

# using riotwatcher object to get summoner info
me = watcher.summoner.by_name(my_region, 'feddachini')

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'])

# fetch last match detail
last_match = my_matches[0]
match_detail = watcher.match.by_id(my_region, last_match)

participants = []
for row in (match_detail.get('info')).get('participants'):
    participants_row = {'summonerName': row['summonerName'],
                        'champion': row['championId'],
                        # 'spell1Casts': row['spell1Casts'],
                        # 'spell2Casts': row['spell2Casts'],
                        'win': row['win'],
                        'kills': row['kills'],
                        'deaths': row['deaths'],
                        'assists': row['assists'],
                        'totalDamageDealt': row['totalDamageDealt'],
                        # 'goldEarned': row['goldEarned'],
                        # 'champLevel': row['champLevel'],
                        # 'totalMinionsKilled': row['totalMinionsKilled'],
                        # 'item0': row['item0'],
                        # 'item1': row['item1']
                        }
    participants.append(participants_row)

# Check league's latest version
latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']

# Champ static information
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

# Champ static list-data to dict for look up
champ_dict = {}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[row['key']] = row['id']

# Change ChampID to ChampName in table
for row in participants:
    row['champion'] = champ_dict[str(row['champion'])]

df = pd.DataFrame(participants)

print(LIGHT_BLUE + "feddachini's latest game")
print(df)
