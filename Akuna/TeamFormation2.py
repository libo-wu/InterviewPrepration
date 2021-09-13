import math

# Team Formation 2 和 这个里面第一题一样 输入：skills，minPlayers，minLevel，maxLevel，skills是每个player的skill level，
# 首先判断是否在minLevel和maxLevel之间，然后计算这些players能组成多少个组，每个组至少有minPlayers个players

def TeamFormation(skills, minSkill, maxSkill, minPlayers):
    good_players_num = 0
    for s in skills:
        if s >= minSkill and s <= maxSkill:
            good_players_num = good_players_num + 1

    return math.floor(good_players_num/minPlayers)


if __name__ == "__main__":
    skills = [-1,0,0,1,1,2,2,3,3,4,5,6]
    minSkill = 1
    maxSkill = 4
    minPlayers = 2

    team_num = TeamFormation(skills, minSkill, maxSkill, minPlayers)

    print(team_num)