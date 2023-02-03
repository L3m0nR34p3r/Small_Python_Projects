import random as r

# How many questions are in each chapter
chapter1 = 293
chapter2 = 192
chapter3 = 160
chapter4 = 200
chapter5 = 220

def getNumbers(chapter):
    #How many questions do you want on the practice test
    numQue = 100
    #Devides the chapters evenly to output questions
    numPerChap = int(numQue/5)
    test = []
    i = 0
    #iterates through the chapter questions and generates a list of random #'s
    while i < numPerChap:
        rnum = r.randint(1,chapter)
        if rnum not in test:
            test.append(rnum)
        else:
            continue
        i += 1
    test.sort()
    return test
#Creates an array of chapter's with the questions you should pull to create your test.    
test1 = (f"Ch.1: {getNumbers(chapter1)}\nCh.2: {getNumbers(chapter2)}\nCh.3: {getNumbers(chapter3)}\nCh.4: {getNumbers(chapter4)}\nCh.5: {getNumbers(chapter5)}\n")
print(test1)