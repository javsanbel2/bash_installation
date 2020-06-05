import unittest
import os

class InstallTest(unittest.TestCase):
    
    def calculate_size(self, path):
        total_size = 0
        #use the walk() method to navigate through directory tree
        for dirpath, dirnames, filenames in os.walk(path):
            for i in filenames:
                #use join to concatenate all the components of path
                f = os.path.join(dirpath, i)
                #use getsize to generate size in bytes and add it to the total size
                total_size += os.path.getsize(f)
        return total_size/(1024*1024)

    def test_python(self):
        _ = os.system("which python");
        self.assertAlmostEqual(0, 0, msg="Python installation failed")
    
    def test_java(self):
        _ = os.system("java -version");
        self.assertAlmostEqual(0, 0, msg="Java installation failed")
    
    def test_eclipse(self):
        folder_eclipse = "/opt/eclipse"
        correct_size = 230
        actual_size = self.calculate_size(folder_eclipse)
        print(actual_size)
        self.assertTrue(actual_size > 200 and actual_size < correct_size, "Eclipse installation failed")