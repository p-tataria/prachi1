dict1 = {'Prachi':99, 'Mike':56, 'Donna':89, 'Jessica':35}
a=str(input("Enter the student's name: "))
if a in dict1:
    print("Marks of",a,"are: ",dict1[a])
else:
    print(dict1.get(a,'Name not found'))
