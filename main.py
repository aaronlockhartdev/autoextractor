import os
import zipfile
import threading
import time

def thread_func(f, zip_directory, unzip_directory, num):
    print(str("{} started unzipping " + f).format("Thread" + str(num)))
    unzipper = zipfile.ZipFile(zip_directory + '/' + f, 'r')
    unzipper.extractall(path=unzip_directory)
    print(str("{} finished unzipping " + f).format("Thread" + str(num)))

def unzip(zip_directory, unzip_directory):

    files = os.listdir(zip_directory)
    threads = list()

    for ind, f in enumerate(files):
        thread = threading.Thread(target=thread_func,
                                  args=(f, zip_directory, unzip_directory, ind + 1))
        threads.append(thread)
        thread.start()
    print(str(len(threads)) + " started successfully")

    for t in threads:
        t.join()


def move_files(unzip_directory):
    dirs = os.listdir(unzip_directory)
    for d in dirs:
        directory = unzip_directory + '/' + d
        files = os.listdir(directory)
        for f in files:
            try:
                print(f, end='\r', flush=True)
                os.rename(directory + '/' + f, 'tmp/' + f)
            except:
                continue
        os.rmdir(directory)
    files = os.listdir('tmp')
    for f in files:
        os.rename('tmp/' + f, unzip_directory + '/' + f)


def main():

    zip_directory = 'C:/Users/aaron/Downloads/2017 LDS 194 - 200'
    unzip_directory = 'C:/Users/aaron/Downloads/2017 LDS 194 - 200 - Unzipped'
    unzip(zip_directory, unzip_directory)
    move_files(unzip_directory)



if __name__ == '__main__':
    main()