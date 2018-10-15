targetString = "Earlier this year, the user information of millions of Facebook users was leaked." \
               " It was a big deal." \
               " Personal information leaks online occur very frequently." \
               " To make use of services on the Internet, people have to enter their personal information." \
               " These days, search histories and user patterns are all recorded permanently." \
               " When this information is compromised by hackers, it’s a major headache." \
               " Users experience a serious invasion of privacy." \
               " It makes them feel uneasy when using the Internet." \
               " The hacked personal information could be used in identity theft crimes." \
               " Some exposure of personal information is part and parcel of cyberspace." \
               " However, obtaining and abusing personal information by shady means should be prevented." \
               " Before the problem gets out of hand, we have to nip it in the bud by strengthening laws."

firstIndex = targetString.index(".", 0, len(targetString))
secondIndex = targetString.index(".", firstIndex+1, len(targetString))
thirdIndex = targetString.index(".", secondIndex+1, len(targetString))
fourthIndex = targetString.index(".", thirdIndex+1, len(targetString))
fifthIndex = targetString.index(".", fourthIndex+1, len(targetString))
sixthIndex = targetString.index(".", fifthIndex+1, len(targetString))
seventhIndex = targetString.index(".", sixthIndex+1, len(targetString))
eightIndex = targetString.index(".", seventhIndex+1, len(targetString))
ninthIndex = targetString.index(".", eightIndex+1, len(targetString))
tenthIndex = targetString.index(".", ninthIndex+1, len(targetString))
eleventhIndex = targetString.index(".", tenthIndex+1, len(targetString))
twelfthIndex = targetString.index(".", eleventhIndex+1, len(targetString))

firstSentence = targetString[0:firstIndex+1]
secondSentence = targetString[firstIndex+1:secondIndex+1]
thirdSentence = targetString[secondIndex+1:thirdIndex+1]
fourthSentence = targetString[thirdIndex+1:fourthIndex+1]
fifthSentence = targetString[fourthIndex+1:fifthIndex+1]
sixthSentence = targetString[fifthIndex+1:sixthIndex+1]
seventhSentence = targetString[sixthIndex+1:seventhIndex+1]
eightSentence = targetString[seventhIndex+1:eightIndex+1]
ninthSentence = targetString[eightIndex+1:ninthIndex+1]
tenthSentence = targetString[ninthIndex+1:tenthIndex+1]
eleventhSentence = targetString[tenthIndex+1:eleventhIndex+1]
twelfthSentence = targetString[eleventhIndex+1:twelfthIndex+1]

a = [firstSentence, secondSentence, thirdSentence, fourthSentence, fifthSentence, sixthSentence, seventhSentence,
     eightSentence, ninthSentence, tenthSentence, eleventhSentence, twelfthSentence]
for x in range(12):
    print(a[x+0])

dotCount = targetString.count(".")

for s in range(0, dotCount):
    firstSentence = targetString[0:firstIndex + 1]

    dotCount += 1
    first = firstIndex+2
    print()

wordList = targetString.split(" ")
print(wordList)
print(len(wordList))
singleWordList = list(set(wordList))
print(singleWordList)
print(len(singleWordList))

from collections import Counter
counts = Counter(wordList)
print(counts)
