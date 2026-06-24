from Common.Decorator import handle_exception

@handle_exception
def inputInt():
    return int(input())

@handle_exception
def inputFloat():
    return float(input())

@handle_exception
def inputStr():
    return input()

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
