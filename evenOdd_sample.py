num = int(input("Choose a number to enter input : "));
numArray =  [];
evenArray = [];
oddArray = [];

while len(numArray) < num:
    Number = int(input("What number would you like to add?"))
    numArray.append(Number)

print ("Entered number :", numArray); 

for i in numArray:
   if (i%2==0):
      evenArray.append(i);
   else:
      oddArray.append(i);
  
print("Even list ", evenArray);  
print("Odd list ", oddArray);