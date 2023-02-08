LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Vic_Recon = ''

while True:
    print("Big fish, enter a word/message\n No numerical or special characters allowed")
    JS_Word = input(">").upper()
    y = JS_Word.replace(" ", "")
    if y.isalpha():
        break
    else:
        print("[no numerical or special characters allowed]")
    
while True:
    print("Big fish, enter tries(a number)(has to be less than 26 tries & more than 0)")
    tries = input(">").upper()
    if tries.isdecimal():
        if int(tries) < 26 and int(tries) > 0:
            break

JS_list = list(JS_Word.strip())
u = list(JS_Word.strip())
Vic_Recon = ("_" *len(JS_list))
Vic_Recon = list(Vic_Recon.strip())
test = list(JS_Word.strip())
def alphred(x,life,li2):
    while True:
        if x not in li2:

            break
        elif x in li2:
            index = li2.index(x)
            life[index] = x
            li2[index] = '_'

print(f"Rules:\n1. If you fail in {tries} tries you will die\n2. If you guess boss's word/message you survive :)\nDon't die, . . .")
while True:
    z = Vic_Recon.count('_')
    print("small fish enter a letter")
    Vic_Le = input(">").upper()
    tries = int(tries)
    if ' ' in JS_list:
       Re = JS_list.index(" ")
       Vic_Recon[Re] = ' '
       alphred(' ',Vic_Recon,JS_list)
    if y.isalpha() == False:
       print("That isn't a letter, try again")
    elif z == 1 and Vic_Le in JS_list:
       Re = JS_list.index(Vic_Le)
       Vic_Recon[Re] = Vic_Le
       alphred(Vic_Le,Vic_Recon,JS_list)
       res = str(Vic_Recon)[1:-1]
       re = res.replace("'","")
       s = re.replace(",","")
       print(s)
       print("CONGRADULATIONS the you survived :)!")
       print(LETTERS)
       break 
    elif tries == 1 and Vic_Le in JS_list:
       Re = JS_list.index(Vic_Le)
       Vic_Recon[Re] = Vic_Le
       alphred(Vic_Le,Vic_Recon,JS_list)
       tries = tries-1
       res = str(Vic_Recon)[1:-1]
       re = res.replace("'","")
       s = re.replace(",","")
       rep = str(u)[1:-1]
       r = rep.replace("'","")
       n = r.replace(",","")
       print(s)
       print(f"{tries} tries left")
       print(f"The word/message was: {n}")
       print("GAME OVER\nyou die :(")
       print(LETTERS)
       break
    elif tries == 1 and Vic_Le not in JS_list:
       tries = tries-1
       res = str(Vic_Recon)[1:-1]
       re = res.replace("'","")
       s = re.replace(",","")
       rep = str(u)[1:-1]
       r = rep.replace("'","")
       n = r.replace(",","")
       print(s)
       print(f"{tries} tries left")
       print("GAME OVER\nyou die :(")
       print(f"The word/message was: {n}")
       print(LETTERS)
       break
    elif len(Vic_Le) == 1 and Vic_Le in JS_list:
        Re = JS_list.index(Vic_Le)
        Vic_Recon[Re] = Vic_Le
        alphred(Vic_Le,Vic_Recon,JS_list)
        res = str(Vic_Recon)[1:-1]
        re = res.replace("'","")
        s = re.replace(",","")
        L = LETTERS.replace(Vic_Le, ' ')
        LETTERS = L
        print(s)
        print(f"GUES SUCCESFUL\n{tries} tries left")
        print(L)
        tries = tries - 1
    elif Vic_Le not in JS_list:
        L = LETTERS.replace(Vic_Le, ' ')
        LETTERS = L
        res = str(Vic_Recon)[1:-1]
        re = res.replace("'","")
        s = re.replace(",","")
        print(s)
        print(f"GUESS INCORRECT\n{tries} tries left")
        print(LETTERS)
        tries = tries - 1