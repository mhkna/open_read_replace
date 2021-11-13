import shutil
import os
import time
import re

START_ID=17
END_ID=256

def remove_files():
    dir = 'build/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

def build():
    src='example.js'
    x = START_ID
    while x < END_ID+1:
        dst=f'build/{x}.js'
        shutil.copy(src,dst)
        x += 1

def replace():
    x = START_ID
    while x < END_ID+1:
        with open(f'build/{x}.js', 'r+') as f:
            text = f.read()
            find = "'17'"
            replace = f"'{x}'"
            new_text = re.sub(find, replace, text)
            f.seek(0)
            f.write(new_text)
        x+=1

def main():
    print('Removing old files....')
    remove_files()
    time.sleep(1)
    print('Building....')
    build()
    time.sleep(1)
    print('Replacing....')
    replace()
    print('COMPLETE')

if __name__ == '__main__':
    main()
