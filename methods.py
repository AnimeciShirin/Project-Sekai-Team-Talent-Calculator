from Rrich import print, input
from classes import characters
import sys

# Cleaning
for n in dir(characters):
    if not callable(getattr(characters, n)) and not n.startswith("__") and not type(getattr(characters, n)) == list:
        if type(getattr(characters, n)) != list:
            if getattr(characters, n)["team"] == "virtualS":
                getattr(characters, n)["sub"] = "0"



def get_group(char):
    try:
        return getattr(characters, char)["team"]
    except NameError or IndexError:
        sys.exit("At least one character input is wrong")


def calculate(
    chars,
    sub_group,
    rarity,
    mastery,
    side_story,
    accesory,
    element_accesory,
    team_accesory,
    talent_bonus,
    all_same_type,
    all_same_team
):
    # Char check
    try:
        c_sub_group = sub_group.replace(" ", "").split(",")

        c_char = chars.replace(" ", "").split(",")
        c_rarity = rarity.replace(" ", "").split(",")
        c_mastery = mastery.replace(" ", "").split(",")
        c_side_story = side_story.replace(" ", "").split(",")
        c_accesory = accesory.replace(" ", "").split(",")
        c_element_accesory = element_accesory.replace(" ", "").split(",")
        c_team_accesory = team_accesory.replace(" ", "").split(",")
        c_talent_bonus = talent_bonus.replace(" ", "").split(",")

        # team bonus        
        try:
            _w = 0
            for n in range(0, 5):
                if get_group(c_char[n]) == "virtualS":
                    getattr(characters, c_char[n])["sub"] = c_sub_group[_w]
                    _w += 1

        except IndexError:
            sys.exit("Sub group input amount isn't equal to Virtual Singer amount.")

        # Rarity Talent
        c_base_talent = []
        c_final_talent =[]
        for n in range(0,5):
            if getattr(characters, c_char[n])["name"] == "Hatsune Miku" and getattr(characters, c_char[n])["sub"] != "0":                
                # Sublu Miku
                if c_rarity[n] == "4":
                    c_base_talent.append(31746)
                elif c_rarity[n] == "3":
                    c_base_talent.append(28167)
                elif c_rarity[n] == "2":
                    c_base_talent.append(6788)
            elif getattr(characters, c_char[n])["team"] == "virtualS" and getattr(characters, c_char[n])["sub"] != "0":
                # Sublu VS
                if c_rarity[n] == "4":
                    c_base_talent.append(31743)
                elif c_rarity[n] == "3":
                    c_base_talent.append(28175)
                elif c_rarity[n] == "2":
                    c_base_talent.append(16968)
            else:
                # NORMAL ve SUBsuz VS
                if c_rarity[n] == "4":
                    c_base_talent.append(32045)
                elif c_rarity[n] == "3":
                    c_base_talent.append(30269)
                elif c_rarity[n] == "2":
                    c_base_talent.append(30269)
                elif c_rarity[n] == "1":
                    c_base_talent.append(7576)
                elif c_rarity[n] == "0":
                    c_base_talent.append(30656)

        # Side Story
        for n in range(0,5):
            if c_side_story[n] == "0":
                pass
            elif c_side_story[n] == "1":
                if c_rarity[n] == "4":
                    c_base_talent[n] += 750
                elif c_rarity[n] == "3":
                    c_base_talent[n] += 600
                elif c_rarity[n] == "2":
                    c_base_talent[n] += 450
                elif c_rarity[n] == "1":
                    c_base_talent[n] += 200
                elif c_rarity[n] == "0":
                    c_base_talent[n] += 720
            elif c_side_story[n] == "2":
                if c_rarity[n] == "4":
                    c_base_talent[n] += 2550
                elif c_rarity[n] == "3":
                    c_base_talent[n] += 2100
                elif c_rarity[n] == "2":
                    c_base_talent[n] += 1350
                elif c_rarity[n] == "1":
                    c_base_talent[n] += 900
                elif c_rarity[n] == "0":
                    c_base_talent[n] += 2370

        # Mastery Talent
        try:
            for n in range(0,5):
                if c_rarity[n] == "4":
                    c_base_talent[n] += int(c_mastery[n]) * 600
                elif c_rarity[n] == "3":
                    c_base_talent[n] += int(c_mastery[n]) * 450
                elif c_rarity[n] == "2":
                    c_base_talent[n] += int(c_mastery[n]) * 300
                elif c_rarity[n] == "1":
                    c_base_talent[n] += int(c_mastery[n]) * 150
                elif c_rarity[n] == "0":
                    c_base_talent[n] += int(c_mastery[n]) * 5407
        except TypeError:
            sys.exit("Mastery value should be integer")

        # Mastery|  S1 |  S2  |
        # 4* 600 | 750 | 2550 |
        # 0* 540 | 720 | 2370 |
        # 3* 450 | 600 | 2100 |
        # 2* 300 | 450 | 1350 |
        # 1* 150 | 200 |  900 |
            
            # Final Calculating
        try:
            for n in range(0,5):
                c_final_talent.append(float(c_base_talent[n] + c_base_talent[n] * (float(c_accesory[n])/100 + float(c_talent_bonus[n])/100)))

                if all_same_team == "y" or all_same_team == "Y":
                    c_final_talent[n] += c_base_talent[n]*(((float(c_team_accesory[n])/100)*2))
                else:
                    c_final_talent[n] += c_base_talent[n]*(float(c_team_accesory[n])/100)

                if all_same_type == "y" or all_same_type == "Y":
                    c_final_talent[n] += c_base_talent[n]*(((float(c_element_accesory[n])/100)*2))
                else:
                    c_final_talent[n] += c_base_talent[n]*(float(c_element_accesory[n])/100)
        except TypeError:
            sys.exit("Accessory and Talent bonus should be integer")
        except IndexError:
            sys.exit("There is no enough input")

        print("# Results #\n")
        for n in range(0,5):
            print(f"[{getattr(characters, c_char[n])["color"]}]{getattr(characters, c_char[n])["name"]}[/{getattr(characters, c_char[n])["color"]}] = {int(c_final_talent[n])}")
        print("\n")
        _total = 0
        for n in range(0,5):
            _total += c_final_talent[n]
        print(f"Total Talent: {int(_total)}")

    except NameError:
        sys.exit("At least one character input is wrong")
