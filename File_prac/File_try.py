# f=open("File_prac/file.txt","rt")
# data=f.read()
# print(data)
# f.close()
with open("File_prac/file.txt","rt") as f:
    data=f.read()
    print(data)
   

# with open("File_prac/file.txt") as f:
#   for x in f:
#     print(x)




# f=open("File_prac/file2.txt","a")
# f.write("\n line 2")
# print("done")
# f.close()

# with open("File_prac/file2.txt") as p:
#     print("file2 write output")
#     # print(p.read())
#     for x in p:
#         print(x)
        
        
# f=open("File_prac/file.txt","rt")
# data1=f.readlines(1)
# print(data1)
# data2=f.readlines(2)
# print(data2)
# data3=f.readlines(3)
# print(data3)
# f.close()