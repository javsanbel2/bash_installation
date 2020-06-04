#!/usr/bin/env python3

#===============================================================================
# SCRIPT TO INSTALL THE APP EXPERTS ENVIRONMENT
# The script install the following:
# Python 3.6.8, pip, selenium
# Java JDK 1.8
# Eclipse
#===============================================================================

from python import install_python;
from java import install_java;
from eclipse import install_eclipse;


print("Starting environment installation")

print("Installing python")
install_python()

print("Installing java")
install_java()

print("Installing eclipse")
install_eclipse()