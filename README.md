# PJSK Team Talent Calculator
An application you can calculate your team talent.

## Usage
### Example
```python main.py -c char1,char2,char3.char4,char5 -g sub_group_if_there_is_in_order -r 4,4,0,3,4 -m 0,0,3,5,0 -s 2,2,2,1,0 -a 14,12,10,16,20 -t 2.5,1.5,3,0.5,1 -b 1.5,2,2.5,3.1,1.9 -x n -q n```
### Commands
```
"-c", "--characters" | 5 character input | Example: -c miku,kanade,saki,rui,emu
"-g", "--sub_group" | Virtual Singer subgroup input. Can take multiple input. If input amount isn't equal to Virtual Singer amount; you will get error. | Example: -g leoNeed,moreMJump
"-r", "--rarity | Char rarity input. Birthday = 0. | Example: -r 0,3,3,4,4
"-m", "--mastery" | Mastery input. | Example: -m 0,1,2,5,5
"-s", "--side_story" | Side story input. All Locked = 0, Unlocked Story = 1 or 2. | Example: -s 0,0,1,2,2
"-a", "--accesory" | Character accesory input. Buff percent. | Example: -a 2,5,15,20,18
"-e", "--element_accesory" | Type accesory. Buff percent. | Example: -e 2.5,1.5,3,0.5,1
"-t", "--team_accesory" | Team accessory input. Buff percent. | Example: -t 2.5,1.5,3,0.5,1
"-b", "--talent_bonus" | Character rank talent bonus. Buff percent. | Example: -b 1.5,2.0,2.5,3.1,1.9
"-x", "--all_same_type" | Is types of all the characters same? Type y or n. | Example: -x y
"-q", "--all_same_team" | Is teams of all the characters same? Type y or n. | Example -q n
```

## Warning
Calculator results may not match with results in the game %100, has a small margin of error.
