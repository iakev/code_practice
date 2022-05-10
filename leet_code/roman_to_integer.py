# def romanToInt(s:str) -> int:
#     # dictionary to store roman to int mapping
#     roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#     interger = 0 #resulting interger
#     previous = 0 #holding the previous to deal with subtraction

#     for i in range(len(s)):
#         if i > 0:

#             previous = roman_dict[s[i-1]]

#         if previous < roman_dict[s[i]] and previous != 0:
#             interger -= previous
#             interger += (roman_dict[s[i]]-previous)
#         else:

#             interger += roman_dict[s[i]]
        
#     return interger

# print(romanToInt("III"))

## Someone else's solution
def romanToInt(s:str) -> int:
    # dictionary to store roman to int mapping
    roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    interger = 0 #resulting interger

    for i in range(len(s)):
        if (i + 1) < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
            interger -= roman_dict[s[i]]

        else:
            interger += roman_dict[s[i]]

    return interger

print(romanToInt("III"))