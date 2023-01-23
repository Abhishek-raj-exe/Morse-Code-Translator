# Morse-Code-Translator
 A morse code translator made using pyside6.

# About Project:

The program translates alpha-numerical letters and sentences to morse code.
Few special char are also supported , spaces will be represented by "|" in morse.

Orignally written in PyQt6,5 rewritten in Pyside6 for LPGL
.
.
.
The code was possible with references to https://www.geeksforgeeks.org/morse-code-translator-python/ & https://morsecode.world/ , https://pythonguis.com

# Run

```
Your message: "Message to be en/decrypted"
```
1) For encryption enter the message alpha-num... [ check for supported symbols list `list()` ]
eg:

!alt (url:https://github.com/Abhishek-raj-exe/Morse-Code-Translator/blob/Development/Images/Morse%20SS.jpg)

2) For decryption enter the message in morse...(enter every letter with space " " & a word space as "/" or "|")
eg:

input
```
Your message: .. -- / .--- ..- ... - / .- / --. ..- -.-- / .-- .... --- ... / .... . .-. --- / ..-. --- .-. / ..-. ..- -. .-.-.- .-.-.- .-.-.- .-.-.- 
```
output (will always be in lowercased)
```
im just a guy whos hero for fun....
```

The message loop can be broken by `back()` as input &takes back to selection menu or `ex()` to directly exit from loop...`list()` shows the list supported letters & symbols

Note: the intro/outro execution can be disabled by commenting out [exit_() on line 82 and 87 & intro on line 66] for quick translation
