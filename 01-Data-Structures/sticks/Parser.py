jsonFile1 = open("winedata_1.json", "rt", encoding='utf-8')
jsonFile2 = open("winedata_2.json", "rt", encoding='utf-8')

contents1 = jsonFile1.read().replace("]", "").replace("[", "")
contents2 = jsonFile2.read().replace("]", "").replace("[", "").replace("{", ", {", 1)

fullContents = (contents1 + contents2).replace("{", "").replace("\": ", "@@@").replace("}, ", "|||"). \
    replace(", \"", "~~~").replace("\"", "")
jsonFile2.close()
jsonFile1.close()

listWine = fullContents.split("|||")
listOfDistinctElements = list(dict.fromkeys(listWine))

listOfDict = []
for wineString in listOfDistinctElements:
    wineDictionary = {}
    listOfPairs = wineString.split("~~~")

    for elem3 in listOfPairs:
        listOfKeyAndValue = elem3.split("@@@")
        if len(listOfKeyAndValue) % 2 == 1:
            print(listOfKeyAndValue)
        for val in listOfKeyAndValue:
            index = listOfKeyAndValue.index(val)
            if val == 'price' and listOfKeyAndValue[index + 1] != 'null':
                wineDictionary[val] = int(listOfKeyAndValue[index + 1])
                continue
            if val == 'price' and listOfKeyAndValue[index + 1] == 'null':
                wineDictionary[val] = 0
                continue
            if val == 'taster_name' and listOfKeyAndValue[index + 1] == 'null':
                wineDictionary[val] = " "
                continue
            if index == 0:
                wineDictionary[val] = listOfKeyAndValue[index + 1]
    listOfDict.append(wineDictionary)
sortedList = listOfDict

sortedList.sort(key=lambda x: x['taster_name'])
sortedList.sort(key=lambda x: x['price'])

output_file3 = open('sortedJson.json', 'w', encoding='utf-8')
output_file3.write(str(sortedList).replace("\'", "\"").replace("\" \"", "null").
                   replace("\"price\": 0", "\"price\": null"))
output_file3.close()

listOfSelectedWines = []
listOfWineNames = ["Gew[üu]rztraminer", "Riesling", "Merlot", "Madera", "Tempranillo", "Red Blend"]
for x in range(5):
    wine = {"title": listOfWineNames[x]}

    average_price = 0
    average_score = 0
    min_price = 0
    max_price = 0
    most_common_region = ""
    most_common_country = ""

    counter = 0
    sumOfPrices = 0
    sumOfPoints = 0

    for wineDictionary in sortedList:
        if wineDictionary["title"] == wine["title"]:

            dictionaryCountries = {wineDictionary["region_1"] : 1}
            dictionaryRegions = {}

            dictionaryRegions[=
            wineDictionary["region_2"]
            currentPrice = int(wineDictionary["price"])
            counter += 1
            sumOfPrices += currentPrice
            average_price = sumOfPrices / counter

            sumOfPoints += int(wineDictionary["points"].replace("\"", ""))
            average_score = sumOfPoints / counter

            if min_price == 0 or min_price < currentPrice:
                min_price = currentPrice
            if max_price == 0 or max_price > currentPrice:
                max_price = currentPrice



