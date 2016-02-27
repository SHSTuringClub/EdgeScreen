#! /usr/bin/env python
if __name__ == '__main__':
    import os
    import sys

    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    ui_list = [['entrance.ui', 'ui_ent.py'],
               ['horizontal.ui', 'ui_hor.py'],
               ['vertical.ui', 'ui_ver.py']]
    for i in ui_list:
        if os.system('pyuic5 ui/{} -o {}'.format(i[0], i[1])) != 0:
            print("UI Compile error!")
            sys.exit(-1)
