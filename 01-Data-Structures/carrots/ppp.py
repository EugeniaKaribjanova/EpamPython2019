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
dnaContents1


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
output_file2.write(f'First RNA is:{rna1}\nSecond RNA is:{rna2} \n')
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
    RNAlist = [RNA[i:i + 3] for i in range(0, len(RNA), 3)]
    print("RNA is", RNAlist)
    for key in dictionaryOfCodons:
        for i in range(len(RNAlist)):
            if RNAlist[i] == key:
                RNAlist[i] = dictionaryOfCodons.get(key)
    return (', '.join(RNAlist)).replace(",","")


output_file3 = open('./files/proteins.txt', 'w')
output_file3.write(f'First protein is:{translationRNAtoProt(rna1)}\nSecond protein is:{translationRNAtoProt(rna2)} \n')
output_file3.close()

# for key in dictionary:
#  rna1=rna1.replace(key, dictionary[key])
#  print(rna1+" ")




