# Ceasar Cipher Crack
# Author Brandon Zazza

import Cipher as Ci
import csv

def crack_text(cipher):
    words = cipher.split(" ")
    for i in range(len(words)):
        if len(words[i]) == 5:
            file_read("Caesar_Cipher/flw.txt", words[i])
        else:
            print("Not Found")

def file_read(filename, ciph_word):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in range(len(Ci.letter_list)):
            print(i)
            check = Ci.text_change(i, ciph_word)
            for record in csv_reader:
                if record[0] == check:
                    print('Found' , record[0], 'after', i, "permeitations")
                    return 
                    


crack_text("water")



        