from Rrich import print, input
from classes import characters
import sys

#     Method Listesi
#
# komut()                      | Komut çekme
#
# chardogrumu(char:str)        | inputlanan karakterin geçerli olup olmadığını kontrol eder, boolean döndürür
# keyscan(key:str)             | karakterin key değerine bakarak diğer tüm bilgilerini döndürür
# charalma(inpt:str)           | ! charInput() tarafından tetiklenir ! Liste / Input farkını ayarlar, geçerli girişe True, geçersiz girişe False döndürür
# charInput()                  | Takıma karakter ve info girişi
# virtualSSub(key:str, id:int) | Karakter Virtual Singer mı diye bakar ve öyleyse sub grup sorar
# sideStory()                  | Side story aktif mi diye bakar
# mastery()                    | Mastery rankını alır
# accesoryInput()              | Aksesuar buff miktarı girişi
# charTalentInput()            | Character Rank Talent Bonus girişi
# sonHesap()                   | Takımın toplam talentini döndürür

menu = """[bold][yellow]╰┈➤ [/yellow] [green]Komut Listesi[/green][yellow] ✧.*[/yellow][/bold]
1 | Grup Toplam Talent Hesaplama
2 | Çıkış"""

def komut():  
    print("\n", menu, "\n")  
    while True:        
        girdi = input("[bold light_cyan1]İşlem Seçiniz[/bold light_cyan1][bold yellow] ̗̀➛[/bold yellow]  ")
        match girdi:
            case "1":
                grupTalentHesaplama()
                selected.clear()
                print("\n", menu, "\n")
                continue
            case "2":
                sys.exit()            
                break
            case default:
                print("[bold red]\nGeçersiz giriş, lütfen seçiminizin sayısal kodunu girin[/bold red] [yellow]:>[/yellow]")
                continue

def chardogrumu(char:str):
    for n in range(0,len(characters.chars)):
        if char == characters.chars[n]["key"]:
            return True           
    return False

def keyscan(key:str):
    for n in range(0,len(characters.chars)):
        if characters.chars[n]["key"] == key:
            return {"name":characters.chars[n]["name"], "color":characters.chars[n]["color"], "team":characters.chars[n]["team"]}

# charalma() Değişkenleri
selected = []
attribuffs = {}
areabuffs = {}

def virtualSSub(key:str, id:int):
    if keyscan(key)["team"] == "virtualS":
                print("""
            [bold #4455DD]Leo*╯Need[/bold #4455DD] : ̗̀➛ leo
            [bold][#FF679A]MO[/#FF679A][#3367CD]RE[/#3367CD] [#FF7721]MO[/#FF7721][#9AEEDE]RE[/#9AEEDE] [#6CCB20]ꕥ JUMP[/#6CCB20][/bold] : ̗̀➛ jump
            [bold][#EE1166]Vivid[/#EE1166][#33CCBA]✗.[/#33CCBA][#BBDE22]BAD[/#BBDE22] [#EE1166]S[/#EE1166][#33AAEE]Q[/#33AAEE][#EE1166]U[/#EE1166][#33AAEE]A[/#33AAEE][#EE1166]D[/#EE1166][/bold] : ̗̀➛ vivid
            [bold][#ffc85a]W[/#ffc85a][#86d2a1]o[/#86d2a1][#ffc85a]n[/#ffc85a][#86d2a1]d[/#86d2a1][#ffc85a]e[/#ffc85a][#86d2a1]r[/#86d2a1][#ffc85a]l[/#ffc85a][#86d2a1]a[/#86d2a1][#ffc85a]n[/#ffc85a][#86d2a1]d[/#86d2a1][#ffc85a]s[/#ffc85a][#eecec2]✘[/#eecec2][/bold] [bold][#fc848f]S[/#fc848f][#56bcdb]h[/#56bcdb][#fc848f]o[/#fc848f][#56bcdb]w[/#56bcdb][#fc848f]t[/#fc848f][#56bcdb]i[/#56bcdb][#fc848f]m[/#fc848f][#56bcdb]e[/#56bcdb][/bold] : ̗̀➛ wonderlands
            [bold][gray50]Ni[/gray50][#627bd1]/[/#627bd1][gray50]ghtcord at[/gray50][#627bd1]✗[/#627bd1][gray50]25:00[/gray50][/bold] : ̗̀➛ nightcord
                       """)
                
                sub = input("Seçtiğin karakterin sub grubu nedir? [bold][yellow]([/yellow]Yok ise '[red]none[/red]' yaz[yellow])[/yellow][/bold] : ̗̀➛ ")
                while not (sub == "leo" or sub == "jump" or sub == "vivid" or sub == "wonderlands" or sub == "nightcord" or sub == "none"):
                    print("[bold red]\nGeçersiz giriş, lütfen seçiminizin kodunu girin[/bold red] [yellow]:>[/yellow] \n")
                    sub = input("Seçtiğin karakterin sub grubu nedir? [bold][yellow]([/yellow]Yok ise '[red]none[/red]' yaz[yellow])[/yellow][/bold] : ̗̀➛ ")   
                
                selected[id]["sub_group"] = sub
    print("")

