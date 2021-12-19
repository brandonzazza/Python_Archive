# Caesar Cipher v1
# Author Brandon Zazza

""" Hard Coded Dictionary
letter_dict = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"j",10:"k",11:"l",12:"m",
13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
"""

def dictionary_gen(letter_list):
    dict_return = {}
    for i in range(len(letter_list)):
        key = i+1
        dict_return[key] = letter_list[i]
    return dict_return

def text_change(n,message):
    message = list(message)
    output_list = []
    for i in range(len(message)):
        key = GetKey(message[i])
        if type(key) == type(int()):
            if key + n > len(letter_dict):
                key = key+n-26
            else:
                key = n+key
                output_list.append(letter_dict[key])
        else:
            output_list.append(" ")
    return "".join(output_list)

def GetKey(val):
    for key, value in letter_dict.items():
        if val == value:
            return(key)

letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter_dict = dictionary_gen(letter_list)

    
def main():
    message = "khoor zruog lwv ph eudqgrq"
    print(text_change(-3,message))


main()