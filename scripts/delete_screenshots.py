import os

def delete_screenshots():
    screenshots_dir = os.path.expanduser("~/Screenshots")
    
    if not os.path.exists(screenshots_dir):
        print("Screenshots directory does not exist.")
        return
    
    files = os.listdir(screenshots_dir)
    
    if not files:
        print("Screenshots directory is empty.")
        return
    
    print("Deleting files in Screenshots directory...")
    for file_name in files:
        file_path = os.path.join(screenshots_dir, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_name}")
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")

if __name__ == "__main__":
    delete_screenshots()