def charalma(inpt:str):
# Listeleme    
    if inpt == "list":
        current = ""
        print("")
        for n in range(0, len(characters.chars)):        
            if current == "":
                current = characters.chars[n]["team"]
                print("\n[bold gray50]: ̗̀➛ VIRTUAL SINGER[/bold gray50]")        
            elif current != characters.chars[n]["team"]:
                current = characters.chars[n]["team"]
                match current:
                    case "leoNeed":
                        print("\n[bold gray50]: ̗̀➛ [/bold gray50][bold #4455DD]Leo*╯Need[/bold #4455DD]")
                    case "moreMJump":
                        print("\n[bold gray50]: ̗̀➛ [/bold gray50][bold][#FF679A]MO[/#FF679A][#3367CD]RE[/#3367CD] [#FF7721]MO[#9AEEDE]RE[/#9AEEDE] [#6CCB20]ꕥ JUMP[/#6CCB20][/bold]")
                    case "vividBSquad":
                        print("\n[bold gray50]: ̗̀➛ [/bold gray50][bold][#EE1166]Vivid[/#EE1166][#33CCBA]✗.[/#33CCBA][#BBDE22]BAD[/#BBDE22] [#EE1166]S[/#EE1166][#33AAEE]Q[/#33AAEE][#EE1166]U[/#EE1166][#33AAEE]A[/#33AAEE][#EE1166]D[/#EE1166][/bold]")
                    case "wonderLShowT":
                        print("\n[bold gray50]: ̗̀➛ [/bold gray50][bold][#ffc85a]W[/#ffc85a][#86d2a1]o[/#86d2a1][#ffc85a]n[/#ffc85a][#86d2a1]d[/#86d2a1][#ffc85a]e[/#ffc85a][#86d2a1]r[/#86d2a1][#ffc85a]l[/#ffc85a][#86d2a1]a[/#86d2a1][#ffc85a]n[/#ffc85a][#86d2a1]d[/#86d2a1][#ffc85a]s[/#ffc85a][#eecec2]✘[/#eecec2][/bold] [bold][#fc848f]S[/#fc848f][#56bcdb]h[/#56bcdb][#fc848f]o[/#fc848f][#56bcdb]w[/#56bcdb][#fc848f]t[/#fc848f][#56bcdb]i[/#56bcdb][#fc848f]m[/#fc848f][#56bcdb]e[/#56bcdb][/bold]")
                    case "nightcord25":
                        print("\n[bold gray50]: ̗̀➛ [/bold gray50][bold][gray50]Ni[/gray50][#627bd1]/[/#627bd1][gray50]ghtcord at[/gray50][#627bd1]✗[/#627bd1][gray50]25:00[/gray50][/bold]")

            print(f"[bold {characters.chars[n]["color"]}]{characters.chars[n]["name"]}[/bold {characters.chars[n]["color"]}]: {characters.chars[n]["key"]}")
        return False
