import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("C:\\Users\\kyles\\Documents\\app1\\files\\bonuses\\compressed.zip",
                    "C:\\Users\\kyles\\Documents\\app1\\files\\bonuses\\files\\dest")