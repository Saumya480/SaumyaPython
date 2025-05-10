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


def find_duplicate_and_count(s):
    op = {}
    for i in s:
        if i != " ":
            if i not in op:
                op[i] = 1
            else:
                op[i] += 1
    print(op)
    op_new = [(i,j) for i,j in op.items() if j>1]
    return op_new


s1 = "Python Automation is very easy"
obj = find_duplicate_and_count(s1)
print(obj)