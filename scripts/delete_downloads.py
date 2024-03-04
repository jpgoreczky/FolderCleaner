import os

def delete_downloads():
    downloads_dir = os.path.expanduser("~/Downloads")
    
    if not os.path.exists(downloads_dir):
        print("Downloads directory does not exist.")
        return
    
    files = os.listdir(downloads_dir)
    
    if not files:
        print("Downloads directory is empty.")
        return
    
    print("Deleting files in Downloads directory...")
    for file_name in files:
        file_path = os.path.join(downloads_dir, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_name}")
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")

if __name__ == "__main__":
    delete_downloads()
