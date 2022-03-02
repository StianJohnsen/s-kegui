from gettext import find
import os 

directory_counter = 0
file_counter = 0


path = "C:/Users/stian/Documents/Python/skole-test/SøkeGui/"
for base,dirs,files in(os.walk(path)):
    for directories in dirs:
        directory_counter += 1
    for Files in files:
        file_counter += 1


path_1 = "C:/Users/stian/Documents/Python/skole-test/SøkeGui/heisann.txt"

list_files = [
    [],
    []
]

def find_files_directories(path):
    
    if not (os.path.isfile(path)):

        for subdir in os.listdir(path):
            find_files_directories(path+"\\"+subdir)

    else:
        list_files[0].append(os.path.dirname(path))
        list_files[1].append(os.path.basename(path))
        #path_file[os.path.dirname(path)] = list_files
    
    return (list_files[0], list_files[1],directory_counter,file_counter)

    
def read_file():

 

    for i,j in zip(find_files_directories(path)[0],find_files_directories(path)[1]):
        print(i)
        print(j)
        print()
        


read_file()








