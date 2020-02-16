import os
import shutil

def copy_all_to(local, dir):
    for file in os.listdir(directory):
        if not file.endswith(".jpg") and not file.endswith(".png") and not file.endswith(".jpeg"):
            copy_all_to(local+"/"+file, dir)
        else:
            name = file.replace(".jpg", ".jpeg").replace(".png", ".jpeg")
            shutil.move(local+"/"+file, dir+"/"+name)



if __name__ == "__main__":
    main_directory = "D:/Test/"
    os.chdir(main_directory)
    files = os.listdir(main_directory)



    # print(files)
    for i, file in enumerate(files):
        i = i + 1
        os.renames(file, str(i))
        directory = main_directory + str(i)
        for file in os.listdir(directory):
            if not file.endswith(".jpg") and not file.endswith(".png") and not file.endswith(".jpeg"):
                copy_all_to(directory+"/"+file, directory)



    # for i, file in enumerate(files):
    #     os.renames(file, i)