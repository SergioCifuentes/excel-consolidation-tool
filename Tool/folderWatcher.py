
from time import sleep

from fileManager import FileManager

DEFAULT_TIME_INTERVAL = 5   # Time interval (sec) for folder watching


class FolderWatcher:

    def __init__(self, folderPath):
        self.folderPath = folderPath
        self.fileManager = FileManager()

    def isPathValid(self):
        # Validate if path is a directory
        path = self.folderPath
        valid = self.fileManager.isDirectory(path)
        return valid

    def watch(self):

        while (True):
            print("Watching Folder...")
            self.fileManager.getFiles(self.folderPath)
            sleep(DEFAULT_TIME_INTERVAL)    # Pause for folder watching
