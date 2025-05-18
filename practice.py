# # # s1=input("Enter first string :")
# # # s2=input("Enter second string :")
# # # if s1==s2:
# # #     print("Both string are equal")
# # # elif s1>s2 :
# # #     print("First string is greater than second string")
# # # else:
# # #     print("first string is lesser than second string")
# #
# # s=input("Enter Main string :")
# # sub=input("Enter sub string :")
# # flag=False
# # pos=-1
# # n=len(s)
# # while True:
# #     pos=s.find(sub,pos+1,n)
# #     if pos==-1:
# #         break
# #     print("Found at position",pos)
# #     flag = True
# # if flag==False:
# #         print("Not Found")
# s="ababab"
# print(s)
# print("Before replacement",id(s))
# s=s.replace('a','b')
# print(s)
# print("After replacement",id(s))

s='0123456789'

print(s[-1:-2:-1])
