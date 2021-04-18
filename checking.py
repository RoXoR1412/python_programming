#lex_auth_012693816331657216161

def encode(message):
    message=message+"0"
    s=""
    count=0
    for i in range(1,len(message)):
        if message[i-1]==message[i]:
                count+=1
        elif message[i-1]!=message[i]:
            count=count+1
            s=s+str(count)+message[i-1]
            count=0

            # print(count)
        #print(chr(a))

    return s

    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)