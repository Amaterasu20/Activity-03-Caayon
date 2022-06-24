class Squirtle_Stats():
    def HP_Stat_Value(lvl,hp,iv,ev):
        HP_total = (((2 * hp + iv[0] + (ev[0]/4)) * lvl)/100) + lvl + 10
        return HP_total
    def Other_Stat_Value(atk,defense,SPatk,SPdef,spd,iv,ev,lvl,nature):
        str = [atk,defense,SPatk,SPdef,spd,]
        x = 0
        for x in range(len(str)):
            str[x] = (((((2 * str[x] + iv[x+1] + (ev[x+1]/4)) * lvl) / 100) + 5)) * nature[x + 1]
            x = x + 1
        return str