from riotwatcher import LolWatcher, ApiError
import pandas as pd

####################
# global variables #
api_key = 'RGAPI-3983c4de-0d2b-4da9-842a-0c40e60d7d11'
watcher = LolWatcher(api_key)
my_region = 'na1'
#                  #
####################

me = watcher.summoner.by_name(my_region, 'feddachini')
print(me)

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'])
print("My Matches: ")
print(my_matches)

# fetch last match detail
last_match = my_matches[0]
match_detail = watcher.match.by_id(my_region, last_match)

# print((match_detail.get('info')).get('participants')[0])


participants = []
for row in (match_detail.get('info')).get('participants'):
    participants_row = {'champion': row['championId'],
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
df = pd.DataFrame(participants)
print(df)

#
# # check league's latest version
# latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
# # Lets get some champions static information
# static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
#
# # champ static list data to dict for looking up
# champ_dict = {}
# for key in static_champ_list['data']:
#     row = static_champ_list['data'][key]
#     champ_dict[row['key']] = row['id']
# for row in participants:
#     print(str(row['champion']) + ' ' + champ_dict[str(row['champion'])])
#     row['championName'] = champ_dict[str(row['champion'])]
#
# # print dataframe
# df = pd.DataFrame(participants)
# df
#
