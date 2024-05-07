#  # # Folder Cleaner.
import os
# A OS Module function that is create a folder if it does not exist.
def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
# A OS Module function that is used to move the files to the folder.
def Move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
    # A OS Module function that is used to list all the files in the current directory.
    files = os.listdir()
    files.remove("main.py")
    # print(files)

    CreateIfNotExist("Images")
    CreateIfNotExist("Docs")
    CreateIfNotExist("Media")
    CreateIfNotExist("Others")
    # These are used to split the file by extension.
    imgExts = [".jpg",".png"]
    image = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    # print(image)

    docExts = [".pdf", ".xlsx", ".txt", ".docx"]
    doc = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    # print(doc)

    Other = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts ) and os.path.isfile(file):
            Other.append(file)

    # print(Other)

    Move("Images", image)
    Move("Docs", doc)
    Move("Others", Other)

    print("Done")