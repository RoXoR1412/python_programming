#lex_auth_012693816331657216161

def encode(message):
    s=""
    count=0
    for a in range(ord('A'),ord('Z')+1):
        for i in range(0,len(message)):
            if chr(a)==message[i]:
                count+=1
        if count>0:
            s=s+str(count)+chr(a)
       # print(count)
        #print(chr(a))
        count=0
    return s

    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)