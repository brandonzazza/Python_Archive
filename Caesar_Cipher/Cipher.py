# Caesar Cipher v1
# Author Brandon Zazza

letter_dict = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"j",10:"k",11:"l",12:"m",
13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

def text_change(n,message):
    message = list(message)
    output_list = []
    for i in range(len(message)):
        key = GetKey(message[i])
        if key + n > len(letter_dict):
            key = key+n - 25
        else:
            key = n+key
        output_list.append(letter_dict[key])
    return "".join(output_list)



def GetKey(val):
   for key, value in letter_dict.items():
      if val == value:
        return(key)
        
     




message = "z"

print(text_change(1,message))
