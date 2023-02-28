

#exception handling
filename = 'C:\Users\USER\OneDrive\Documents\Inspire_Youths_In_STEM\week4\test.txt'
try:
    for file in filename:
         with open(filename,'r+w') as f_obj:
               contents = f_obj.read()
        
except FileNotFoundError:
    msg = "Sorry, the file" 




f =open("C:\\Users\USER\OneDrive\Documents\Inspire_Youths_In_STEM\week4\test.txt",mode = "r")
print(f.readlines())

