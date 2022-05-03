# def is_palindrome(x: int) -> bool:
#     if str(x) == str(x)[::-1]:
#         return True

#     return False


# print(is_palindrome(123))

def is_palindrome1(x: int) -> bool:
    if (x < 0) or (x % 10 == 0 and x != 0):
        return False

    reverse_int = 0
    while x > reverse_int:
        reverse_int += (reverse_int* 10) + x % 10
        x = int(x/10)

    return x == reverse_int or x == int(reverse_int/10)
    
print(is_palindrome1(1001))
