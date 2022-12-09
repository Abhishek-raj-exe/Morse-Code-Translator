from time import sleep ; import random ;import warnings ; warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd ; import re

class Morse:

    global dict  
    dict = pd.DataFrame({
        "Sr":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],

        "Word":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'                           #alphas
                , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                , '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',                                       #numbers
                ',', '.','?','/', '-', '(', ')', '&', ':', ';', '=', '+', '_', "'",'"', '!' , '@', ' '],  #symbols

        "Morse":['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.' , '...', '-', 
                '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '--..--',
                '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '..--.-', '.----.', ".-..-.", '-.-.--', '.--.-.', '|']
    })

    url = "https://raw.githubusercontent.com/Abhishek-raj-exe/Morse-Code-Translator/Development/Data_Morse.csv" 
    dict = pd.read_csv(url,error_bad_lines=False,delim_whitespace=True)  # Run these in case the file gets corrupted  #dict.set_index('Sr', inplace = True); dict.to_csv("Data_Morse.csv",sep="\t",index =True,header=True).

    enc_mes = ''

    def __init__(self,letters):
        self.letters = letters
        self.dict = dict

        global let_list_1 ; global let_list_2 ; global Mr_str; global Wrd_str        
        let_list_1 = list(self.letters) ; let_list_2 = list(self.letters.split(" "))
        Mr_str = (dict["Morse"].tolist())
        Wrd_str = "".join(self.dict["Word"].tolist())        

    def Encrypt(self):        
        i = 0 ; n = len(let_list_1)
        for i in range(0,n):
            cnt = (let_list_1[i]).upper()
            Mor = Mr_str[(re.search(cnt,Wrd_str).span())[1]-1]
            i+=1
            Morse.enc_mes += Mor+" "
        print(Morse.enc_mes)

    def Decrypt(self):
        i = 0 ; n = len(let_list_2)
        for i in range(0,n):
            cnt = let_list_2[i];cz = 0
            for ml in Mr_str:
                if ml == cnt:break
                cz += 1
            i+=1;Morse.enc_mes += Wrd_str[cz]
        print(Morse.enc_mes.lower())

def intro():
    global sec ; sec = .6
    print("loading"),(sleep(sec),print(".")),(sleep(sec),print(".")),(sleep(sec),print("."))
    print("indexing dictionary"),(sleep(sec),print(".")),(sleep(sec),print(".")),(sleep(sec),print("."))
    print("Done!!\n\n")
    print("~"*50+" MORSE TRANSLATOR v0.05a "+"~"*51)
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

wait,ex = False,False
while wait is not True:
    try:
        while ex == False:
                select = int(input("\nYour selection: "))
                if select == 3:
                        ex=True;exit_()
                elif 3 < select or select < 0:
                    print("Invalid selection!!"); continue ; ex=False  
                while True:
                    U_input = input("\nYour message : ")    #..Only Alpha-num and symbols can be entered..
                    p = Morse(U_input) ; Morse.enc_mes = ""
                    if  U_input == "ex()":
                        exit_()
                    elif U_input == "list()":
                        print("\n-----Valid input list-----\n")
                        for i in range(1,len(Mr_str)):
                            l1,l2 = dict["Morse"][i], dict["Word"][i]
                            l1c = 6-len(l1)
                            print(f'{l1+(" "*l1c)}   <==>\t {dict["Word"][i]}\n');i+=1
                    elif U_input == "back()": print("\n\tJust a sec"),(sleep(1));break
                    elif select == 1:
                        p.Encrypt() ; ex=False  
                    elif select == 2:
                        p.Decrypt() ; ex=False  
    except(ValueError,IndexError,AttributeError,KeyboardInterrupt,TypeError) as e:
        print("Input is'nt valid!!")
