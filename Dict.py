# Dictionary in Map

x={'key':4}

x['key2']=5

print(x)


# list of keys

y=[];

y.append(x)

print(y)

# deleted Dic

del x['key']

print(x)


for key, value in x.items():
    print(key, value)
