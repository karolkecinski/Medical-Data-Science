from requests import *
import json 

class Exercise:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def printNegative(self, inputlist):
        for element in inputlist:
            if element < 0:
                print(element)

    def filterOdd(self, inputlist):
        oddList = []
        for element in inputlist:
            if element % 2 == 1:
                oddList.append(element)
        return oddList

    def removeDuplicate(self, inputlist):
        return list(set(inputlist))

    def reverseString(self, str):
        result = ""
        wordList = str.split()
        for word in wordList[::-1]:
            result = result + " " + word
        return result

    def sendRequest(self, method, endpoint):
        return request(
            method,
            endpoint,
            headers = { },
            stream=True
        )

    def distanceToSun(self):
        planet = input("Please, typle a planet name:")
        endpoint = 'https://api.le-systeme-solaire.net/en/'
        res = self.sendRequest('GET', endpoint)

ex = Exercise()
print(ex.factorial(11))

inputlist = [1, 6, 6, -5, 0, -234, -234, 7]
ex.printNegative(inputlist)

print(ex.filterOdd(inputlist))
print(ex.removeDuplicate(inputlist))
print(ex.reverseString("This is an example string!"))