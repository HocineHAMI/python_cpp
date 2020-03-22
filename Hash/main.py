import sha3

def printElemHash(elem):
    print("\"",elem,"\"", " => ","\"", sha3.hash(elem),"\"")

#Utilisation des anciens chaines de caracteres pour s'assurer des outputs 
testList=["","a","abc","message digest","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789","12345678901234567890123456789012345678901234567890123456789012345678901234567890""The quick brown fox jumps over the lazy dog"]

for elemStr in testList :
    printElemHash(elemStr)


