# Ceasar Cipher Crack
# Author Brandon Zazza

import Cipher as Ci
import csv

def crack_text(cipher):
    words = cipher.split(" ")
    for i in range(len(words)):
        if len(words[i]) == 5:
            file_read("fiv_lw.txt", words[i])
        elif len(words[i]) == 4:
            file_read("fur_lw.txt", words[i])
        elif len(words[i]) == 3:
            file_read("tre_lw.txt", words[i])
        else:
            print("Not Found")

def file_read(filename, ciph_word):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for record in csv_reader: 
            for i in range(26):
                check = Ci.text_change(i, ciph_word)
                if record[0] == check:
                    print('Found word' , '"'+record[0]+'"', 'after', i, "permutations")
                    return
    print("Error Computing") 


crack_text("fdqqe mdq sdqqz")



        