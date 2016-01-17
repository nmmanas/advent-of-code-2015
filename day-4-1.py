import hashlib
m = hashlib.md5()

input = 'ckczppom'

digit = 1

while True:

    new_input = input+str(digit)
    m1 = hashlib.md5(new_input.encode()).hexdigest()

    chck = m1[:5]

    if chck=='00000':
        break
    digit += 1


print digit
