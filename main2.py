from collections import deque

def is_palindrome(string: str):
    d = deque()
    pure_str = string.replace(" ", "").lower()
    for char in pure_str:
        d.append(char)

    validation = True    

    while len(d) > 1:
        right = d.pop()
        left = d.popleft()
        if right != left:
            validation = False
            break

    return validation    

# Test the function
print(is_palindrome("A man a plan a canal Panama"))  # Should return True
print(is_palindrome("racecar"))  # Should return True
print(is_palindrome("hello"))  # Should return False
