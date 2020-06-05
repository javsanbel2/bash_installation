#!/usr/bin/env python3

#===============================================================================
# SCRIPT TO INSTALL THE APP EXPERTS ENVIRONMENT
# The script install the following:
# Python 3.6.8, pip, selenium
# Java JDK 1.8
# Eclipse
#===============================================================================
import multiprocessing
import os
import requests
import time

_ = os.system("sudo touch readme.txt")

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

def wait_until_is_downloaded(path, isDownloaded):
    time.sleep(3)
    if not isDownloaded:
        print("Is downloading")
        downloads = os.listdir(path)
        count = 0
        for file in downloads:
            if file.endswith(".part"):
                count += 1
        if count != 0:
            wait_until_is_downloaded(path, False)
        print("FINISH")  
        
def install_java():
    username = "javiernegsb1997@gmail.com"
    password = "Ingles123."
    filename = "jdk-8u251-linux-x64.tar.gz"
    path_jdk_downloaded = os.path.expanduser("~/Downloads/" + filename);
    path_scriptfolder = os.path.expanduser("~/Desktop/scriptfiles");
    
    print("Installing pip...")
    _ = os.system('sudo apt install python3-pip')
    os.system("clear")
    
    print("Installing selenium")
    _ = os.system('pip3 install selenium')
    os.system("clear")
    from selenium import webdriver
    
    print("Downloading firefox driver...")
    r = requests.get('https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz', allow_redirects=True)
    f = open('geckodriver.tar.gz', 'wb').write(r.content)
    _ = os.system('tar -xf geckodriver.tar.gz'); # Unpack file
    
    print("Downloading Java 1.8")
    _ = os.system('chmod +x ./geckodriver');
    
    print("Creating profile to Firefox")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/x-gzip");
    
    print("Creating Web Driver and go to oracle downloads")
    browser = webdriver.Firefox(firefox_profile=profile, executable_path='./geckodriver')
    browser.get('https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html')
    time.sleep(10)
    
    print("Accept cookies")
    iframe = browser.find_element_by_xpath('//*[@title="TrustArc Cookie Consent Manager"]')
    browser.switch_to.frame(iframe);
    browser.find_element_by_link_text("I accept all cookies").click()
    browser.switch_to.default_content();
    time.sleep(1)
    
    print("Download Linux file")
    browser.find_element_by_xpath('/html/body/div[2]/section[5]/div/div/div/table/tbody/tr[6]/td[3]/div/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div/form/ul/li/label/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div/form/div/div[2]/div/div/a').click()
    time.sleep(5)
    
    print("Sign in and download file")
    browser.find_element_by_xpath('//*[@id="sso_username"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="ssopassword"]').send_keys(password)
    browser.find_element_by_xpath('/html/body/div/div[3]/div[1]/form/div[2]/span/input').click()
    time.sleep(2)
    
    # Wait until is downloaded
    wait_until_is_downloaded(os.path.expanduser("~/Downloads"), False)
    # Move file to our directory
    print("Extract JDK to Java's default location")
    
    _ = os.system("mv " + path_jdk_downloaded + " " + path_scriptfolder);
    
    _ = os.system("sudo mkdir /usr/lib/jvm");
    os.chdir("/usr/lib/jvm")
    _ = os.system("sudo tar -xvzf " + path_scriptfolder + "/" + filename);
    
    print("Set environment variables")
    _ = os.system("echo 'export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/jvm/jdk1.8.0_251/bin:/usr/lib/jvm/jdk1.8.0_251/db/bin:/usr/lib/jvm/jdk1.8.0_251/jre/bin' >> ~/.bashrc");
    _ = os.system("echo 'export J2SDKDIR=/usr/lib/jvm/jdk1.8.0_251' >> ~/.bashrc");
    _ = os.system("echo 'export J2REDIR=/usr/lib/jvm/jdk1.8.0_251/jre' >> ~/.bashrc");
    _ = os.system("echo 'export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_251' >> ~/.bashrc");
    _ = os.system("echo 'export DERBY_HOME=/usr/lib/jvm/jdk1.8.0_251/db' >> ~/.bashrc");
    _ = os.system("exec bash");

    
    print("Inform Ubuntu about the installed location")
    _ = os.system('sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_251/bin/java" 0');
    _ = os.system('sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_251/bin/javac" 0');
    _ = os.system('sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_251/bin/java');
    _ = os.system('sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_251/bin/javac');
    
    print("Setup verification")
    _ = os.system('update-alternatives --list java');
    _ = os.system('update-alternatives --list javac');


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
    
def run_tests():
    _ = os.system('python -m unittest install_test');

if __name__ == '__main__':
    print("Starting environment installation")
    jobs = []
     
    # Python process
    a = multiprocessing.Process(target=install_python)
    jobs.append(a)
    a.start()
    # Java process
    b = multiprocessing.Process(target=install_java)
    jobs.append(b)
    b.start()
    # Eclipse process
    c = multiprocessing.Process(target=install_eclipse)
    jobs.append(c)
    c.start()
    
    a.join()
    b.join()
    c.join()
    
    # Run tests
    run_tests()
     