# Karakter Algılama            
    elif chardogrumu(inpt):
        selected.append({"key":inpt})
        print(f"[bold]Seçilen karakter: [{keyscan(inpt)["color"]}]{keyscan(inpt)["name"]}[/{keyscan(inpt)["color"]}][/bold]","\n")
        virtualSSub(inpt, 0)

        secilen = 1
        while secilen < 5:
            secilenchar = input("[bold]Karakter seçiniz ̗̀➛ [/bold]")
            if not chardogrumu(secilenchar):
                print("[bold red]\nGeçersiz giriş, lütfen seçiminizin kodunu girin[/bold red] [yellow]:>[/yellow]")
                continue
            print(f"[bold]Seçilen karakter: [{keyscan(secilenchar)["color"]}]{keyscan(secilenchar)["name"]}[/{keyscan(secilenchar)["color"]}][/bold]","\n")
            selected.append({"key":secilenchar})
            virtualSSub(secilenchar, secilen)
            secilen+=1
        return True
    else:
        print("[bold red]\nGeçersiz giriş, lütfen seçiminizin kodunu girin[/bold red] [yellow]:>[/yellow] \n")
        return False

def charInput():
    inp = input("[bold]Takıma ekleyeceğiniz kartın kodunu yazın, kodları görmek için [blue]'list'[/blue] yazın. ̗̀➛ [/bold]")
    while not charalma(inp):
        if inp == "list":
            inp = input("\n[bold]Takıma ekleyeceğiniz kartın kodunu yazın. ̗̀➛ [/bold]")
        else:
            inp = input("\n[bold]Takıma ekleyeceğiniz kartın kodunu yazın, kodları görmek için [blue]'list'[/blue] yazın. ̗̀➛ [/bold]")
    


    n = 0
    while n < 5:
        inp = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}] kaç yıldızlı? [bold][yellow]([/yellow]Doğum günü karakteri ise '0' yaz[yellow])[/yellow] ̗̀➛ ")
        try:
            if int(inp) not in range(0,5):
                print("[bold red]\nGeçersiz giriş, lütfen 0 - 4 arası bir rakam girin[/bold red] [yellow]:>[/yellow] \n")
                continue
            selected[n]["stars"] = int(inp)
        except ValueError:
            print("[bold red]\nGeçersiz giriş, lütfen 0 - 4 arası bir rakam girin[/bold red] [yellow]:>[/yellow] \n")
            continue
        n+=1

    print("""\n[bold gray50]: ̗̀➛ Attributes[/bold gray50]
     [bold #796bc3] Mysterious[/bold #796bc3]: mys
     [bold #fc9729] Happy[/bold #fc9729]: hap
     [bold #fe74a5] Cute[/bold #fe74a5]: cut
     [bold #04b94e] Pure[/bold #04b94e]: pur
     [bold #475ef9] Cool[/bold #475ef9]: coo\n""")

    n = 0
    while n < 5:
        inp = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}] hangi gruptan? ̗̀➛ ")
        match inp:
            case "mys":
                selected[n]["attribute"] = "mys"
            case "hap":
                selected[n]["attribute"] = "hap"
            case "cut":
                selected[n]["attribute"] = "cut"
            case "pur":
                selected[n]["attribute"] = "pur"
            case "coo":
                selected[n]["attribute"] = "coo"
            case default:
                print("[bold red]\nGeçersiz giriş, lütfen seçiminizin kodunu girin[/bold red] [yellow]:>[/yellow] \n")
                continue
        n+=1
    print("")

