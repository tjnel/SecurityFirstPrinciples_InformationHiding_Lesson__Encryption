# Security First Principles - Information Hiding
## Exploring Encryption Lab -- ANSWERS --


### Lab Exercise 1 - De-Cipher this
For this exercise we will be exploring various methods to hide information in text. There are many different cipher types each vary in diffficulty to solve and information needed to decode. For each message I will provide you with the cipher type for you to look up and and solve. Submit the solved messages for credit.

#### Morris Code
```
FIRST ONE IS EASY
```
#### Bacon
```
NUMBERTWODONENOWWEARECOOKING
```
#### ROT13
```
third time is a charm
```
#### Vigenere
```
this is number four
```
#### Playfair Cipher
```
HIGHFIVEYOUAREDONE
```

A good resource for this is www.dcode.fr

### Lab Exercise 2 - PGP and Me
#### PGP Part 1
shoud look something like the public key below
```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: BCPG C# v1.6.1.0

mQENBFv630YBCACsOQSVz+GL41f4e/fXNt0CeBRLAB+vOZbre+VRa3Dl7cdsbDOR
ScqNwDYsfoLBt2CGdmkkWwWh4f8dGeL540bK8ltbcRsfA95H2KK4qaGLDL6HY65y
Ubb++oxoXtJ75wllE83CNRpCcBd3mzqM2ITBdUZ4evN5Ukc0ihXG7szBHEl+9F1k
MCtaD7LnGwiihV4fNSQ3wphkPwYEAAMcuWpSX8YGi1koVXVBHJ0/y/KqdnONwPj9
jUgxqkzlBYLDrn6j2yrcjSZ4sT0+mRfTTjWrPtxomRHTbKdBWJq5cpDBo9CgPtQh
WMBFBBz5FSEuvTBuRp+8oeMs6uAajEotCuLFABEBAAG0E2V4YW1wbGVAZXhhbXBs
ZS5jb22JARwEEAECAAYFAlv630YACgkQ0LMjYPKskjfInQgAmjpBqiKC3GG1ZuJ/
FUtQp5ETMGo5ZIoaIhZk2lMxTFDlA/M7ALZAamCSo3q48CKFM1cVGyhixhqn6KlX
3y89TGSRunbGNEsba1bE8y/7fusTqIP+3P0FeTFdP9XoaKjAXKSogDxYCLltoGXM
DsHpdkkASUGROolJ33/JfVoDy+8v0W6+vm5CjT/YUUO/vWLvGSxo7HuPAr9fmGOa
02NYiZDETSI6b5oocm6r+PZMopHX4npf07QEpCnCngjf6sjKDlNwEGWuA7yiBijs
JD/NsjLfFGZx086W5h4WE99C3us8Nah85mNkQhF40LHe3gowLgSim+mrThHsj/pI
YPkxvg==
=xUXB
-----END PGP PUBLIC KEY BLOCK-----
```

#### PGP Part 2
Message for example@example.com
```
example name
PGP is for me
```

### Lab Exercise 3 - Breaking Ceasar
The answer is ROT-23:
```
you came, you saw, you conquered.
```
An example python script for this answer is below:
```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def main():
    encrypted = input("What is the Ceasar message you are trying to bruteforce: ")
    for shift in range(26):
        print("ROT {}: ".format(shift), end='')
        for letter in encrypted:
            print(alphabet[(alphabet.index(letter) - shift) % 26], end='')
        print("")

if __name__ == "__main__":
    main()
```