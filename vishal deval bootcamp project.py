import hashlib
a=input('Enter any text to convert into md5 = ')
print(hashlib.md5(a.encode()).hexdigest())
