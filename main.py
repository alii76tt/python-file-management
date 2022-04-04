from pathlib import Path
from colorama import Fore, init
import os
import platform
import argparse
import shutil

init(autoreset=False)
system = platform.uname()


class MyApp():
    def __init__(self, location=None):
        super(MyApp, self).__init__()

        self.location = location
        os.chdir(location)

        self.pictures = []
        self.videos = []
        self.documents = []
        self.musics = []
        self.archives = []
        self.database = []
        self.website = []
        self.developer = []
        self.system = []
        self.executables = []

        # source https://www.online-convert.com/file-type
        self.thisdict = {
            "picture": ["jpg", "jpeg", "jfif", "pjpeg", "pjp", "png", "svg", "apng", "gif", "avif", "ico", "cur", "tiff", "tif", "bmp", "art", "arw", "dcm", "jp2", "raf", "wbmp", "pct", "webp", "avif", "jxr", "wpg", "odg", "mix"],
            "music": ["mp3", "aac", "ogg", "oga", "aiff", "flac", "alac", "m4a", "wav", "wma", "dsd", "pcm", "mpc", "flac", "m4a", "au", "mp2", "m4p", "m4r", "mpga", "m4b", "3ga", "mpa", "4mp"],
            "video": ["mp4", "avi", "mpeg", "m4v", "mov", "wmv", "mpg", "swf", "3gp", "3g2", "mkv", "ogv", "webm", "asf", "ts", "f4v", "h264", "flv", "3gpp", "amv", "dvsd", "nfv", "mepx"],
            "document": ["pdf", "doc", "docx", "ppt", "pptx", "pptm", "pps", "ppsx", "odt", "xls", "xlsx", "xlsm", "ods", "txt", "xml", "psd", "odt", "chm", "rtf", "sxw", "wpd", "wps", "docm", "pub", "dot", "log", "pages", "dotx", "shs", "msg", "tex"],
            "archive": ["zip", "rar", "7z", "bz2", "gz", "tar", "snb", "jar", "apk", "mht", "tgz", "gzip", "crx", "deb", "rpm", "sitx", "zipx", "sit", "ace", "dd", "r01"],
            "database": ["pdb", "dbf", "bup", "db", "crypt", "accdb", "mdb", "sql", "sqlite3"],
            "website": ["html", "htm", "xhtml", "aspx", "php", "js", "nzb", "json", "do", "css", "webloc", "xfdl", "asp", "cer", "cfm", "csr", "jsp", "rss", "cfml", "mhtml", "webarchive"],
            "developer": ["rc", "p", "d", "c", "class", "cpp", "cs", "dtd", "fla", "h", "java", "lua", "m", "pl", "py", "sh", "sln", "swift", "vcxproj", "xcodeproj", "asc", "bas", "asm", "cbl", "vbp", "xq", "cd", "sb", "b", "hpp", "pass", "ccc"],
            "system": ["clur", "ani", "dvd", "dat", "lnk", "dll", "nfo", "prop", "bin", "cab", "clp", "dmp", "drv", "sys", "cat", "ffo", "dev", "nt", "reg"],
            "executable": ["scr", "exe", "ipa", "app", "bat", "cgi", "com", "gadget", "pif", "vb", "wsf", "cmd", "ds", "air"]
        }

        print(Fore.GREEN + "[+] Scanning the file format...")
        self.getFileList()
        print(Fore.MAGENTA + "[+] Adding file paths to lists.")
        self.checkArray(self.pictures, "_Pictures_")
        self.checkArray(self.videos, "_Videos_")
        self.checkArray(self.documents, "_Documents_")
        self.checkArray(self.musics, "_Musics_")
        self.checkArray(self.archives, "_Archives_")
        self.checkArray(self.database, "_Databases_")
        self.checkArray(self.website, "_Websites_")
        self.checkArray(self.developer, "_Developer_")
        self.checkArray(self.system, "_Systems_")
        self.checkArray(self.executables, "_Executables_")

    # add file path to array

    def appendList(self, arrayList, dictName, dirpath, _file, result):
        for i in self.thisdict[dictName]:
            if result[-1] == i:
                if system.system == "Windows":
                    location = dirpath + "\\" + _file
                elif system.system == "Linux":
                    location = dirpath + "/" + _file
                arrayList.append(location)

    # get file list

    def getFileList(self):
        for dirpath, dirname, filenames in os.walk(os.getcwd()):
            if filenames:
                for _file in filenames:
                    result = _file.split('.')
                    self.appendList(self.pictures, 'picture',
                                    dirpath, _file, result)
                    self.appendList(self.musics, 'music',
                                    dirpath, _file, result)
                    self.appendList(self.videos, 'video',
                                    dirpath, _file, result)
                    self.appendList(self.documents, 'document',
                                    dirpath, _file, result)
                    self.appendList(self.archives, 'archive',
                                    dirpath, _file, result)
                    self.appendList(self.database, 'database',
                                    dirpath, _file, result)
                    self.appendList(self.website, 'website',
                                    dirpath, _file, result)
                    self.appendList(self.developer, 'developer',
                                    dirpath, _file, result)
                    self.appendList(self.system, 'system',
                                    dirpath, _file, result)
                    self.appendList(self.executables, 'executable',
                                    dirpath, _file, result)

    # move files

    def moveFiles(self, files, folderName):
        if system.system == "Windows":
            os.chdir(os.getcwd() + '\\' + folderName)
        elif system.system == "Linux":
            os.chdir(os.getcwd() + '/' + folderName)

        for i in files:
            file = os.path.basename(i)
            _path = os.path.join(os.getcwd(), file)
            try:
                shutil.move(str(i), _path)
            except PermissionError:
                print(Fore.RED + "Permission Error! Run as administrator.")
        print(Fore.LIGHTBLUE_EX + f"[+] The {folderName} file is ready.")

    # create folder

    def checkArray(self, array, folderName):
        print(Fore.YELLOW + "[+] Moving files.")
        if len(array) > 0:
            if os.path.exists(folderName):
                self.moveFiles(array, folderName)
            else:
                os.mkdir(folderName)
                self.moveFiles(array, folderName)
        os.chdir(self.location)


ap = argparse.ArgumentParser(add_help=False)
ap.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                help="""This project is a very simple one with just a python script to automate the process of moving files to different folders by file type.
                            This script uses os and Shutil python modules.
                            It works according to your operating system.""")
ap.add_argument('-t', '--target', type=Path, dest='target',
                help="Enter your target folder. \npython main.py -t '<target_path>'")

args = vars(ap.parse_args())
if args['target'] and os.path.isdir(args['target']):
    try:
        MyApp(args['target'])
        print(Fore.GREEN + "[!] End:  The processing has been finished.")
    except FileNotFoundError:
        print(Fore.RED +
              f"Error: -FileNotFoundError- Please check your target folder. Targer: {args['target']}")
else:
    print(Fore.LIGHTRED_EX + """Enter your target folder. Example:\nWindows:\n python main.py -t 'C:\\Users\\Ali\\Documents\\Python\\Edit Folder App\main' \nLinux:\npython3 main.py -t '/home/ali/folder'""")
