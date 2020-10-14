#-----assignment-1 ---------------------------------------

string = "shfbsmbfmsf,jsnwh.wkheshdka"
print(len(string))


#-------assignment-3--------------------------------------
strg = "w3resource"
arr = []
for i in strg:
    arr.append(i)
print(arr)
for element in arr:    
    output = arr[0] + arr[1] + arr[len(arr)-2] + arr[len(arr)-1]
print(output)
    

#--------assignment-4--------------------------------------

strg1 = "restart"
new1 = ""
new2 = ""
for i in strg1 :
    new1 = strg1
print(new1)
new2 = new1.replace("r","$",1)
print(new2)


#---------assignment : 2 ----------------------------------
        
name = "google.com"

name1 = {}

for i in name :
    if i in name1 :
        name1[i] += 1
    else :
        name1[i] = 1

print(name1)


        










     
