#!/usr/bin/env python3

#===============================================================================
# SCRIPT TO INSTALL THE APP EXPERTS ENVIRONMENT
# The script install the following:
# Python 3.6.8, pip, selenium
# Java JDK 1.8
# Eclipse
#===============================================================================
import multiprocessing
from python import install_python;
from java import install_java;
from eclipse import install_eclipse;


if __name__ == '__main__':
    print("Starting environment installation")
    jobs = []
     
    # Python process
    p = multiprocessing.Process(target=install_python)
    jobs.append(p)
    p.start()
    # Java process
    p = multiprocessing.Process(target=install_java)
    jobs.append(p)
    p.start()
    # Eclipse process
    p = multiprocessing.Process(target=install_eclipse)
    jobs.append(p)
    p.start()
     
