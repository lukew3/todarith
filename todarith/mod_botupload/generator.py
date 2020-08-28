def runGenerator():
    mainList=[]
    mainList = mainList + singleDigitAddition()
    mainList = mainList + singleDigitSubtraction()
    mainList = mainList + doubleDigitAddition_noCrossover()
    mainList = mainList + doubleDigitAddition_all()
    mainList = mainList + doubleDigitSubtraction_noCrossover()
    mainList = mainList + doubleDigitSubtraction_all()
    return mainList


def singleDigitAddition():
    skill = 2
    setList = []
    for x in range(0, 10):
        for z in range(0,10):
            prob = str(z) + "+" + str(x)
            ans = str(z + x)
            if int(ans)<10:
                print(prob + "=" + ans)
                problem_tuple = (prob, ans, skill)
                setList.append(problem_tuple)
    print(setList)
    return setList

def singleDigitSubtraction():
    skill = 3
    setList = []
    for x in range(0, 10):
        for z in range(0, 10):
            prob = str(z) + "-" + str(x)
            ans = str(z-x)
            if int(ans)>=0:
                print(prob + "=" + ans)
                problem_tuple = (prob, ans, skill)
                setList.append(problem_tuple)
    print(setList)
    return setList


def doubleDigitAddition_noCrossover():
    skill = 2
    setList = []
    for x in range(0, 100):
        for z in range(0, 100):
            prob = str(z) + "+" + str(x)
            ans = str(z + x)
            if int(ans)<100 and (x%10 + z%10 < 10):
                print(prob + "=" + ans)
                problem_tuple = (prob, ans, skill)
                setList.append(problem_tuple)
    print(setList)
    return setList

def doubleDigitAddition_all():
    skill = 2
    setList = []
    for x in range(0, 100):
        for z in range(0, 100):
            prob = str(z) + "+" + str(x)
            ans = str(z + x)
            if int(ans)<100:
                print(prob + "=" + ans)
                problem_tuple = (prob, ans, skill)
                setList.append(problem_tuple)
    print(setList)
    return setList

def doubleDigitSubtraction_noCrossover():
    skill = 3
    setList = []
    for x in range(0, 100):
        for z in range(0, 100):
            prob = str(z) + "-" + str(x)
            ans = str(z - x)
            if (int(ans)>=0 and (z%10 > x%10)):
                print(prob + "=" + ans)
                problem_tuple = (prob, ans, skill)
                setList.append(problem_tuple)
    print(setList)
    return setList

def doubleDigitSubtraction_all():
    skill = 3
    setList = []
    for x in range(0, 100):
        for z in range(0, 100):
            prob = str(z) + "-" + str(x)
            ans = str(z - x)
            if (int(ans)>=0):
                print(prob + "=" + ans)
                problem_tuple = (prob, ans, skill)
                setList.append(problem_tuple)
    print(setList)
    return setList
