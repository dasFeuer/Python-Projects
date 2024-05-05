import os
import shutil
import datetime
import schedule
import time

sourceDir = r"C:\Users\Acer\Pictures\Screenshots"
destinationDir = r"C:\Users\Acer\Pictures\BackUp_SS"

def copyFolderToDirectory(source, dest):
    today = datetime.date.today()
    destDir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, destDir)
        print(f"Folder coiped to: {destDir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("07:32").do(lambda: copyFolderToDirectory(sourceDir, destinationDir))

while True:
    schedule.run_pending()
    time.sleep(60)
# copyFolderToDirectory(sourceDir, destinationDir)