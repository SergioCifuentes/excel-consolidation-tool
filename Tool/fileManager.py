import os.path
import shutil
from fnmatch import fnmatch

from excelManager import ExcelManager

PATH = r""                          # Path where folders will be created
PROCESSED = "Processed"             # Processed folder name
NOT_APPLICABLE = "NotAplicable"     # Not applicable folder name
PATTERN = "*.xls*"                  # Excel Pattern


class FileManager(object):

    def __new__(cls):
        # if instance already exists it doesn't create a new one
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
        return cls.instance

    def isDirectory(self, path):
        # Validate if path is a Directory
        isdir = os.path.isdir(path)
        return isdir

    def getFiles(self, path):
        self.excelManager = ExcelManager()
        self.__createDirectory()
        # Iterate through  directory
        for path, subdirs, files in os.walk(path):
            for name in files:
                fullName = os.path.join(path, name)
                if fnmatch(name, PATTERN):      # verify excel type file
                    processed = self.excelManager.proccessFile(fullName)
                    self.__moveFile(fullName, processed)
                else:
                    self.__moveFile(fullName, False)

    def __createDirectory(self):
        # creates two directories (Processed and Not Applicable)
        try:
            os.makedirs(os.path.join(PATH, PROCESSED), exist_ok=True)
            os.makedirs(os.path.join(PATH, NOT_APPLICABLE), exist_ok=True)
        except OSError:
            print('Creating directory error')

    def __moveFile(self, file, processed):
        # moves file to corresponding folder(processed or not applicable)
        try:
            if processed:
                print("Processed Correctly "+file)
                shutil.move(file, os.path.join(PATH, PROCESSED))
            else:
                print("Not Applicable "+file)
                shutil.move(file, os.path.join(PATH, NOT_APPLICABLE))
        except FileNotFoundError:
            print('File Not Found')
        except OSError:
            print('Moving error')
