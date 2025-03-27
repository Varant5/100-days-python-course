#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "r") as f:
    context = f.read()
    with open("Input/Names/invited_names.txt", "r") as n:
        for line in n:
            line = line.strip()
            with open(f"Output/ReadyToSend/letter_to_{line}.txt", "w") as end:
                change_context = context.replace("[name]", line)
                end.write(change_context)