#Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as
# SMS and returns the abbreviated sentence.
# Rules are as follows:
#a. Spaces are to be retained as is
#b. Each word should be encoded separately

#If a word has only vowels then retain the word as is

#If a word has a consonant (at least 1) then retain only those consonants

#Note: Assume that the sentence would begin with a word and there will be only a single space between the words.


#lex_auth_01269444961482342489

def sms_encoding(data):
    s2=s=s1=s3=""
    coun=0
    data=data + " "
    #start writing your code here
    vowel=set("aeiouAEIOU")
    for a in data:
        if a==" ":
            for b in s:
                if (b in vowel):
                    s1=s1+b
                else:
                    s1=s1+b
                    coun+=1

            if coun>=1:
                for c in s1:
                    if (c in vowel):
                        continue
                    else:
                        s2=s2+c

                s3=s3+s2+" "
            else:
                for c in s1:
                    s2=s2+c
                s3=s3+s2+" "
            s=""
            coun=0
            s2=s1=""
        else:
            s=s+a
    return s3.rstrip( )






data="I love Python"
print(sms_encoding(data))