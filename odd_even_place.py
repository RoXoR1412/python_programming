#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    s=sentence.split()
    i=0
    for i in range(len(s)):
        if i%2==0:
            s[i]=s[i][::-1]
        elif i%2!=0:
            #print("in second loop"            )
            vowel=set("aeiou")
            t = ""
            t2 = ""
            for j in s[i]:
                if (j in vowel):
                    t2 = t2 + j
                else:
                    t = t + j
            t = t + t2
            s[i] = t

    s="  ".join(s)
    return s
    #start writing your code here

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)