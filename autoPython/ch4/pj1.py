def reMap(someList):
    result = ''
    for i in range(len(someList)):
        if i == len(someList) - 1:
            result += ('and ' + someList[i])
        else:
            result += (someList[i] + ', ')
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(reMap(spam))
