import Squirtle_script_1_stat as Script_Stat
import Squirtle_script_2_ev as Script_Ev

"""
Pokemon: Squirtle
Level = 45
Nature = Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)
Based Stats:
    Hp: 35 (iv = 20, ev = 90)
    Attack: 40 (iv = 15, ev = 70)
    Defense: 45 (iv = 25, ev = 80)
    Special Attack: 40 (iv = 22, ev = 77)
    Special Defense: 45 (iv = 27, ev = 90)
    Speed: 30 (iv = 10, ev = 60)
"""

iv = [0,0,0,0,0,0]
ev = [0,0,0,0,0,0]
nature = [1,1,1.1,1,1,0.9]
base = [0,0,0,0,0,0]
ivCalcu = [0,0,0,0,0,0]
evCalcu = [0,0,0,0,0,0]

Ev_Check = 0

addStat = [0,0,0,0,0,0]

def start():
    print("""
    Choose Calculation:

    1. Stats Calculation
    2. Ev Calculation
    3. Exit
    """)
    option = int(input("Choose an Option: "))
    if option == 1:
        Stats_Calculation()
    elif option == 2:
        while True:
            print("""
            1. Ev Calculation for Single Stats
            2. Ev Calculation for All Stats
            3. Back
            """)
            option = int(input("Choose an Option: "))
            if option == 1:
                Single_Stats()
            if option == 2:
                All_Stats()
            if option == 3:
                start()
            print("Invalid Input, Try Again")
    elif option == 3:
        exit()
    else:
        print("Invalid Input, Try again")
        start()

def Stats_Calculation():
    print("\nNote: IV values range from 0-31 and EV values range from 0-255 with maximumof 510 values in all Stats\n")

    print("\nEnter Pokemon Stats: ")
    lvl = int(input("Enter level: "))
    hp = int(input("Enter hp value: "))
    iv[0] = int(input("Enter IV value: "))
    ev[0] = int(input("Enter EV value: "))

    print("\nFor other Stats\n")
    atk = int(input("Enter Attack value: "))
    iv[1] = int(input("Enter IV value: "))
    ev[1] = int(input("Enter EV value: "))
    defense = int(input("Enter Defense value: "))
    iv[2] = int(input("Enter IV value: "))
    ev[2] = int(input("Enter EV value: "))
    SPatk = int(input("Enter Special Attack value: "))
    iv[3] = int(input("Enter IV value: "))
    ev[3] = int(input("Enter EV value: "))
    SPdef = int(input("Enter Special Defense value: "))
    iv[4] = int(input("Enter IV value: "))
    ev[4] = int(input("Enter EV value: "))
    spd = int(input("Enter Speed value: "))
    iv[5] = int(input("Enter IV value: "))
    ev[5] = int(input("Enter EV value: "))

    Ev_Check = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if Ev_Check > 510:
        print("\nThe total value should not exceed 510. Try Again")
        Stats_Calculation()

    print("\nPokemon Stats\n")
    print("Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
    HP_Total = Script_Stat.Squirtle_Stats.HP_Stat_Value(lvl,hp,iv,ev)
    print("\nHP: ",round(HP_Total,2),end='\n\n')
    print("Other Stats: \n")
    str = Script_Stat.Squirtle_Stats.Other_Stat_Value(atk,defense,SPatk,SPdef,spd,iv,ev,lvl,nature)
    StatsName = ['Attack: ','Defense: ','Special Attack: ','Special Defense: ','Speed: ']
    for x in range(len(str)):
        print(StatsName[x],round(str[x],2))
        x = x + 1
    Another_Calculation()

def Single_Stats():
    BaseStat = [0,0,0,0,0,0]
    while True:
        print("""
        1. HP
        2. Attack
        3. Defense
        4. Special Attack
        5. Special Defense
        6. Speed
        """)
        option = int(input("Choose an Option: "))
        if option == 1:
            Stat_Type = 'hp'
            print("\nEnter Pokemon Stats: ")
            lvl = int(input("Enter Level: "))
            BaseStat[0] = int(input("Enter HP: "))
            iv[0] = int(input("Enter IV: "))
            if iv[0] > 31:
                print("\nIV should range from 0 to 31. Try Again")
                Single_Stats()
            ev[0] = int(input("\nEnter EV: "))
            if ev[0] > 255:
                print("\nEV should range from 0 to 255. Try Again")
                Single_Stats()
            Stat = int(input("Desired Increased in Hp: "))

            Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature)

            print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
            print("\nThe Evs Needed to increased the ",Stat_Type,": ",round(Needed_Ev, 2))

            while True:
                print("""
                1. Another Evs Calculaton
                2. Back
                """)
                option = int(input("Choose an Option: "))
                if option == 1:
                    Single_Stats()
                if option == 2:
                    Another_Calculation()
                print("Invalid Input, Try Again")
        if option == 2:
            Stat_Type = 'attack'
            print("\nEnter Pokemon Stats: \n")
            lvl = int(input("Enter Level: "))
            BaseStat[1] = int(input("Enter Attack: "))
            iv[1] = int(input("Enter IV: "))
            ev[1] = int(input("Enter EV: "))
            Stat = int(input("Desired Increased in Attack: "))

            Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature)

            print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
            print("\nThe Evs Needed to increased the ",Stat_Type,": ",round(Needed_Ev, 2))

            while True:
                print("""
                1. Another Evs Calculaton
                2. Back
                """)
                option = int(input("Choose an Option: "))
                if option == 1:
                    Single_Stats()
                if option == 2:
                    Another_Calculation()
                print("Invalid Input, Try Again")
        if option == 3:
            Stat_Type = 'Defense'
            print("\nEnter Pokemon Stats: \n")
            lvl = int(input("Enter Level: "))
            BaseStat[2] = int(input("Enter Defense: "))
            iv[2] = int(input("Enter IV: "))
            ev[2] = int(input("Enter EV: "))
            Stat = int(input("Desired Increased in Defense: "))

            Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature)

            print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
            print("\nThe Evs Needed to increased the ",Stat_Type,": ",round(Needed_Ev, 2))

            while True:
                print("""
                1. Another Evs Calculaton
                2. Back
                """)
                option = int(input("Choose an Option: "))
                if option == 1:
                    Single_Stats()
                if option == 2:
                    Another_Calculation()
                print("Invalid Input, Try Again")
        if option == 4:
            Stat_Type = 'Special attack'
            print("\nEnter Pokemon Stats: \n")
            lvl = int(input("Enter Level: "))
            BaseStat[3] = int(input("Enter Special Attack: "))
            iv[3] = int(input("Enter IV: "))
            ev[3] = int(input("Enter EV: "))
            Stat = int(input("Desired Increased in Special Attack: "))

            Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature)

            print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
            print("\nThe Evs Needed to increased the ",Stat_Type,": ",round(Needed_Ev, 2))

            while True:
                print("""
                1. Another Evs Calculaton
                2. Back
                """)
                option = int(input("Choose an Option: "))
                if option == 1:
                    Single_Stats()
                if option == 2:
                    Another_Calculation()
                print("Invalid Input, Try Again")
        if option == 5:
            Stat_Type = 'Special Defense'
            print("\nEnter Pokemon Stats: \n")
            lvl = int(input("Enter Level: "))
            BaseStat[4] = int(input("Enter Special Defense: "))
            iv[4] = int(input("Enter IV: "))
            ev[4] = int(input("Enter EV: "))
            Stat = int(input("Desired Increased in Special Defense: "))

            Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature)

            print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
            print("\nThe Evs Needed to increased the ",Stat_Type,": ",round(Needed_Ev, 2))

            while True:
                print("""
                1. Another Evs Calculaton
                2. Back
                """)
                option = int(input("Choose an Option: "))
                if option == 1:
                    Single_Stats()
                if option == 2:
                    Another_Calculation()
                print("Invalid Input, Try Again")
        if option == 6:
            Stat_Type = 'Speed'
            print("\nEnter Pokemon Stats: \n")
            lvl = int(input("Enter Level: "))
            BaseStat[5] = int(input("Enter Speed: "))
            iv[5] = int(input("Enter IV: "))
            ev[5] = int(input("Enter EV: "))
            Stat = int(input("Desired Increased in Speed: "))

            Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_SingleStat(Stat_Type,BaseStat,lvl,iv,ev,Stat,nature)

            print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
            print("\nThe Evs Needed to increased the ",Stat_Type,": ",round(Needed_Ev, 2))

            while True:
                print("""
                1. Another Evs Calculaton
                2. Back
                """)
                option = int(input("Choose an Option: "))
                if option == 1:
                    Single_Stats()
                if option == 2:
                    Another_Calculation()
                print("Invalid Input, Try Again")
        print("Invalid Input, Try Agin")
        Single_Stats()

