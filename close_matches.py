from difflib import get_close_matches
names = ['Siddharth','Suraj','Python','Garg','Raj']
print(get_close_matches('Pythonis',names)) #Python
print(get_close_matches('Gargis',names)) #Garg
