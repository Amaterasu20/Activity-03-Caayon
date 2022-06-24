class Squirtle_Ev():
    def Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature):
        if Stat_Type == 'hp':
            D = (2 * BaseStat[0] + iv[0] + (ev[0]/4)) * (lvl/100)
            Needed_Ev = (((((Stat/nature[0]) - D) * 400) /lvl) / 4) + 4
        if Stat_Type == 'attack':
            D = (2 * BaseStat[1] + iv[1] + (ev[1]/4)) * (lvl/100)
            Needed_Ev = (((((Stat/nature[1]) - D) * 400) /lvl) / 4) + 4
        if Stat_Type == 'defense':
            D = (2 * BaseStat[2] + iv[2] + (ev[2]/4)) * (lvl/100)
            Needed_Ev = (((((Stat/nature[2]) - D) * 400) /lvl) / 4) + 4
        if Stat_Type == 'special attack':
            D = (2 * BaseStat[3] + iv[3] + (ev[3]/4)) * (lvl/100)
            Needed_Ev = (((((Stat/nature[3]) - D) * 400) /lvl) / 4) + 4
        if Stat_Type == 'special defense':
            D = (2 * BaseStat[4] + iv[4] + (ev[4]/4)) * (lvl/100)
            Needed_Ev = (((((Stat/nature[4]) - D) * 400) /lvl) / 4) + 4
        if Stat_Type == 'speed':
            D = (2 * BaseStat[5] + iv[5] + (ev[5]/4)) * (lvl/100)
            Needed_Ev = (((((Stat/nature[5]) - D) * 400) /lvl) / 4) + 4
        
        return Needed_Ev

    def Squirtle_AllStat(lvl,base,ivCalcu,evCalcu,addStat,nature):
        Needed_Ev = [0,0,0,0,0,0]
        for x in range(len(Needed_Ev)):
            D = (2 * base[x] + ivCalcu[x] + (evCalcu[x]/4)) * (lvl/100)
            Needed_Ev[x] = (((((addStat[x]/nature[x]) - D) * 400) / lvl) / 4) + 4
            x = x + 1

        return Needed_Ev