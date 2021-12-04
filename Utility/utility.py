def fileReader(filename):
    fin = open(filename)
    returnList = []
    for each in fin.readlines():
        tempElement = each.replace('\n', '').replace('\r', '')
        returnList.append(tempElement)
    return returnList
