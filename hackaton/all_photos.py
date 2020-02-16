import os
import shutil

main_dir = "D:/Test/"
photos_dir = "D:/Photos/"
photo_extensions = ["jpg", "jpeg", "png"]


def files(dir):
    return os.listdir(dir)


def is_photo(name):
    return any(name.endswith(ext) for ext in photo_extensions)


def photo_here(dir):
    flag = 0
    for file in files(dir):
        if is_photo(file):
            flag = 1
            break
    return flag


def cut_photo(file, to_dir):
    shutil.move(file, to_dir)


def cut_photos(from_dir, to_dir):
    for file in files(from_dir):
        if is_photo(file):
            cut_photo(f"{from_dir}/{file}", to_dir)
        else:
            cut_photos(f"{from_dir}/{file}", to_dir)


if __name__ == "__main__":
    if not photo_here(main_dir):
        cut_photos(main_dir, photos_dir)
    else:
        print("Error! Files in directory.")
