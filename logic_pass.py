#q1 method remove any given character from a string
def Remove_str():
    str_char = input("Please enter a string:\n")
    # Printing original string  
    print ("The original string: " + str_char) 
    num =int( input("Please enter anumber of character to remove it:\n") )
    result_str = "" 
      
    for i in range(0, len(str_char)): 
        if i !=num : 
            result_str += str_char[i] 
      
    # Printing string after removal   
    print ("String after removal of i'th character : " + result_str)
    
Remove_str()
#q2 Program to find Prime Numbers in a Given Range
low = int(input("Enter the lower number : "))
up = int(input("Enter the upper number: "))
for n in range(low,up + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
#q3 function counts how many the given character repeated in agiven string by python
def dublicate():
    string = input("Enter the string : ")
        
    print("the duplicate characters in a given string: ");  
    for i in range(0, len(string)):  
        count = 1;  
        for j in range(i+1, len(string)):  
            if(string[i] == string[j] and string[i] != ' '):  
                count = count + 1;  
                string = string[:j] + '0' + string[j+1:];  
        
        if(count > 1 and string[i] != '0'):  
            print(string[i]," - ",count);
dublicate()
