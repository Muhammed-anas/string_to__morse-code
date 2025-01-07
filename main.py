name = input("Name: ")
print(f"Hello,{name} Welcome to the translator game")
print("Here you can translate string to morse code")

strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?']

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
              ".---", "-.-", ".-..", "--", "-.", "---", ".---.", "--.-", ".-.",
              "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----",
              "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.",
              "-----", "--..--", ".-.-.-", "..--.."]

string = input("Enter the strings: ").lower()
print(f"The string are you entered is {string}")
print(f"The morse code is: ")

word = [letter for letter in string]

for let in word:
    if let in string:
        index = strings.index(let)
        result = morse_code[index]
        print(result, end="")

# for let in word:
#     if let in string:
#         index = strings.index(let)
#         result = morse_code[index]
#         print(result, end="")
