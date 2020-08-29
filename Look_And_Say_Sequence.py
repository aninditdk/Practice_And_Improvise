import re
s = '1'
i = '1'
str1 = ''
n = int(input())
def look_say_sequence(s):
    global i
    global str1
    match = re.match("%s+" % i, s)
    str1 += str(len(match.group(0))) + i
    s = s[len(match.group(0)):]
    if len(s)==0:
        return str1
    i = s[0]
    return look_say_sequence(s)
if n==1:
    print(1)
else:
    for j in range(n-1):
        a = look_say_sequence(s)
        s = a
        i = s[0]
        str1=''
    print(a)
