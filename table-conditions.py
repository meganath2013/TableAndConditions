rows=5
cols=5
errors=list()
error_cond3_check1=None
error_cond3_check2=None
#creating a 2d array with zero values
table1=[["0" for a in range(cols)] for b in range(rows)]

#Can use the below code to get input table one cell at a time
print("Enter the Table below one cell-value at a time")
table1=[[input() for p in range(cols)] for q in range(rows)]

#or can initilise table directly as below
#table1= [["Lorem", "354e", "dollor8", "86", "fd"],["consectetur", "745", "e8lit9", "812", "do"],["e9ius8mod", "731", "incididunt", "84", "labore"],["et", "122", "magna", "84129", "ut"],["enim", "8894", "minim", "91283", "quis"]]
print(table1)
for i in range(cols):
    error_cond3_check1="No 8 and 9"
    error_cond3_check2="No 89 or 98"
    for j in range(rows):
        #checking if its the even column ie col# 1,3,5 
        if(j%2!=0):
            if(not table1[i][j].isnumeric()):
                error_string="["+str(i+1)+" "+str(j+1)+"] cell doesnt have only numeric value"
                errors.append(error_string)
        #checking for null values
        if(table1[i][j]!=""):
        #checks if the cell value contains anything other than alphanumeric value
            if(not table1[i][j].isalnum()):
                error_string="["+str(i+1)+" "+str(j+1)+"] cell have special character"
                errors.append(error_string)
            
        if(table1[i][j].__contains__("8") and table1[i][j].__contains__("9") ):
            error_cond3_check1="Yes 8 and 9"
            if(table1[i][j].__contains__("89") or table1[i][j].__contains__("98")):
                error_cond3_check2="Yes 89 or 98"
                error_string="["+str(i+1)+" "+str(j+1)+"] cell have 8 and 9 as adjacent"
                errors.append(error_string)
    if(error_cond3_check1=="No 8 and 9"):
        error_string="["+str(i+1)+"] row doesnt have 8 and 9 in a cell"
        errors.append(error_string)
        
if(len(errors)==0):
    print("No Errors Found")
else:
    print( len(errors)," Errors Found in checking the table: See below: ")
    for temp in errors : print(temp)
   
