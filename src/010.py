'''
http://www.pythonchallenge.com/pc/return/bull.html

a = [1, 11, 21, 1211, 111221,
len(a[30]) = ?
'''

def f(x):
    if x == 0: return "1"
    count = 0
    current = ""
    result = ""
    prev = f(x-1)
    for char in prev:
        if current == "":
            current = char
            count = 1
        elif current == char:
            count += 1
        else:
            result += str(count)
            result += current
            count = 1
            current = char
    result += str(count) + char
    return result

for i in range(7):
    print f(i)
print len(f(30))