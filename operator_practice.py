# 1. Display the sum of 3 and 8
a,b=2,4
sum=a+b
print(f"The sum of {a} and {b} is {sum}")
# 2. Display the difference of 3 and 8
a=8
b=3
diff=a-b
print(f"The diff of {a} and {b} is {diff}")
# 3. Display the product of 3 and 8
a=3
b=8
product=a*b
print(f"The Product of {a} and {b} is {product}")
# 4. Display the result of 8 divided by 3
a=8
b=3
div=a/b
print(f"The dividend of {a} and {b} is {div}")
# 5. Display the remainder or modulus of 8 by 3
a=8
b=3
mod=a%b
print(f"The Modulus of {a} and {b} is {mod}")
# 6. Display the result of 8 to the power of 3
a=8
b=3
result=a**b
print(f"The Power  of {a} and {b} is {result}")
# 7. Display the divisor of 8 by 3
numerator = 8
denominator = 3
result = numerator / denominator
print("The result of", numerator, "divided by", denominator, "is", result)
# COMPARISON OPERATOR  QUESTIONS
# 1. Display the result if 5 is equal 5.0
a=5
b=5.0
result=(a==b)
print("Is 5 equal to 5.0  True or False :",result)
# 2. Display the result if 5 is greater than 2
a=5
b=2
res1=a>b
print(f" {a} greater than {b} True or False :" ,res1)
# 3. Display the result if 5 is lower than 2
a=5
b=2
res2=a<b
print(f" {a} lower than {b} True or False :" ,res2)
# 4. Display the result if 5 is greater than or equal to 5.0
a=5
b=5.0
res3=(a>=b)
print("Is 5 equal to 5.0  True or False :",res3)
# 5. Display the result if 5 is lower than or equal to 4
a=5
b=4
res4=(a<=b)
print("Is 5 lower than equal to 4 True or False :",res4)
# 6. Display the result if 5 is equal or not to 5.0
a=5
b=5.0
if a==b:
    print("5 is equal to 5.0")
else:
    print("5 is not equal to 5.0")

# Membership Operators

# 1. Check if the value 10 is in the given list [1,5,10,101]
x=10
y=[1,5,10,101]
print(x  in y)
# 2. Check if the value -8 is in the given list [1,5,10,101]
x=-8
y=[1,5,10,101]
print(x in y)