import re
import reprlib
n = 0
i = 1
t = 0
re = re.compile('')

class plvr:

    def __init__(self, text):
        self.text = text
        self.words = re.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'plvr(%s)' %reprlib.repr(self.text)

def tent():
    if b in palavra[k]:
        for i in range(len(palavram)):
            if b in palavra[i - 1] and b != palavram[i - 1]:
                palavram[i-1] = b
                print(palavram)
            i += 1
    else:
        print('A palavra não contem %s' %(b))




c = int(input('Quantas palavras vão pra forca?'))

palavra = [[]for z in range(c)]

palavram = [[] for z in range(c)]


print(palavra)
for y in range(c):
    a = plvr(input('Qual palavra vai pra forca? '))
    for x in a.text:
        palavra[y].append(x)
        n+=1
        print(x)
    for g in palavra[y]:
        palavram[y].append('_')
        print(palavram)
        print(palavra)




for k in range(len(palavram) + 3):
    b = str(input('Advinhe uma letra: '))
    l = int(input('Qual o numero da palavra que deseja adivinhar? Existem %d palavras' %(len(palavra))))

    if b in palavra[l]:
        for i in range(len(palavram[l])):
            if b in palavra[l][i - 1] and b != palavram[l][i - 1]:
                palavram[l][i - 1] = b
                print(palavram[l])
            i += 1
    else:
        print('A palavra não contem %s' % (b))


    if '_' not in palavram[l]:
        print('Boa Tanso!!')
        break