import sys, os, glob, traceback
from optparse import OptionParser
from multiprocessing import Process
PY3K = sys.version_info >= (3, 0)

from wget import download

__version__ = "3.2"

def makedir(dir):
    if dir and not os.path.exists(dir):
        os.makedirs(dir)

def fetch_files_from_urls(urls, dir):
    """
    Creates a process for each url in the given urls list. Each process runs in parallel.
    """
    makedir(dir)
    try:
        pool = []
        for url in urls:
            p = Process(target=download, args=(url, dir,))
            p.start()
            pool.append(p)
        for p in pool:
            p.join()
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    # except Exception:
    #     traceback.print_exc(file=sys.stdout)

    # print("removing temporary files from current directory")
    map(os.remove, glob.glob("*.tmp"))


usage = """\
usage: wget.py [options] URLS
URLS is a list of comma separated urls

options:
  -o --output FILE|DIR   output filename or directory
  -h --help
  --version
"""

if __name__ == "__main__":
    if len(sys.argv) < 2 or "-h" in sys.argv or "--help" in sys.argv:
        sys.exit(usage)

    # patch Python 2.x to read unicode from command line
    if not PY3K and sys.platform == "win32":
        sys.argv = win32_utf8_argv()
    # patch Python to write unicode characters to console
    if sys.platform == "win32":
        win32_unicode_console()

    parser = OptionParser()
    parser.add_option("-o", "--output", dest="output")
    (options, args) = parser.parse_args()

    urls = args[0].split(',')
    fetch_files_from_urls(urls, options.output)
    # sys.exit(0)
    # print("Saved under %s" % filename)