def sideStory():
    for n in range(0,5):
        st = ""
        while (st != "e" or st != "h"):
            st = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in 1. Hikayesi açık mı? [bold yellow]([/bold yellow] '[bold blue]e[/bold blue]' veya '[bold blue]h[/bold blue]' ile yanıt verin [bold yellow])[/bold yellow]")        
            if (st == "e" or st == "h"):
                match st:
                    case "e":
                        selected[n]["story1"] = True
                        print(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in 1. Hikayesi: [bold green]Açık[/bold green]\n")
                    case "h":
                        selected[n]["story1"] = False
                        print(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in 1. Hikayesi: [bold red]Kapalı[/bold red]\n")
                break
            print("[bold red]\nGeçersiz giriş, lütfen seçiminizin kodunu girin[/bold red] [yellow]:>[/yellow] \n")
        
        st = ""
        while (st != "e" or st != "h"):
            st = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in 2. Hikayesi açık mı? [bold yellow]([/bold yellow] '[bold blue]e[/bold blue]' veya '[bold blue]h[/bold blue]' ile yanıt verin [bold yellow])[/bold yellow]")        
            if (st == "e" or st == "h"):
                match st:
                    case "e":
                        selected[n]["story2"] = True
                        print(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in 2. Hikayesi: [bold green]Açık[/bold green]\n")
                    case "h":
                        selected[n]["story2"] = False
                        print(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in 2. Hikayesi: [bold red]Kapalı[/bold red]\n")
                break
            print("[bold red]\nGeçersiz giriş, lütfen seçiminizin kodunu girin[/bold red] [yellow]:>[/yellow] \n")

def mastery():
    for n in range(0,5):
        st = None
        while st not in range(0,6):
            st = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in Mastery Rankı kaç? ̗̀➛ ")        
            try:
                if int(st) in range(0,6):
                    selected[n]["mastery"] = int(st)
                    print(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}]'in Mastery Rankı: {selected[n]["mastery"]}\n")
                    break
                print("[bold red]\nGeçersiz giriş, lütfen 0-5 arası bir rakam girin[/bold red] [yellow]:>[/yellow] \n")
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen 0-5 arası bir rakam girin[/bold red] [yellow]:>[/yellow] \n")
                continue


def accesoryInput():
    attris = {"mys":False, "hap":False, "cut":False, "pur":False, "coo":False}
    teams = {"virtualS":False, "leoNeed":False, "moreMJump":False, "vividBSquad":False, "wonderLShowT":False, "nightcord25":False}
    for n in range(0,5):
        attris[selected[n]["attribute"]] = True
    
    if attris["mys"]:
        while True:
            buff = input("[bold #796bc3]Mysterious[/bold #796bc3] buff oranı ̗̀➛ %")
            try:
                attribuffs["mys"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if attris["hap"]:
        while True:
            buff = input("[bold #fc9729]Happy[/bold #fc9729] buff oranı ̗̀➛ %")
            try:
                attribuffs["hap"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if attris["cut"]:
        while True:
            buff = input("[bold #fe74a5]Cute[/bold #fe74a5] buff oranı ̗̀➛ %")
            try:
                attribuffs["cut"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if attris["pur"]:
        while True:
            buff = input("[bold #04b94e]Pure[/bold #04b94e] buff oranı ̗̀➛ %")
            try:
                attribuffs["pur"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if attris["coo"]:
        while True:
            buff = input("[bold #475ef9]Cool[/bold #475ef9] buff oranı ̗̀➛ %")
            try:
                attribuffs["coo"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue

    print("")

    for x in range(0,5):
        teams[keyscan(selected[x]["key"])["team"]] = True
        if keyscan(selected[x]["key"])["team"] == "virtualS":
            if selected[x]["sub_group"] != "none":
                teams[selected[x]["sub_group"]] = True

    if teams["virtualS"] == True:
        while True:
            buff = input("[bold gray50]VIRTUAL SINGER[/bold gray50] buff oranı ̗̀➛ %")
            try:
                areabuffs["virtualS"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if teams["leoNeed"] == True:
        while True:
            buff = input("[bold #4455DD]Leo*╯Need[/bold #4455DD] buff oranı ̗̀➛ %")
            try:
                areabuffs["leoNeed"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if teams["moreMJump"] == True:
        while True:
            buff = input("[bold][#FF679A]MO[/#FF679A][#3367CD]RE[/#3367CD] [#FF7721]MO[/#FF7721][#9AEEDE]RE[/#9AEEDE] [#6CCB20]ꕥ JUMP[/#6CCB20][/bold] buff oranı ̗̀➛ %")
            try:
                areabuffs["moreMJump"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if teams["vividBSquad"] == True:
        while True:
            buff = input("[bold][#EE1166]Vivid[/#EE1166][#33CCBA]✗.[/#33CCBA][#BBDE22]BAD[/#BBDE22] [#EE1166]S[/#EE1166][#33AAEE]Q[/#33AAEE][#EE1166]U[/#EE1166][#33AAEE]A[/#33AAEE][#EE1166]D[/#EE1166][/bold] buff oranı ̗̀➛ %")
            try:
                areabuffs["vividBSquad"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if teams["wonderLShowT"] == True:
        while True:
            buff = input("[bold][#ffc85a]W[/#ffc85a][#86d2a1]o[/#86d2a1][#ffc85a]n[/#ffc85a][#86d2a1]d[/#86d2a1][#ffc85a]e[/#ffc85a][#86d2a1]r[/#86d2a1][#ffc85a]l[/#ffc85a][#86d2a1]a[/#86d2a1][#ffc85a]n[/#ffc85a][#86d2a1]d[/#86d2a1][#ffc85a]s[/#ffc85a][#eecec2]✘[/#eecec2][/bold] [bold][#fc848f]S[/#fc848f][#56bcdb]h[/#56bcdb][#fc848f]o[/#fc848f][#56bcdb]w[/#56bcdb][#fc848f]t[/#fc848f][#56bcdb]i[/#56bcdb][#fc848f]m[/#fc848f][#56bcdb]e[/#56bcdb][/bold] buff oranı ̗̀➛ %")
            try:
                areabuffs["wonderLShowT"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    if teams["nightcord25"] == True:
        while True:
            buff = input("[bold][gray50]Ni[/gray50][#627bd1]/[/#627bd1][gray50]ghtcord at[/gray50][#627bd1]✗[/#627bd1][gray50]25:00[/gray50][/bold] buff oranı ̗̀➛ %")
            try:
                areabuffs["nightcord25"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    
    print("")

    for n in range(0,5):
        while True:
            buff = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}] karakterinin kişisel dekorasyonundan gelen buff oranı ̗̀➛ %")
            try:
                selected[n]["charBonus"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue
    print("")
        

def charTalentInput():
    for n in range(0,5):
        while True:
            buff = input(f"[bold {keyscan(selected[n]["key"])["color"]}]{keyscan(selected[n]["key"])["name"]}[/bold {keyscan(selected[n]["key"])["color"]}] karakterinin Character Rank'tan gelen talent buff oranı ̗̀➛ %")
            try:
                selected[n]["talentBonus"] = float(buff)
                break
            except ValueError:
                print("[bold red]\nGeçersiz giriş, lütfen sayı girin[/bold red] [yellow]:>[/yellow] \n")
                continue

# Rarity'e göre talent veritabanı (All Upgraded)
# h ekleri Hatsune Miku'nun değerleridir, v ekleri tüm Virtual Singer'lara aittir
_4 = 32045 # neredeyse global
_4h = 31743
_3 = 30269
_3v = 28167
_2 = 18318
_2v = 16971
_1 = 7574 # global
_0 = 30656 # global


def sonHesap():
# Initial Talent
    for n in range(0,5):
        if selected[n]["stars"] == 4:
            if selected[n]["key"] == "hm":
                selected[n]["init_talent"] = _4h
            else:
                selected[n]["init_talent"] = _4

        elif selected[n]["stars"] == 3:
            if keyscan(selected[n]["key"])["team"] == "virtualS":
                selected[n]["init_talent"] = _3v
            else:
                selected[n]["init_talent"] = _3

        elif selected[n]["stars"] == 2:
            if keyscan(selected[n]["key"])["team"] == "virtualS":
                selected[n]["init_talent"] = _2v
            else:
                selected[n]["init_talent"] = _2
        
        elif selected[n]["stars"] == 1:
            selected[n]["init_talent"] = _1

        elif selected[n]["stars"] == 0:
            selected[n]["init_talent"] = _0

# Final Talent (imdat - yaprak var)
    if selected[0]["attribute"] == selected[1]["attribute"] == selected[2]["attribute"] == selected[3]["attribute"] == selected[4]["attribute"]:
        attribuffs[selected[0]["attribute"]]*=2

    if keyscan(selected[0]["key"])["team"] == keyscan(selected[1]["key"])["team"] == keyscan(selected[2]["key"])["team"] == keyscan(selected[3]["key"])["team"] == keyscan(selected[4]["key"])["team"]:
        areabuffs[keyscan(selected[0]["key"])["team"]]*=2
    else:       
        subs = []
        for n in range(0,5):
            if keyscan(selected[n]["key"])["team"] == "virtualS":
                if selected[n]["sub_group"] != "none":
                    subs.append(selected[n]["sub_group"])
            else:
                subs.append(keyscan(selected[n]["key"])["team"])

        if subs[0] == subs[1] == subs[2] == subs[3] == subs[4]:
            areabuffs[selected[0]["sub_group"]]*=2

    for n in range(0,5):
        selected[n]["finalTalent"] = (selected[n]["init_talent"] * (1 + (attribuffs[selected[n]["attribute"]]/100 + areabuffs[keyscan(selected[n]["key"])["team"]]/100 + selected[n]["talentBonus"]/100) + selected[n]["charBonus"]/100))

    if selected[0]["attribute"] == selected[1]["attribute"] == selected[2]["attribute"] == selected[3]["attribute"] == selected[4]["attribute"]:
        attribuffs[selected[0]["attribute"]]/=2

    if keyscan(selected[0]["key"])["team"] == keyscan(selected[1]["key"])["team"] == keyscan(selected[2]["key"])["team"] == keyscan(selected[3]["key"])["team"] == keyscan(selected[4]["key"])["team"]:
        areabuffs[keyscan(selected[0]["key"])["team"]]/=2
    
    for n in range(0,5):
        match selected[n]["stars"]:
            case 0:
                masteryBonus = 540 * selected[n]["mastery"]
            case 1:
                masteryBonus = 150 * selected[n]["mastery"]
            case 2:
                masteryBonus = 300 * selected[n]["mastery"]
            case 3:
                masteryBonus = 450 * selected[n]["mastery"]
            case 4:
                masteryBonus = 600 * selected[n]["mastery"]

        selected[n]["finalTalent"] += masteryBonus

    for n in range(0,5):
        if selected[n]["story1"] == True:
            match selected[n]["stars"]:
                case 0:
                    storyBonus = 720
                case 1:
                    storyBonus = 300
                case 2:
                    storyBonus = 450
                case 3:
                    storyBonus = 600
                case 4:
                    storyBonus = 750

        selected[n]["finalTalent"] += storyBonus

        if selected[n]["story2"] == True:
            match selected[n]["stars"]:
                case 0:
                    storyBonus = 1650
                case 1:
                    storyBonus = 600
                case 2:
                    storyBonus = 900
                case 3:
                    storyBonus = 1500
                case 4:
                    storyBonus = 1800

        selected[n]["finalTalent"] += storyBonus

def grupTalentHesaplama():
    charInput()       
    mastery()
    sideStory()
    accesoryInput()
    charTalentInput()
    sonHesap()

    print("")
    print("[bold gray50]####################################[/bold gray50]")
    print("[bold gray50]#  [/bold gray50]")
    for n in range(0,5):
        print(f"[bold gray50]#  [/bold gray50][bold {keyscan(selected[n]["key"])["color"]}] {keyscan(selected[n]["key"])["name"]} [/bold {keyscan(selected[n]["key"])["color"]}]: [white]{int(selected[n]["finalTalent"])}[/white]")
    print("[bold gray50]#  [/bold gray50]")

    toplamTalent = 0

    for n in range(0,5):
        toplamTalent+=selected[n]["finalTalent"]

    print(f"[bold gray50]#  [/bold gray50][bold yellow]Toplam Talent:[/bold yellow] {int(toplamTalent)}")
    print("[bold gray50]#  [/bold gray50]")
    print("[bold gray50]####################################[/bold gray50]")
    