
myfile1 = open("winedata_2.json", "rt")
contents1 = myfile1.read().replace("{","").replace("\"", "").replace("}, ", "|||").replace('\"',"")
myfile1.close()

# создали список строк
listWine = contents1.split("|||")
# заменили вхождения ":" и нужных "," на "!!!!!!!"
numbOfDicts=0
listOfDict = []
for wineString in listWine:
        wineDictionary = {}
        reversedString = reversed(wineString)
        counter = 0
        rightReverseString = ""
        for elem3 in reversedString:
            if( elem3 == ":"):
               elem3 = "!!!"
               rightReverseString+=elem3
               counter+=1
            if ( elem3 == "," and counter == 1):
               elem3 = "!!!"
               counter -= 1
               rightReverseString+=elem3
            rightReverseString+= elem3

        # засплитили строки по !!!!!!! и получили список элементов, сделали словарь для каждого вина
        rightString=(rightReverseString[::-1])
        rightList=rightString.split("!!!!!!")
        for element in rightList:
            rightList[10]='price'
            index = rightList.index(element)
            if ( index % 2 == 0 and index < len(rightList) - 1):
             wineDictionary[element] = rightList[index + 1]
        # print(wineDictionary)
        listOfDict.append(wineDictionary)
        numbOfDicts+=1
print(listOfDict)
Sortedlist=[]
Sortedlist = sorted(listOfDict, key=lambda k: k['price'])
 
