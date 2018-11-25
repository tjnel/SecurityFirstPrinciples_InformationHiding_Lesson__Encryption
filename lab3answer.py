# This is the solution to Applied Information Hiding Through Basic Encryption
# CSC840 - Security First principles Information Hiding
# By TJ Nel

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