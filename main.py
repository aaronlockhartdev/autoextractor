import os
import zipfile
import threading
import time


def unzip(zip_directory, unzip_directory):

    files = os.listdir(zip_directory)
    threads = list()

    for ind, f in enumerate(files):
        print(str(ind/len(files) * 100) + "%")
        
        unzipper = zipfile.ZipFile(zip_directory + '/' + f, 'r')
        unzipper.extractall(path=unzip_directory)
    move_files(unzip_directory)


def move_files(unzip_directory):
    dirs = os.listdir(unzip_directory)
    for d in dirs:
        directory = unzip_directory + '/' + d
        files = os.listdir(directory)
        for f in files:
            try:
                print(f, end='\r', flush=True)
                os.rename(directory + '/' + f, 'D:/tmp/' + f)
            except:
                continue
        os.rmdir(directory)
    files = os.listdir('D:/tmp')
    for f in files:
        os.rename('D:/tmp/' + f, unzip_directory + '/' + f)


def main():
    zip_directory = 'D:/LDS_ALL'
    unzip_directory = 'D:/LDS_EXTRACTED'
    unzip(zip_directory, unzip_directory)

if __name__ == '__main__':
    main()