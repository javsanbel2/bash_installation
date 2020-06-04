#!/usr/bin/env python3

#===============================================================================
# JAVA AND SELENIUM INSTALLATION
# Install pip
# Install selenium
# Install java
#===============================================================================

import os
import requests
import time

def install_java():
    username = "javiernegsb1997@gmail.com"
    password = "Ingles123."
    filename = "jdk-8u251-linux-x64.tar.gz"
    path_jdk_downloaded = os.path.expanduser("~/Downloads/" + filename);
    path_scriptfolder = os.path.expanduser("~/Desktop/scriptfiles");
    
    print("Installing pip...")
    _ = os.system('sudo apt install python-pip')
    os.system("clear")
    
    print("Installing selenium")
    _ = os.system('pip install selenium')
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
    time.sleep(5)
    
    print("Accept cookies")
    iframe = browser.find_element_by_xpath('//*[@title="TrustArc Cookie Consent Manager"]')
    browser.switch_to.frame(iframe);
    button_browser = browser.find_element_by_link_text("I accept all cookies").click()
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
    
    # Move file to our directory
    print("Extract JDK to Java's default location")
    
    _ = os.system("mv " + path_jdk_downloaded + " " + path_scriptfolder);
    
    _ = os.system("sudo mkdir /usr/lib/jvm");
    os.chdir("/usr/lib/jvm")
    _ = os.system("sudo tar -xvzf " + path_scriptfolder + "/" + filename);
    
    print("Set environment variables")
    # TO DO TO DO TO DO TO DO 
    
    print("Inform Ubuntu about the installed location")
    _ = os.system('sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_251/bin/java" 0');
    _ = os.system('sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_251/bin/javac" 0');
    _ = os.system('sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_251/bin/java');
    _ = os.system('sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_251/bin/javac');
    
    print("Setup verification")
    _ = os.system('update-alternatives --list java');
    _ = os.system('update-alternatives --list javac');
    
    #check version
