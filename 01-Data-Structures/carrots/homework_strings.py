""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta


import matplotlib.pyplot as plt
DNA = open("files/dna.fasta", "r")
contents = DNA.read()
DNA.close()

listDnaRead = contents.split("\n")
# делим на 2 днк-цепочки
dnaContents1 = ""
dnaContents2 = ""
k = 0
for s in listDnaRead:
    if s.startswith (">"):
         k += 1
    elif (k == 1):
        dnaContents1 += s
    else:
        dnaContents2 += s


#считаем нуклеотиды
def countNucleotides(DNA):
    numberOfNuc = {}
    for nuc in DNA:
        numberOfNuc[nuc] = DNA.count(nuc)
    return numberOfNuc


output_file1 = open('./files/nucleotides_statistics.txt', 'w')
output_file1.write(f'First statictics:{countNucleotides(dnaContents1)}\nSecond statistics:{countNucleotides(dnaContents2)} \n')
output_file1.close()


# переводим днк в рнк
def translationDNAtoRNA(DNA):
    RNA = DNA.replace("T","U")
    return RNA


rna1 = translationDNAtoRNA(dnaContents1)
rna2 = translationDNAtoRNA(dnaContents2)
output_file2 = open('./files/dna_to_rna.txt', 'w')
output_file2.write(f'First RNA is:\n{rna1}\nSecond RNA is:\n{rna2} \n')
output_file2.close()


# переводим РНК в белок
def translationRNAtoProt(RNA):
    # Считываем таблицу кодонов и делаем список из элементов
    codonFile = open("files/rna_codon_table.txt", "r")
    contents1 = codonFile.read()
    codonFile.close()
    contents1.replace("   ", " ")
    listCodonRead = contents1.split(" ")
    listOfCodons = []
    for elem in listCodonRead:
        if ((elem is not "") and ("\n" not in elem)):
            listOfCodons.append(elem)
        elif ("\n" in elem):
            templList = elem.split("\n")
            for elem2 in templList:
                listOfCodons.append(elem2)
    # делаем словарь из кодонов
    dictionaryOfCodons = {}
    for sequence in listOfCodons:
        indexOfElement = listOfCodons.index(sequence)
        if indexOfElement % 2 == 0:
            dictionaryOfCodons[sequence] = listOfCodons[indexOfElement + 1]
    # делаем лист из рнк, лепим из него белок

    mod = len(RNA) % 3
    RNAlist = [RNA[i:i + 3] for i in range(0, len(RNA) - mod, 3)]

    for key in dictionaryOfCodons:
        for i in range (len(RNAlist)):
            if RNAlist[i] == key:
                RNAlist[i] = dictionaryOfCodons.get(key)
    return (', '.join(RNAlist)).replace(",","")
output_file3 = open('./files/proteins.txt', 'w')
output_file3.write(f'First protein is:{translationRNAtoProt(rna1)}\nSecond protein is:{translationRNAtoProt(rna2)} \n')
output_file3.close()