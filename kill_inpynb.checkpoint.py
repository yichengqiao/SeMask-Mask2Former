import os
import sys
import shutil


def traverse_and_delete(input_dir, delete_filename='.ipynb_checkpoints'):
    try:
        os.chdir(input_dir)
        print(os.getcwd())
        if delete_filename in os.listdir():
            try:
                shutil.rmtree(os.getcwd() + '\\' + delete_filename)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))

        for i in range(0, len(os.listdir())):
            new_dir = os.getcwd() + '\\' + os.listdir()[i]
            traverse_and_delete(new_dir, delete_filename)
        os.chdir(os.getcwd() + '\\' + '..')

    except OSError as e:
        pass
    return


if __name__ == '__main__':

    traverse_and_delete(os.getcwd() + '\\data')
    '''print(os.getcwd())
    os.chdir(os.getcwd()+'\\'+os.listdir()[0])
    print(os.getcwd())
    os.chdir(os.getcwd() + '\\' + '..')
    print(os.getcwd())'''


