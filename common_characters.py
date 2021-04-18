#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    msg1=set(msg1)
    msg2=set(msg2)
    s=msg1 & msg2
    st=""
    for a in s:
        if a!=' ':
            st=st+str(a)
    if s=="":
        return -1
    
    return st

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)