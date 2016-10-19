import unittest
from wget import detect_filename, filename_fix_existing
from main import fetch_files_from_urls
import os, shutil

dir = 'downloads'

def remove_dir():
    try:
        # remove dir if present
        shutil.rmtree(dir)
    except Exception:
        pass

class EmptyUrlsTest(unittest.TestCase):
    urls = []

    def test_empty_url_none_dir(self):
        prev = len(os.listdir('.'))
        fetch_files_from_urls(self.urls, None)
        after = len(os.listdir('.'))
        self.assertEqual(prev, after)

    def test_empty_url_dir_not_present(self):
        remove_dir()
            # print("this dir was not present")
        prev = len(os.listdir('.'))
        fetch_files_from_urls(self.urls, dir)
        after = len(os.listdir('.'))
        self.assertEqual(prev + 1, after)

    def test_empty_url_dir_already_present(self):
        remove_dir()
            # print("this dir was not present")
        os.makedirs(dir)
        prev = len(os.listdir('.'))
        fetch_files_from_urls(self.urls, dir)
        after = len(os.listdir('.'))
        self.assertEqual(prev, after)


class NonEmptyUrls(unittest.TestCase):

    def test_file_not_present_download_successful(self):
        urls = ['ftp://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz']
        remove_dir()
        fetch_files_from_urls(urls, dir)
        files = os.listdir(dir)
        for url in urls:
            filename = detect_filename(url, None)
            if filename not in files:
                # file not found,
                self.assertTrue(False)
        self.assertTrue(True)

    def test_file_present_download_successful(self):
        urls = ['ftp://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz']
        remove_dir()
        os.makedirs(dir)
        filenames = []
        for url in urls:
            empty_file = detect_filename(url, None)
            filenames.append(filename_fix_existing(empty_file))
            # create empty dummy files
            f = open(dir+"/"+empty_file, 'w')
            f.close()
        fetch_files_from_urls(urls, dir)
        files = os.listdir(dir)
        for filename in filenames:
            if filename not in files:
                # file not found,
                self.assertTrue(False)
        self.assertTrue(True)

"""
Test cases non-empty:
1. multiple urls, all complete successfully.
2. file alerady present, new file with (1) should be created.
3. one file fails to download. the remaining others should work properly.
4.
"""

if __name__ == '__main__':
    unittest.main()
