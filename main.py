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

results = [morse_code[strings.index(let)] for let in string if let in string]
print(results, end="")
