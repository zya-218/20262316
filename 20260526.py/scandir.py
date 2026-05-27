import os
base = input()
if os.path.exists(base) and os.path.isdir(base):
    with os.scandir(base) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f" folder {entry.name}")
            elif entry.is_file():
                print(f" file {entry.name}")
else:
    print("base is not folder!")