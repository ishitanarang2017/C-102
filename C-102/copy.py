import os,shutil
path = "C:/Users/Ishita Narang/Desktop/WhiteHatjr/C-102"
print(os.listdir(path))
source = "C:/Users/Ishita Narang/Desktop/WhiteHatjr/C-102/C102_assets-main/Badminton.gif"
dest = path + "/badminton.gif"
d = shutil.copy(source,dest)
print(os.listdir(path))