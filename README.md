# Morse-Code-Translator
 A morse code translator made using pyside6.
 [Download app](https://github.com/Abhishek-raj-exe/Morse-Code-Translator/releases/download/application/Morse-Translator.v1.5-setup.exe)

# About Project:

The program translates alpha-numerical letters and sentences to morse code.
Few special char are also supported , spaces will be represented by "|" in morse.
-
Orignally written in PyQt6,5 rewritten in Pyside6 for LPGL
.
.
The code was possible with references to https://morsecode.world/ , https://pythonguis.com



# Run
1) For encryption enter the message alpha-num... [ check for supported symbols list ]

![Screenshot](https://github.com/Abhishek-raj-exe/Morse-Code-Translator/blob/Development/Images/Morse%20SS.jpg)

2) For decryption enter the message in morse...(enter every letter with space " " & a word space as "/" or "|")
input
```
Your message: .. -- / .--- ..- ... - / .- / --. ..- -.-- / .-- .... --- ... / .... . .-. --- / ..-. --- .-. / ..-. ..- -. .-.-.- .-.-.- .-.-.- .-.-.- 
```
output will be lowercased
```
im just a guy whos hero for fun....
```


Note: window wont be visible in taskbar ,toggle with "alt-tab" and hit close or kill with taskmanager

# Support List
-----Valid input list-----
```
A    =>   .-
B    =>   -...
C    =>   -.-.
D    =>   -..
E    =>   .
F    =>   ..-.
G    =>   --.
H    =>   ....
I    =>   ..
J    =>   .---
K    =>   -.-
L    =>   .-..
M    =>   --
N    =>   -.
O    =>   ---
P    =>   .--.
Q    =>   --.-
R    =>   .-.
S    =>   ...
T    =>   -
U    =>   ..-
V    =>   ...-
W    =>   .--
X    =>   -..-
Y    =>   -.--
Z    =>   --..
1    =>   .----
2    =>   ..---
3    =>   ...--
4    =>   ....-
5    =>   .....
6    =>   -....
7    =>   --...
8    =>   ---..
9    =>   ----.
0    =>   -----
,    =>   --..--
.    =>   .-.-.-
?    =>   ..--..
/    =>   -..-.
-    =>   -....-
(    =>   -.--.
)    =>   -.--.-
&    =>   .-...
:    =>   ---...
;    =>   -.-.-.
=    =>   -...-
+    =>   .-.-.
_    =>   ..--.-
"    =>   .-..-.
@    =>   .--.-.
" "  =>    |
'    =>   .----.
!    =>   -.-.--
$    =>   ...-..-
```

