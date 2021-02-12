MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

LOGO = """                                                                          
,--.   ,--.                                                ,--.           
|   `.'   | ,---. ,--.--. ,---.  ,---.      ,---. ,---.  ,-|  | ,---.     
|  |'.'|  || .-. ||  .--'(  .-' | .-. :    | .--'| .-. |' .-. || .-. :    
|  |   |  |' '-' '|  |   .-'  `)\   --.    \ `--.' '-' '\ `-' |\   --.    
`--'   `--' `---' `--'   `----'  `----'     `---' `---'  `---'  `----'    
 ,-----.                                       ,--.                       
'  .--./ ,---. ,--,--,,--.  ,--.,---. ,--.--.,-'  '-. ,---. ,--.--.       
|  |    | .-. ||      \\  `'  /| .-. :|  .--''-.  .-'| .-. :|  .--'       
'  '--'\' '-' '|  ||  | \    / \   --.|  |     |  |  \   --.|  |          
 `-----' `---' `--''--'  `--'   `----'`--'     `--'   `----'`--'          
                                                                          """


def split(sentence):
    if " " in sentence:
        return sentence.split()
    else:
        return [sentence]


def translate(word):
    word_list = list(word)
    output = []
    for char in word_list:
        try:
            output.append(MORSE_CODE_DICT[char.capitalize()])
        except KeyError:
            print(f"I'm sorry, I cannot translate the character '{char}'")
    translation = ""
    return translation.join(output)


keep_going = True
print(LOGO)

while keep_going:
    string = input('What do you want me to translate into morse code? ')
    for word in split(string):
        print(f"{translate(word)} ", end="")
    answer = input("\n\nDo you have more sentences to translate? [y/n] ")
    if answer.lower() != "y":
        print("Thanks for using my Morse code translator. See you soon!")
        keep_going = False
