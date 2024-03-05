# PJSK Team Talent Calculator
An application you can calculate your team talent.

## Usage
### Example
```python main.py -c miku,kanade,saki,rui,emu -g moreMJump -r 4,4,0,3,4 -m 0,0,3,5,0 -s 2,2,2,1,0 -a 14,12,10,16,20 -t 2.5,1.5,3,0.5,1 -b 1.5,2,2.5,3.1,1.9 -x n -q n```
### Commands
```
"-c" | 5 character input | Example: -c miku,kanade,saki,rui,emu
"-g" | Virtual Singer subgroup. Input in order. 0 = no sub group. | Example: -c miku,nene,len,ichika,kaito -g leoNeed,moreMJump,0 | miku = leoNeed , len = moreMJump , kaito = No Sub Group
"-r" | Char rarity input. Birthday = 0. | Example: -r 0,3,3,4,4
"-m" | Mastery input. | Example: -m 0,1,2,5,5
"-s" | Side story input. All Locked = 0, Unlocked Story = 1 or 2. | Example: -s 0,0,1,2,2
"-a" | Character accesory input. Buff percent. | Example: -a 2,5,15,20,18
"-e" | Type accesory. Buff percent. | Example: -e 2.5,1.5,3,0.5,1
"-t" | Team accessory input. Buff percent. | Example: -t 2.5,1.5,3,0.5,1
"-b" | Character rank talent bonus. Buff percent. | Example: -b 1.5,2.0,2.5,3.1,1.9
"-x" | Is types of all the characters same? Type y or n. | Example: -x y
"-q" | Is teams of all the characters same? Type y or n. | Example -q n
```
### Character and Team Codes
```
# Character Codes
miku
rin
len
luka
meiko
kaito

ichika
saki
honami
shiho

minori
haruka
airi
shizuku

kohane
an
akito
toya

tsukasa
emu
nene
rui

kanade
mafuyu
ena
mizuki
```
```
# Team Codes
0        #no sub group
leoNeed
moreMJump
vividBSquad
wonderLShowT
nightcord25
```

## Warning
Calculator results may not match with results in the game %100, has a small margin of error.
