#!/usr/bin/env python3

import os
import requests

def install_python():
    # Create folder and set that folder as current
    path = os.path.expanduser("~/Desktop/scriptfiles");
    os.mkdir(path)
    os.chdir(path)
    
    # Download python
    print("Downloading python")
    r = requests.get('https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz', allow_redirects=True)
    f = open('Python.tgz', 'wb').write(r.content)
    
    # Unpack file
    _ = os.system('tar zxvf ./Python.tgz');
    if _ != 0: print("Error");
    
    # Assign current route to Python folder
    path_python = os.path.expanduser("~/Desktop/scriptfiles/Python-3.6.8");
    os.chdir(path_python);
    
    os.system("clear")
    print("Installing build essentials")
    # Install build essentials (compiler C) and unpacker
    _ = os.system("sudo apt install build-essential");
    os.system("clear")
    _ = os.system("sudo apt install zlib1g-dev");
    print("Installing zlib unpacker")
    
    os.system("clear")
    print("Building python file...")
    
    # Build Python file
    _ = os.system("./configure --enable-shared --with-zlib=/usr/include --enable-optimizations --prefix=" + path_python);
    _ = os.system("make build-all"); #1min build_all to speed up make
    #_ = os.system("make test"); slow
    _ = os.system("make install");
    
    # Set environment variables
    _ = os.system("echo 'export PATH=~/Desktop/scriptfiles/Python-3.6.8:$PATH' >> ~/.bashrc");
    _ = os.system("echo 'export LD_LIBRARY_PATH=~/Desktop/scriptfiles/Python-3.6.8/lib:$LD_LIBRARY_PATH' >> ~/.bashrc");
    _ = os.system("exec bash");
