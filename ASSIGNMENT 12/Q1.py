# Write a program which accepts one character and checks whether it is vowel or consonant
# INNPUT : a
# OUTPUT : VOWEL


def CheckingVowelorConsonant(char):
    char = char.lower()
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        return "It's a vowel"
    elif (char >= "a" and char <= "z"):
        return "It's a consonant"
    else:
        return "Invalid character"
   

def main():
    char = input("Enter a character :")

    Ret = CheckingVowelorConsonant(char)

    print("Character",char,"is a :",Ret)

if __name__ == "__main__":
    main()