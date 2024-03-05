from classes import characters
from Rrich import print, input
from methods import calculate
import argparse

print(f"[bold gray50]#####################################################################################[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]                                                                                   [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]                           [bold][cyan]Project[/cyan] [yellow]Sekai[/yellow][/bold] [deep_pink4]Talent Calculator[/deep_pink4]                         [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]                                                                                   [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]                                    [bold green]Creator:[/bold green] [yellow]Shirin[/yellow]                                [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]                                                                                   [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]              [bold cyan]Including accesories[/bold cyan] | another PJSK utility application              [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#[/bold gray50]                                                                                   [bold gray50]#[/bold gray50]")
print(f"[bold gray50]#####################################################################################[/bold gray50]")
print("")

parser = argparse.ArgumentParser(description="Calculate talent points")
# parser.add_argument("-i", "--input_file", required=True, help="Input video file.")

parser.add_argument("-c", "--characters", required=True, help="5 character input. Example: hm,kn,sai,krui,oe")
parser.add_argument("-g", "--sub_group", help="Virtual Singer subgroup input. Can take multiple input. If input amount isn't equal to Virtual Singer amount; you will get error. Example: leo,vivid")
parser.add_argument("-r", "--rarity", required=True, help="Char rarity input. Birtday = 0. Example: 0,3,3,4,4")
parser.add_argument("-m", "--mastery", required=True, help="Mastery input. Example: 0,1,2,5,5")
parser.add_argument("-s", "--side_story", required=True, help="Side story input. Closed = 0, Level = 1 or 2. Example: 0,0,1,2,2")
parser.add_argument("-a", "--accesory", required=True, help="Character accesory input. Buff percent. Example: 2,5,15,20,18")
parser.add_argument("-t", "--team_accesory", required=True, help="Team accessory input. Buff percent. Example: 2.5,1.5,3,0.5,1")
parser.add_argument("-e", "--element_accesory", required=True, help="Type accesory. Buff percent. Example: 2.5,1.5,3,0.5,1")
parser.add_argument("-b", "--talent_bonus", required=True, help="Character rank talent bonus. Buff percent. Example: 1.5,2.0,2.5,3.1,1.9")
parser.add_argument("-x", "--all_same_type", required=True, help="Is all the types same? Type y or n.")
parser.add_argument("-q", "--all_same_team", required=True, help="Is all the teams same? Type y or n.")

args = parser.parse_args()

calculate(
    args.characters,
    args.sub_group,
    args.rarity,
    args.mastery,
    args.side_story,
    args.accesory,
    args.element_accesory,
    args.team_accesory,
    args.talent_bonus,
    args.all_same_type,
    args.all_same_team
)