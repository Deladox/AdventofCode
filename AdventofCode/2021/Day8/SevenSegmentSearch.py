
def digitEncrypter(digits):
    #print(digits)
    fives = []
    sixes = []
    digitpair = [0,1,2,3,4,5,6,7,8,9]
    for x in digits:
        if len(x) == 2:
            digitpair[1] = x
        if len(x) == 3:
            digitpair[7] = x
        if len(x) == 4:
            digitpair[4] = x
        if len(x) == 7:
            digitpair[8] = x
        if len(x) == 5:
            fives.append(x)
        if len(x) == 6:
            sixes.append(x)
    for i, x in enumerate(fives):
        counter = 0
        if digitpair[1][0] in x and digitpair[1][1] in x:
            digitpair[3] = x
            fives[i] = 0
        for y in digitpair[4]:
            if y in x:
                counter += 1
        if counter == 2:
            digitpair[2] = x
            fives[i] = 0
    for i, x in enumerate(fives):
        if x != 0:
            digitpair[5] = x
    for i, x in enumerate(sixes):
        if digitpair[4][0] in x and digitpair[4][1] in x and digitpair[4][2] in x and digitpair[4][3] in x:
            digitpair[9] = x
            sixes[i] = 0
        if digitpair[1][0] not in x or digitpair[1][1] not in x:
            digitpair[6] = x
            sixes[i] = 0
    for i, x in enumerate(sixes):
        if x != 0:
            digitpair[0] = x
    print(digitpair)
    return digitpair
        

def wordCounter(wordList, digitList,):
    outputvalues = []
    for i in range(len(digitList)):
        outputdigits = []
        digits = digitEncrypter(digitList[i])
        #print(wordList[i])
        #print(digits)
        for word in wordList[i]:
            print(wordList[i])
            outputdigits.append(whatDigit(word, digits))
            print(outputdigits)
        testdigit = "".join(outputdigits)
        testdigit = int(testdigit)
        outputvalues.append(testdigit)
    return sum(outputvalues)
    

def whatDigit(word, digitList):
    sortedWordList = sorted(word)
    sortedWord = "".join(sortedWordList)
    print(sortedWord)
    for i, x in enumerate(digitList):
        sortedWordDigitList = sorted(x)
        sortedWordDigit = "".join(sortedWordDigitList)
        print(sortedWordDigit)
        if sortedWordDigit == sortedWord:
            #print(i)
            return str(i)
        

    sortedWordList = sorted(word)
    sortedWord = "".join(sortedWordList)



with open("input.txt") as f:
    read = [line.strip() for line in f.readlines()]
    output = []
    alldigits = []
    for i, line in enumerate(read):
        read[i] = line.split(" | ")
        alldigits.append(read[i][0].split(" "))
        output.append(read[i][1].split(" "))
    count = wordCounter(output, alldigits)
    word = "abskrhy"


    print(count)