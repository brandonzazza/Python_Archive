# Caesar Cipher v1
# Author Brandon Zazza

#""" Hard Coded Dictionary
letter_dict = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",
14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
#"""

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
                output_list.append(letter_dict[key])
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

#letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#letter_dict = dictionary_gen(letter_list)

def main():
    message = "trees are green"
    print(text_change(12,message))

if __name__ == "__main__": 
    main()