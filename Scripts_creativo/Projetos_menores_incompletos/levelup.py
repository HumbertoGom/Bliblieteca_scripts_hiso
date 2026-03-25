Lot = {
    'Name':'Lot',
    'Level':3,
    'HP' : 29,
    'Str':7,
    'Skl':6,
    'Spd':7,
    'Lck':2,
    'Def':4,
    'Res':1,
    'Con':12 ,
    'Aid':11,
    'Mov':5,

    'HpG':80,
    'StrG':30,
    'SklG':30,
    'SpdG':35,
    'LckG':30,
    'DefG':40,
    'ResG':15,
}

from random import randint





def levelup(char):
    char['Level']+=1
    print(char['Name'],' leveled up')
    print('')
    if randint(1,100) < char['HpG']:
        print(char['Name'] ,'ganhou +1HP')
        char['HP'] +=1
    if randint(1,100) < char['StrG']:
        print(char['Name'],' ganhou +Str')
        char['Str']+=1        

'''

print('GROW DE HP DO LOT',Lot['HpG'])

if randint(1,100)< Lot['HpG']:
    print('level up +1 de HP')
else:
    print('Lot não levelou HP')

'''
print(Lot)
levelup(Lot)
print(Lot)