# Morse-Code-Translator
 A morse code translator made using python classes

# About Project:

The program translates alpha-numerical letters and sentences to morse code
Few special char are also supported , spaces are represented by "/" for simplicity purposes

Classes were implemented for practice n learning purpose

.
.
.
The code was possible with references to https://www.geeksforgeeks.org/morse-code-translator-python/ & https://morsecode.world/

# Run

```
Your selection: "selection fm 1-3"
Your message: "Message to be en/decrypted"
```
1) For encryption enter the message alpha-num... [ check for supported symbols list `list()` ]
eg:

```input (will be converted 2 lowercase for translation)```
```
Your message: Who.. me?
```
```output```
```
.-- .... --- .-.-.- .-.-.- / -- . ..--..
```

2) For decryption enter the message in morse...(enter every letter with space " " & a word space as "/")
eg:

```input```
```
Your message: .. -- / .--- ..- ... - / .- / --. ..- -.-- / .-- .... --- ... / .... . .-. --- / ..-. --- .-. / ..-. ..- -. .-.-.- .-.-.- .-.-.- .-.-.- 
```
```output (will always be in lowercase)```
```
im just a guy whos hero for fun....
```

```The message loop can be broken by `back()` as input &takes back to selection menu or `ex()` to directly exit from loop...`list()` shows the list supported letters & symbols```

Note: the intro/outro execution can be disabled by commenting out [exit_() on line 82 and 87 & intro on line 66] for quick translation

