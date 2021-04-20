#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0
    thisdict={}
    c=0
    length=0
    s=data.split()
    for a in s:
        for i in range(len(s)):
            if a==s[i]:
                c=c+1
        thisdict[a]=c
        c=0
    #print(thisdict)
    for value in thisdict:
        if thisdict[value]>frequency:
            frequency=thisdict[value]
            word=value
            length=len(value)
        elif thisdict[value]==frequency:
            if len(value)>length:
                word=value
                length=len(value)
                frequency=thisdict[value]


    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,frequency)


#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)