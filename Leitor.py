arq = open("Texto.txt", "r")
linha = arq.readlines()

for i in linha:
    print(i)
arq.close()