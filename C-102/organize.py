import os,shutil
source = "C:/Users/Ishita Narang/Desktop/WhiteHatjr/C-102/C102_assets-main"
dest = "C:/Users/Ishita Narang/Desktop/WhiteHatjr/python/C-102"
listoffiles = os.listdir(source)
for files in listoffiles:
    name,extension = os.path.splitext(files)
    if extension=="":
        continue
    if extension in['.gif','.png','.jpeg','.jpg','.jfif']:
        path1 = source + '/'+ files
        path2 = dest + '/'+ "imgfiles"
        path3 = dest + '/' + "imgfiles"+ '/' + files
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
