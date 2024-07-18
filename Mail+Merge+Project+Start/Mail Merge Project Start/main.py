#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#
with open("./Input/Letters/starting_letter.txt") as file:
    line = file.read()

with open("./Input/Names/invited_names.txt") as invited:
    name_list = invited.readlines()

for name in name_list:
    invited_name = name.strip()
    new_line = line.replace("Dear [name]", f"Dear {invited_name}")
    with open(f"./Output/ReadyToSend/letter_for_{invited_name}.txt", "w") as invited_letter:
        invited_letter.write(new_line)

