name_file = open('/etc/passwd', 'r')
contents = name_file.read()
name_file.close()

c2 = contents.split('\n')[:-1]

temp1 = map(lambda x: x.split(':'), c2)
what = lambda x: (x[0], x[2])
[what(x) for x in temp1]
print(temp1[1])
print(what(temp1[1]))

[x[0] for x in temp1]

print([len(x) for x in temp1])
print(temp1[-1])

# print xf[3]
