import math
import random

#Numbers
print(123+222)
print(1.5 * 4)
print(2 ** 100)
print(3.1415 * 2)
print(math.pi)
print(math.sqrt(54))
print(random.choice([1, 9 , 6]))
#String
S = "Spam"
print(len(S))
print(S[0])
print(S[len(S)-1])
print(S[1:3])
S = 'z' + S[1:]
print(S)
print(S.find("pa"))
print(S.replace('pa', 'XYZ'))
line = 'aaa,bbb,ccc,dd'
print(line.split(','))
print(S.upper())
print(S.isalpha())
print(line.rstrip())