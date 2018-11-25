# SECURITY FIRST PRINCIPLES
# Information Hiding
## Exploring Encryption Lab
### Lab Overview
This lab will explore various aspects of encryption starting with ciphers moving into PGP and following up with cryptoanalysis. Once complete the learner should have a basic understanding of the motives and implementations of various encryption schemes and how they are used.
### Lab Environment
Most of this lab can be done using online resources however the last exercise will need a computer with Python 2 or 3 installed in order to complete.
### Lab Files that are Needed:
No lab files needed

### Lab Exercise 1 - De-Cipher this
For this exercise we will be exploring various methods to hide information in text. There are many different cipher types each vary in diffficulty to solve and information needed to decode. For each message I will provide you with the cipher type for you to look up and and solve. Submit the solved messages for credit.

#### Morris Code
```
..-. .. .-. ... - / --- -. . / .. ... / . .- ... -.--
```
#### Bacon
```
ABBAABAABBABABBAAAABAABAABAAAABAABABABAAABBABAAABBABBABABBAAAABAAABBAAABBABBABAABABAAAABAAAAAAABAAAAAABAAAAABAABBABABBABABAABABAAAABBAAAABBA

hint: there are no spaces for this one
```
#### ROT13
```
guveq gvzr vf n punez
```
#### Vigenere
```
dlgc mq xyklip pssb

key = KEY
alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
#### Playfair Cipher
```
IKHIGKZADTQEUBITPC

hint: ⠒↤⠨↥⠢ ( or bruteforce)
grid = ABCDEFGHIKLMNOPQRSTUVWXYZ
```

### Lab Exercise 2 - PGP and Me
#### PGP Part 1 - Setting up PGP
For this portion of the lab you will learn about Pretty Good Privacy (PGP) encryption which is primarily used in email today. Review this short 2 minute video to learn about PGP https://youtu.be/4PZb0tkxuUk and generate your own pgp private a public keys.

**Note: If you have generated your keys online  it would be best to never use them for personal and sensitive matters.**

Once you have generate a private and public key submit your public key block with your write-up.

#### PGP Part 2 - Using PGP
For this part we will be using a some generated PGP information to decrypt a message sent to us. Decrypt this message using the provided private key and password:
```
-----BEGIN PGP MESSAGE-----
Version: BCPG C# v1.6.1.0

hQEMA9CzI2DyrJI3AQf9GARjOEjmaZA18oQ0Yhuo4F/HeXduLxTsTn1CnJeegIhc
xPXGHUuOpMlSPCLE8qoxdr+M/PXo/Gfmh4MXAc7lHhwLmRw0N2WXnBo4T1R3eMrJ
uxJizetAocCKKMqDrGNnfJlJr8nCZX1uRgjZD3VUw6DekMsMTbDceHLPw0LyWdAU
nqKwNpC6SHxsmejwTi5CP3LOZVm72Fo8gcNGUVp17o9j2uE1m7ffMu40lyAzwdUO
xu41wQsWfaNCASLqZqVeDLm+tRaBM9U/ZGJdvzq2wGoaPRv8cs6qiBjiYzrmTZ6d
hZf+mO8HpEpDh7IN15BwaNz6czMqRuodss/RaKc6x8k5dsqwiT7BFOpWro6+vdmU
SNrFB8NZK0cz/7VRCwWtCrtepPhSPiSnOAEsVXsGctOJXBLbo4+Y3j8g
=85k7
-----END PGP MESSAGE-----
```
Private Key example@example.com (Password: example)
```
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: BCPG C# v1.6.1.0

