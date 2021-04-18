#lex_auth_012693819159732224162

def check_palindrome(word):
    s=""
    for a in word:
        s=a+s
    if word==s:
        return True
    else:
        return False
    #Remove pass and write your logic here
status=False
status=check_palindrome("mango")
print(status)
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")