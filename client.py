from ftplib import FTP
import os

# https://pythonspot.com/ftp-client-in-python/
class client:
    def __init__(self, host=None, user=None, pswd=None):
        self.host = host
        self.user = user
        self.pswd = pswd
        self.ftp = None

    def connectToFTP():
        self.ftp = FTP(self.host)    # connect to host
        try:
            ftp.login(self.user, self.pswd)
        except:
            print("Login authentication failed")
        ftp.retrlines('LIST')      # list directory comments

    def quitFTP():
        ftp.quit()

    def cd(path):
        ftp.cwd('/'+path+'/')

    def downloadFile(filepath):
        ext = os.path.splitext(filepath)[1]
        try:
            ftp.retrbinary("RETR " + filepath, open(filepath, "wb"), 1024)
        except:
            print("Download Error: %s", filepath)

    def uploadFile(filepath):
        # parse extension
        ext = os.path.splitext(filepath)[1]
        if ext in (".txt", ".htm", ".html"):
            ftp.storlines("STOR " + filepath, open(filepath))   # storlines = ASCII transfer mode
        else:
            ftp.storbinary("STOR " + filepath, open(filepath, "rb"), 1024)

def main():
    print("attemping FTP connection")
    myclient = client("192.168.1.3", "user", "pass")    # instantiate ftp client
    myclient.connectToFTP;
    print("FTP connection is successful!")

    # should be able to parse user input for the following commands
        # cd
        # pwd
        # get file
        # upload file

    # while true loop with switch statement on user input

    # upload file
    myclient.uploadFile("cat.png")

    # download file
    myclient.downloadFile("dog.png")

main()
