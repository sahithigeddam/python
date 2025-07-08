'''if condition'''
#age = int(input())
#if(age >= 18):
 #   print('you are eligible')
#else:
 #   print('sorry you are not eligible')  
'''time condition'''
#t = int(input())
#hr = t / 60 
#min = t % 60
#print(hr) 
#print(min)
#print(hr,'h'  ,min,'m')
#print(str(hr)+"h" +str(min)+"m")

'''sum of 1 tp 10'''
#n = int(input())
#sum_n = 0
#for i in range(1,n):
 #   print(i)
  #  sum_n =sum_n + i
   # print(sum_n)
    
    
'''print even numbers'''
#t=int(input('enter a number:'))
#total=0
#for i in range(t+1):
 #   if i%2==0:
  #      total=total+i
#print(total)

'''print odd numbers'''
#n=int(input())
#t=0
#for i in range(n+1):
#    if i%2!=0:
 #       t=t+i
#print(t)


'''print the numbers into array ''' 
# arr=[5 ,8, 3, 7, 6]
# t=0
# for i in arr:
#    if i%2==0:
#        t=t+i
# print(t)

'''print the s_e,s_o,s_a values'''
#arr  = [5,8,3,7,6]
#s_e =0
#s_o =0
#s_a =0
#for i in arr:
#    s_e += i
#    if (i % 2 == 0):
#        s_e += i
#else:
 #   s_o += i
  #  print(s_e,s_o,s_a)
   # print(s_e)
   # print(s_o)
    #print(s_a)
    
    
'''string slicing'''
#word='sahithi'   
#print(word[2])    

#word=input()
#n = int(input())
#print(word[1:5+1])
#print(word[5:])
#print(word[0],word[-1])
#print(word[:n])

'''string contain in even and old rangerover'''
# word = input()
# print(word[::2])
# print(word[1::2])

# word = input()
# length = len(word)
# even =" "
# odd = " "
# for i in range(length):
#  if(i % 2 == 0):
#    even += word[i]
# else:
#    odd += word[i]
# print(even,odd)      


''' special 11 prigram'''
#n=int(input())
#if n%11<=1:
 #  Print("special eleven")
#else:
 #  Print("normal number")'''
   
#n=int(input())
#if n%11==0 or n%11==1:
 #  Print("special eleven")
#else:
# Print("normal number")

''' input 20,10 output 2 for // 0 for %'''
#A=int(input())
#B=int(input())
#print(A//B)
#print(A%B)

#A = input("enter string")
#B = input("enter a with common letters")  
#r=""
#for i in  A:
 #    if i in B:
  #        pass
   #  else:
    #      r += i
#
#print(r)




#s=input()
#print(ord(s))




#s =input()
#for i in s:
 # print(i)
  #v=i.isupper()
  #print(v)
  #r = i.islower()
  #print(r)
  
'''print top 3'''
#r=int(input())
#if (r<=3):
 # print("one of top 3")
#elif(r<=10):
 # print("not top 3 but one of top 10")
 
 
'''avg    of number from 1'''
 
 # n = int(input())
  #sum = 0
  #for i in  range(1,n+1):
   #     sum += i
    #    a = sum/n
     #   print(a)
     
 #s=input()
#n=int(input())
#r = ""
#for i in range(n):
 #   n1=int(input())
  #  r += s[n1]
  
'''string is saparated into even and odd index'''
# word = input('enter a string')
# a=len(word) 
# even = []
# odd = []
# for i in range(a):
#   if(i%2==0):
#     even += word[i]
#   else:
#     odd += word[i]
#     print(even,odd)     

'''the digit from the given input and find sum of even numbers of even numbers and sum of odd  
hey 25 43 hello 54 good 7'''
# l=list(map(str,input().split())) 
# s_n=0
# s_e=0
# s_0=0
# for i in l :
#   if i.isdegit():
#      s_nt=int(i)
#      if int(i)%2==0:
#         s_et=int(i)
#      else:
#        s_o += int(i)
#   print(s_n)
#   print(s_e)
#   print(s_o)       

'''index numbers are divisible by a given number''' 
# n=list(map(int,input().split()))
# n=int(input())
# r=[]
# for i in r:
#   r.append(i*n)
# print(r)

'''fibonacci numbers meanes sum of its two previus numbers are equal to their third number  
"f(n)=f(n-1)+f(n-2)"
the first  two numbers 0&1 has to be declare at starting'''
# n=int(input())
# l=[0,1]
# a=0
# b=1
# for i in range(n-2):
#   c=a+b
#   l.append(c)
#   a=b
#   b=c  
# print(*l)


