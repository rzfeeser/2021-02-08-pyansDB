#!/usr/bin/env python3
"""learning about moving files and imports"""

import shutil
import os


def main():
    os.chdir('/home/student/pyansDB/')

    shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

    shutil.copytree('5g_research/', '5g_research_backup/')

if __name__ == "__main__":
    main()
