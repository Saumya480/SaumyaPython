def check_palindrome(s):
    op = ""
    for i in s:
        op = i + op
    if op == s:
        print("It's a palindrome string")
    else:
        print("The string is not palindrome!")


ip = "abcba"
check_palindrome(ip)

