from time import sleep
import random
class Morse:

    M_dict = {
        'A':'.-','B':'-...','C':'-.-.',
        'D':'-..', 'E':'.','F':'..-.',
        'G':'--.', 'H':'....','I':'..',
        'J':'.---', 'K':'-.-','L':'.-..',
        'M':'--', 'N':'-.','O':'---',
        'P':'.--.', 'Q':'--.-','R':'.-.',
        'S':'...', 'T':'-','U':'..-',
        'V':'...-', 'W':'.--','X':'-..-',
        'Y':'-.--', 'Z':'--..','1':'.----',
        '2':'..---', '3':'...--','4':'....-',
        '5':'.....', '6':'-....','7':'--...',
        '8':'---..', '9':'----.','0':'-----',
        
        ',':'--..--', '.':'.-.-.-','?':'..--..',
        '/':'-..-.', '-':'-....-','(':'-.--.',
        ')':'-.--.-','&':'.-...', ':':'---...', 
        ';':'-.-.-.','=':'-...-', '+':'.-.-.', 
        '-':'-....-','_':'..--.-', '"':'.-..-.',
        '@':'.--.-.',   
        
        ' ': '/',   ' ': '|', #for space
    }

    Key_list = list(M_dict.keys())
    Val_list = list(M_dict.values())

    enc_mes = ""
    inc = 6

    def __init__(self,letter):
        self.letter = letter  
        global let_list_1 ; global let_list_2
        let_list_1 = list(self.letter) ; let_list_2 = list(self.letter.split(" "))

    def Encrypt(self):
        i = 0 ; n = len(let_list_1)
        for i in range(0,n):
            cnt = (let_list_1[i]).upper()
            find = Morse.Key_list.index(cnt)
            Mor = Morse.Val_list[int(find)]," "
            i+=1
            Mor = str(Mor[0])
            Morse.enc_mes += Mor+" "
        print(Morse.enc_mes) 

    def Decrypt(self):
        i = 0 ; n = len(let_list_2)
        for i in range(0,n):
            cnt = let_list_2[i]
            find = Morse.Val_list.index(cnt)
            Mor = Morse.Key_list[int(find)]
            i+=1
            Morse.enc_mes += str(Mor[0])
        print(Morse.enc_mes.lower()) 

def intro():
    global sec ; sec = .6
    print("loading"),(sleep(sec),print(".")),(sleep(sec),print(".")),(sleep(sec),print("."))
    print("indexing dictionary"),(sleep(sec),print(".")),(sleep(sec),print(".")),(sleep(sec),print("."))
    print("Done!!\n\n")

    print("~"*50+" MORSE TRANSLATOR v0.02a "+"~"*51)
    print(" "*113+" -by abhishek")

    print("\n1) Encrypting a message[A => .-]  \n2) Decrypting a message[.- => A] \n3) Exit ")

intro()    

def exit_():
    print("\nThank you for using.....")
    rand1 = random.randint(3,10)
    rand2 = random.randint(0,43)
    print(f"clearing cache {rand1}/{rand2}"),(sleep(sec),print(".")),(sleep(sec),print(".")),(sleep(sec),print("."))
    print("almost there"),(sleep(sec),print(".")),(sleep(sec),print(".")),(sleep(sec),print("."))
    print("Done!!\n\n")
    exit()
wait = False

while wait is not True:
    try:
        select = int(input("\nYour selection: "))
        if select == 3:
                exit_()
        while True:
            U_input = input("\nYour message : ")
            p = Morse(U_input) ; Morse.enc_mes = ""
            if  U_input == "ex()":
                exit_()
            elif U_input == "list()":
                print("\n-----Valid input list-----\n")
                for key,value in Morse.M_dict.items():
                    print('" " => / or |') if key == " " else print(key,' => ',value)
            elif U_input == "back()": print("\n\tJust a sec"),(sleep(1));break
            elif select == 1:
                p.Encrypt()
            elif select == 2:
                p.Decrypt()
            else:
                print("Invalid selection!!")
    except ValueError as e:
        print("Input is'nt valid!!")
    except KeyboardInterrupt as ki:
        print("\n{{..Only Alpha-num and symbols can be entered..}}")
