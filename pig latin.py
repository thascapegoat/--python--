data = input('enter word(s) to be translated to pig latin: ')
data_a = data.split(' ')
print('')
for i in data_a:   
    a = i[0:1]
    i=i[1:]
    print(i+a+'ay', end=' ')
