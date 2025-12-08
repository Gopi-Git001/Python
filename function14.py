# def myfunc(word1,word2):
#         return True if word1[0].upper()==word2[0].upper() else False


# print(myfunc('Levelheaded','Llama'))


def myfunc(word):
    
    return True if list(word)[0][0].upper()==list(word)[1][0] else False

print(myfunc('Crazy Kangaroo'))