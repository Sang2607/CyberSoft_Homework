from Common.Decorator import handle_exception

@handle_exception
def inputInt(Mess = ""):
    return int(input(Mess))

@handle_exception
def inputFloat(Mess = ""):
    return float(input(Mess))

@handle_exception
def inputStr(Mess = ""):
    return input(Mess)

@handle_exception
def checkDict(value):
    return isinstance(value, dict)

def quickSort(arr): # Độ phức tạp O(nlogn)
    if len(arr) == 0:
        return []
    lastNum = arr[-1]
    minArr = []
    maxArr = []
    equalArr = []
    for i in range(len(arr) + 1):
        num = arr[i - 1]
        if num < lastNum:
            minArr.append(num)
        elif num > lastNum:
            maxArr.append(num)
        else:
            equalArr.append(num)
    ResuftArr = quickSort(minArr)+ equalArr +quickSort(maxArr)
    return ResuftArr
