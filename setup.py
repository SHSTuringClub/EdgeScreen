#! /usr/bin/env python
import os
import sys
import zipfile


def build_ui():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    ui_list = [['entrance.ui', 'ui_ent.py'],
               ['horizontal.ui', 'ui_hor.py'],
               ['vertical.ui', 'ui_ver.py']]
    for i in ui_list:
        if os.system('pyuic5 ui/{} -o {}'.format(i[0], i[1])) != 0:
            print("UI Compile Error! Check if PyQt5 is properly installed!")
            sys.exit(-1)


def make_release():
    build_ui()
    file_list = ['logo_h.png', 'logo_v.png', 'main.py', 'news_class.py',
                 'pic_class.py', 'setup.py', 'timeline.conf.example',
                 'utils.py', 'ui_ent.py', 'ui_hor.py', 'ui_ver.py',
                 'LICENSE']
    fp = zipfile.ZipFile('EdgeScreen_Release.zip', mode='w')
    for i in file_list:
        fp.write(i)
    fp.close()


def print_usage():
    print("Project Edge Screen - Setup System\n"
          "Usage: setup.py [subcommand]\n"
          "Subcommand List: build, release\n"
          "build - Builds the UI files into py. Essential before running the program.\n"
          "release - Makes a runable copy with all the essential files included\n"
          "excluding fonts.\n"
          "Other subcomaand, if any, will give this usage.\n"
          "Copyright: SHS Turing Club\n")

if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        print_usage()
    else:
        if sys.argv[1] == 'build':
            build_ui()
        elif sys.argv[1] == 'release':
            make_release()
