from folderWatcher import FolderWatcher


def main():
    path = input("Please enter the path of the folder to watch\n")
    fw = FolderWatcher(path)
    if fw.isPathValid():
        fw.watch()
    else:
        print("This is not a valid path, please try again")


if __name__ == "__main__":
    main()
