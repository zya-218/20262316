import os
base = input()
search =".txt"
if os.path.exists(base) and os.path.isdir(base):
    with os.scandir(base) as entries:
        for entry in entries:
            if entry.is_file():
                if entry.name.endswith(search):
                    print(f"txt file:{entry.name}")
                else:
                    print("there is not txt file")


else:
    print("base is not folder")