lQOsBFv630YBCACsOQSVz+GL41f4e/fXNt0CeBRLAB+vOZbre+VRa3Dl7cdsbDOR
ScqNwDYsfoLBt2CGdmkkWwWh4f8dGeL540bK8ltbcRsfA95H2KK4qaGLDL6HY65y
Ubb++oxoXtJ75wllE83CNRpCcBd3mzqM2ITBdUZ4evN5Ukc0ihXG7szBHEl+9F1k
MCtaD7LnGwiihV4fNSQ3wphkPwYEAAMcuWpSX8YGi1koVXVBHJ0/y/KqdnONwPj9
jUgxqkzlBYLDrn6j2yrcjSZ4sT0+mRfTTjWrPtxomRHTbKdBWJq5cpDBo9CgPtQh
WMBFBBz5FSEuvTBuRp+8oeMs6uAajEotCuLFABEBAAH/AwMCaOEMmtSSzdZgTwif
ICg5O2RgNt0vScxO/PbAPMEraCWmdMa3IkZwlExxAufA9QPgWLzMhZsMZ8rxVArE
OPsxCpXZdx276A1xHKFuZEnUx6I7AcW9bbwxm2a9pFvUC71G2IalsspM6+minwjw
YnFOXUoZEJRYJmUNUnQNTdUCEqMKrAQy3mg0UaGzxawWPtwwUGII5OBSWrj/adpQ
x0dp9iHPuijdD/KlGl6AIJGaZV/7HKFlqWUcYFCF80kPTxFlC0fDnHIwpuDTHKWH
ss0L76VlKHm/pnVRBJd5nBXZhWjp7BxLOcY3F1nDp0P93OMwDs376GgzRHep8rUj
qbK8Xgm5fsYmRDIKMGrjrNiyeWniLXxSL4OyRRd5IK/6jRNDtXTwBvp7Q5IE5Tzi
eP07IXiDP55y5cENMFAQ7NYW1WxBrQ0062QfpVknCEYj4vIBKSA9esQAuse5aOq6
h5OeXb8rkKSgCuzYQAmSmvmdveNFyNCvFQHqm6BGxF1XEb4O+MHYX65OypVzpUSQ
7kiS4rD2BdxKJMxtIKujyHBIc57NqWC3WsPJHOh7xQO5qmNVxyiqg7GOsKGXqsRe
eYHxVi8q8/+ScCAiy+tCNjfwvljNXe7MVRuBxGaWjOyTaRxKi/fPlFNFv48gP51k
H/kodUj7F5/IW2iP6mZVDeNJYpYypn3tGCNb/nmS8i2crkaeXZ5ZGqqD3fMiU5Fc
W3Gta/9mjbSRcRRhDq5Kmb03Qbbnr9qBociv9sj6ucUymoNJwODXgVVBEuX84kZ9
ZDYZXuQGR/zgTNpYZ0+vRHkAGhJV+xQLTEw2+BHWwrzApPxhJl+Xw2uxPZQ+ir8I
wXqTlEFgFvIjOlfglgp71K0fZQzxd3BdGxfRLmOVorQTZXhhbXBsZUBleGFtcGxl
LmNvbYkBHAQQAQIABgUCW/rfRgAKCRDQsyNg8qySN8idCACaOkGqIoLcYbVm4n8V
S1CnkRMwajlkihoiFmTaUzFMUOUD8zsAtkBqYJKjerjwIoUzVxUbKGLGGqfoqVff
Lz1MZJG6dsY0SxtrVsTzL/t+6xOog/7c/QV5MV0/1ehoqMBcpKiAPFgIuW2gZcwO
wel2SQBJQZE6iUnff8l9WgPL7y/Rbr6+bkKNP9hRQ7+9Yu8ZLGjse48Cv1+YY5rT
Y1iJkMRNIjpvmihybqv49kyikdfiel/TtASkKcKeCN/qyMoOU3AQZa4DvKIGKOwk
P82yMt8UZnHTzpbmHhYT30Le6zw1qHzmY2RCEXjQsd7eCjAuBKKb6atOEeyP+khg
+TG+
=EH0x
-----END PGP PRIVATE KEY BLOCK-----
```
Once you are able to decrypt this message submit the plain text message with your write up.

### Lab Exercise 3 - Breaking Ceasar
For this exercise we will be exploring how you can use cryptoanalysis to break cryptographic ciphers. The cipher we will be breaking is the Ceasar cipher, the was infact used by Julius Ceasar himself to communicate with his generals. This cipher is one ofg the earlist known and simplest ciphers, in fact it is the same as ROT cipher and all you need to solve it is know what number the alphabet is shifted by. However this is not nessesarily true, with 26 letters in the alphabet there is only 26 shift possibilities. That means you could bruteforce the cipher by decoding with all 26 shift amounts then looking for the message that appears to make sense.
Your Task is to create a python program that will display all of the possible decodings for the following ceaser cipher string:
```
vlrzxjbvlrpxtvlrzlknrboba
```
Once your script is working submit the answer, the ROT number and your script in the write up.

### What to Submit
Please submit listed items in one document with your name and title:
* Exercise 1 - All solved messages for each cipher
* Exercise 2 - Your generated PGP public key
* Exercise 2 - The decrypted PGP message
* Exercise 3 - The python script created to solve the cipher, the ROT shift number and the answer