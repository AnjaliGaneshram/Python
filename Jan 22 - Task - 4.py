#Task4:

#collect two strings from user


str1 = input("Enter the first name:")
str2 = input("Enter the second name:")

str_1 = str1.replace(str1[0],str2[0])
str_2 = str2.replace(str2[0],str1[0])
val_1 = (len(str_1)//2)
val_2 = (len(str_2)//2)

print(str_1+str_2+str(len(str_1))+str(len(str_2))+str_1[val_1]+str_2[val_2])




