PLACEHOLER = "[name]"
with open('./Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()
    print(names)

with open('./Input/Letters/starting_letter.txt') as letter_files:
    letter_content = letter_files.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLER, striped_name)
        print(new_letter)
        with open(f'./Output/ReadyToSend/letter_for_{striped_name}.txt', mode="w") as completed_letter:
            completed_letter.write(new_letter)

