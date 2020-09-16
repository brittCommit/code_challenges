
def runningSum(nums):
    
    ret = []
    for idx, num in enumerate(nums):
        print(idx, num)
        if idx == 0:
            ret.append(num)
        else:
            ret.append(num + ret[idx - 1]) 
    return ret