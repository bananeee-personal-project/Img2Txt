from unittest import result


def genNum(s):
    result = 0
    dictA = dict()

    for c in s:
        if not ord(c) in dictA:
            dictA[ord(c)] = 1
        else:
            dictA[ord(c)] += 1
    
    for key in dictA:
        result += dictA[key] * pow(24, key - ord('a') )

    return result


def groupAnagrams(strs):
    dictA = dict()
    
    for str in strs:
        tmpGenNum = genNum(str)

        if not tmpGenNum in dictA:
            arr = [str]
            dictA[tmpGenNum] = arr
        else:
            dictA[tmpGenNum].append(str) 

    result = []
    
    for key in dictA:
        result.append(dictA[key])
    
    return result
        
a = []
# a.pop()
a.append(1)
print(a[-1])

# print(ord("-11"))