def All_Stats():
    Stat_Type = ['hp','attack','defense','special attack','special defense','speed']
    print("\nEnter Pokemon Stats: \n")
    lvl = int(input("Enter Level: "))
    for x in range(len(Stat_Type)):
        base[x] = int(input("Enter Base " + Stat_Type[x] + ": "))
        ivCalcu[x] = int(input("Enter IV: "))
        if ivCalcu[x] > 31:
            print("\nIv Should range from 0 to 31. Try Again")
            All_Stats()
        evCalcu[x] = int(input("Enter EV: "))
        if evCalcu[x] > 255:
            print("\nEv Should range from 0 to 255. Try Again")
            All_Stats()
        addStat[x] = int(input("Desired increased in " + Stat_Type[x] + ": "))
        x = x + 1

    Ev_Check = ev[0] + ev[1] + ev[2] + ev[3] + ev[4] + ev[5]
    if Ev_Check > 510:
        print("\nThe total value should not exceed 510. Try Again")
        All_Stats()

    Needed_Ev = Script_Ev.Squirtle_Ev.Squirtle_AllStat(lvl,base,ivCalcu,evCalcu,addStat,nature)

    print("Pokemon's Nature: Relaxed (Increased Stat in Defense, While Decreased Stat in Speed)")
    print("\nThe Evs needed to increased in: \n")

    for a in range(len(Stat_Type)):
        print(Stat_Type[a],": ",round(Needed_Ev[a], 2))
        a = a + 1

    Another_Calculation()

def Another_Calculation():
    while True:
        print("""
        1. Another Calculation
        2. End
        """)
        option = int(input("Choose an Option: "))
        if option == 1:
            start()
        if option == 2:
            exit()
        print("Invalid Input, Try Again")
        Another_Calculation()
start()