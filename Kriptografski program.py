import random
import string
import getpass
def enkript():
    inputsifra1 = getpass.getpass("Sifra: ")
    sifra1 = ("asb5352")
    if sifra1 == inputsifra1:
        encrypt = input("Ukucajte recenicu za encrypt: ")
        def add_str(lst):
            _letters = ("1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","!","#","$","%","&","/","(",")","=","?","*","+","_","-",";"," ")
            return [''.join(random.sample(set(_letters), 2)) + letter + ''.join(random.sample(set(_letters), 2))for letter in lst]

        print(''.join(add_str(encrypt)))
        input("")
    else:
        print("Pogresna sifra")
        input("")
def generate():
    passwdinput2 = getpass.getpass("Sifra: ")
    passwd2 = ("asb5352")
    if passwdinput2 == passwd2:
        karakteri=("1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","!","#","$","%","&","/","(",")","=","?","*","+","_","-",";")
        user_input=input("Koliko karaktera zelite?(min6-max15) ")
        if user_input == "6":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "7":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "8":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "9":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "10":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "11":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "12":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "13":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "14":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        elif user_input == "15":
            print(random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri)+ random.choice(karakteri))
        else:
            print("Greska")
            input("")
    else:
        print("Pogresna sifra")
        input("")
def dekript():
    passwdinput = getpass.getpass("Sifra: ")
    passwd = ("asb5352")
    if passwd == passwdinput:
        s = input("Ukucajte recenicu za decrypt: ")
        print(s[2::5])
        input("")
print("Dobrodosli u Kriptografski program!")
pocetak = input("Izaberite:Encrypt(e),Decrypt(d),Stvori Sifru(s): ")
if pocetak == ("e"):
    enkript()
elif pocetak == ("d"):
    dekript()
elif pocetak == ("s"):
    generate()
    input("")
else:
    print("Greska")
    input("")



        


        
        
                      
    




