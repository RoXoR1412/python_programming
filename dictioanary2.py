#lex_auth_01269444890062848087

def find_correct(word_dict):
    c1,c2,c3,c=0,0,0,0
    for word in word_dict:
        if word_dict[word]==word:
            c1=c1+1
        elif len(word_dict[word])!=len(word):
            c3=c3+1
        else:
            x=word_dict[word]
            for a in range(len(word)):
                if x[a]!=word[a]:
                    c=c+1
            if c<=2:
                c2+=1
            else:
                c3+=1
            c=0
    list=[c1,c2,c3]
    return list
    #start writing your code here

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))