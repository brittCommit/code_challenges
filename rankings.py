def rankings(matches):
  """
  Take a list of matches and return the final standings in order of the team with
  the most points. Ties receive 1 point each, winners 3 and losers 0.

  >>> rankings(["Liverpool 3:2 PSG", "RedStar 0:0 Napoli", "PSG 6:1 RedStar", "Napoli 1:0 Liverpool"])
  ['Napoli 4', 'Liverpool 3', 'PSG 3', 'RedStar 1']
  """

  team_dict = {}
  ret = []
  
  for match in matches:
    game = match.split(' ')
    team_1 = game[0]
    team_2 = game[2]
    score = game[1].split(':')
    score_1 = score[0]
    score_2 = score[1]

    if team_1 not in team_dict:
      team_dict[team_1] = 0
    if team_2 not in team_dict:
      team_dict[team_2] = 0
    if score_1 == score_2:
      team_dict[team_1] += 1
      team_dict[team_2] += 1
    if score_1 > score_2:
      team_dict[team_1] += 3
      team_dict[team_2] += 0
    if score_1 < score_2:
      team_dict[team_1] += 0
      team_dict[team_2] += 3

  for key, value in sorted(team_dict.items(), key=lambda x: x[1], reverse=True):
    total = key + ' ' + str(value)
    ret.append(total)

  return ret

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')