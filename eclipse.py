#!/usr/bin/env python3

#===============================================================================
# ECLIPSE INSTALLATION
#===============================================================================
import os;
import requests;

def install_eclipse():
    URL_ECLIPSE = 'http://mirror.dkm.cz/eclipse/technology/epp/downloads/release/2020-03/R/eclipse-java-2020-03-R-linux-gtk-x86_64.tar.gz'
    USERNAME = os.environ.get('USER')
    
    # Create folder and set that folder as current
    path = os.path.expanduser("~/Desktop/scriptfiles");
    # os.mkdir(path)
    os.chdir(path)
    
    # Download python
    print("Downloading eclipse")
    print("...")
    r = requests.get(URL_ECLIPSE, allow_redirects=True)
    f = open('eclipse.tar.gz', 'wb').write(r.content)
    
    print("Download finished. Starting extraction")
    _ = os.system('tar -xvzf ./eclipse.tar.gz');
    os.system('clear');
    print("Finished")
    
    
    _ = os.system('sudo mkdir /opt/eclipse');
    _ = os.system('sudo chown -R ' + USERNAME + ':' + USERNAME + ' /opt/eclipse');
    _ = os.system('sudo mv ./eclipse/* /opt/eclipse');
    
    print("Eclipse installed and moved to /opt")
