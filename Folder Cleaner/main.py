import os
from colorama import init, Fore, Style
from tqdm import tqdm

init(autoreset=True)

def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def Move(folderName, files):
    moved = 0
    for file in tqdm(files, desc=f"Moving {folderName}", ncols=75):
        try:
            os.replace(file, f"{folderName}/{file}")
            moved += 1
        except Exception as e:
            print(Fore.RED + f"Error moving {file}: {str(e)}")
    return moved

if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + """
    ╔══════════════════════════════════╗
    ║        FOLDER CLEANER            ║
    ║    Organize Your Files 📂        ║
    ╚══════════════════════════════════╝
    """)

    try:
        files = os.listdir()
        # Remove the script itself from the list if it exists
        if "main.py" in files:
            files.remove("main.py")
        
        # Filter out directories, only keep files
        files = [f for f in files if os.path.isfile(f)]
        
        if not files:
            print(Fore.YELLOW + "\nNo files to organize!")
            exit()

    except Exception as e:
        print(Fore.RED + f"Error accessing directory: {str(e)}")
        exit()

    # Create necessary folders
    folders = ["Images", "Docs", "Media", "Others"]
    for folder in folders:
        CreateIfNotExist(folder)

    # File extensions
    imgExts = [".jpg", ".png", ".webp", ".jpeg", ".gif", ".bmp", ".svg"]
    docExts = [".pdf", ".xlsx", ".txt", ".docx", ".pptx", ".csv", ".rtf"]
    mediaExts = [".mp4", ".mp3", ".wav", ".avi", ".mkv", ".mov", ".wmv"]

    # Categorize files
    image = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    doc = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    
    Other = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            Other.append(file)

    # Move files and collect statistics
    stats = {
        "Images": Move("Images", image),
        "Documents": Move("Docs", doc),
        "Media": Move("Media", media),
        "Others": Move("Others", Other)
    }

    # Print summary
    print(Fore.GREEN + "\nSummary:")
    for category, count in stats.items():
        print(f"{category}: {count} files moved")

    print(Fore.CYAN + "\nFolder cleaning completed! ✨")