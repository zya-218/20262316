import os

dir1 = input("First directory: ")
dir2 = input("Second directory: ")

if not os.path.isdir(dir1) or not os.path.isdir(dir2):
    print("Directory not found")
else:

    files1 = [entry.name for entry in os.scandir(dir1) if entry.is_file()]
    files2 = [entry.name for entry in os.scandir(dir2) if entry.is_file()]

    if len(files1) != len(files2):
        print("Different number of files")
    else:
        print("Same number of files")

    if set(files1) != set(files2):
        print("Different file name")
    else:
        print("Same file names")

    
    common_files = set(files1).intersection(set(files2))

    for file in common_files:
        path1 = os.path.join(dir1, file)
        path2 = os.path.join(dir2, file)

        
        size1 = os.stat(path1).st_size
        size2 = os.stat(path2).st_size

        if size1 == size2:
            print(file, ": same size")
            
            
            with open(path1, "rb") as f1:
                content1 = f1.read()
            with open(path2, "rb") as f2:
                content2 = f2.read()
                
            if content1 == content2:
                print(file, ": same content")
            else:
                print(file, ": different content")
        else:
            print(file, ": different size")
            print(file, ": different content")