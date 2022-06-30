with open("./Input/Names/invited_names.txt") as name_file:
    names_list = name_file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

for name in names_list:
    new_letter = letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
        new_file.write(new_letter)
