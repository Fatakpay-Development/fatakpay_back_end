lst = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]
new = []
s = ""
c = 0
for i in lst:
    if i == 0:
        s = s + str(i)
    else:
        if s == "":
            pass
        else:
            new.append(s)
            s = ""
if s:
    new.append(s)
print(new)
for k in range(len(new)):
    if k == len(new) - 1:
        if len(new[k]) >= 2:
            c = c + 1
        else:
            pass
    elif len(new[k]) >= 2 and k < (len(new) - 1):
        c = c + 2
    elif len(new[k]) == 1:
        c = c + 1
print(c)