'''you are given a string and you have to count the v0wels
in the given string(both upper and lower cases)and return the total count'''
# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for ch in s:
#     if ch in vowels:
#         count += 1

# print("Total vowels:", count)

'''or''' 
# s=input()
# c=0
# for each in s:
#   if each in "aeiouAEIOU":
#     C += 1
    
#     print(C)
'''YOU ARE GIVEN A STRING S YOUR TASK IS TO CHECK IF THE STRING IS A PALANDROM OR NOT
 a string is considered as palindrom it reaches same forward and backed IGNeRed  ' 
'''   
# s = input("Enter a string: ")
# s = s.lower()           
# s = s.replace(" ", "") 
# if s == s[::-1] :   
#     print("true")
# else:
#     print("false")
'''or'''
# s=input().split()
# l="".join(s)
# v=l.lower()
# res=v[ ::-1]
# if v==res:
#   print(true)
# else:
#   print(false)  
'''given a string s your task is to count the number of words in the string and return the total count'''
# s =input()
# word_count = len(s.split())
# print("Number of words:", word_count)
'''your are given a string your task is to remove dupplicate char
to string while presering the order of the first occurings and return the modified string'''
# s = input()
# s = "".join(dict.fromkeys(s))
# print(s)
'''or'''
# s=input()
# v=""
# for i in s:
#   if i not in  v:
#     v += i
#     print(v)


'''addition of sum of 5 numbers using difrient oparators'''
# a=int(input("enter a number:"))
# b=int(input("ente a number:"))
# c=int(input("enter a number:"))
# d=int(input("enter a number:"))
# e=int(input("enter a number:"))
# print("add",a+b)
# print("sub",b-c)
# print("mul",c*d)
# print("div",d/e)

'''given n integer if n is odd "print weired
if n is even and in the range of 6 to 10 "print weired"
if n is even and in the range of 2 to 5 "print not weard"
if n is even and greater than 20 "print not weard'''
# n=int(input())
# if(n%2!=0):
#   print("weird")
# elif(6<=n<=20):
#   print("weird")   
# else:
#   print("not weird")  
'''or'''
# n=int(input())
# if(n%2!=0)or(n%2==0 and 6<=n<=20):
#   print("weird")
# else:
#   print("not weird")  

'''given a,b are  two integers 
output: sum of a,b
        difference of a,b
        product of a,b'''

# a= int(input())
# b=int(input())
# print(a+b)
# print(a-b)
# print(a*b)  
      


'''valid palindrom(125)'''
# s=input()
# r=""
# v=s.lower()
# for i in v:
#     if i.isalnum():
#        r+=i
# l=r[::-1]
# if r==l:
#    print("true")
# else:
#    print("false")    
'''single number(136)'''
# nums=list(map(int,input().split()))
# for i in nums:
#   if nums.count(i)==1:
#     print(i)
#     break
'''two sum(1)'''
# nums=list(map(int,input().split()))
# target=int(input())
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#            print([i,j])
#            break

'''third maximum number(414)'''

# nums=list(map(int,input().split()))
# if(len(nums)>=3):
#    l=list(set(nums))
#    l.sort()
#    print(l[-3])
# else:
#   print(max(nums))   

# for i in nums:
#   if i not in l:
#     l.append(i)
#     print(l)

'''jewels and stones(771)'''
# j=input()  
# s=input()
# count =0
# for i in s:
#   if i in j:
#     count += 1
# print(count)
'''add string(415)'''
# num1=input()
# num2=input()
# s=int(num1)  + int(num2)
# r=str(s)
# print('"',r,'"')
'''sqrt (69)'''
# import math
# x=int(input())
# v=math.floor(math.sqrt(x))
# print(v)
'''divide two integers()'''
# import math
# x=int(input())
# y=int(input())
# print(int(x / y))
# a=input()
# b=input()
# print(a+b)
'''fizz buzz (412)'''
# n=int(input())
# list=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         list.append("fizzbuzz")
#     elif i%3==0:
#         list.append("fizz")
#     elif i%5==0:
#         list.append("buzz")
#     else:
#         list.append(str(i)) 
# print(list)                   

'''palindrome number(9)'''
# x=int(input())
# v=str(x)
# if v in v[::-1]:
#     print("true")
# else:
#     print("flase")   
'''plus one'''
a=int(input("enter the nymber:"))
n=a+1
print([n])
# digits = [1, 2, 3]

# num = int(''.join(map(str, digits))) + 1
# result = list(map(int, str(num)))

# print(result)