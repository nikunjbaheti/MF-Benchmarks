import os
import glob
import subprocess

def delete_files():
    # Get a list of all CSV, LOG, and TXT files in the current directory
    file_types = ["*.csv", "*.log", "*.txt"]
    files_to_delete = []
    for file_type in file_types:
        files_to_delete.extend(glob.glob(file_type))
    
    # Delete each file
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def run_script(script_name):
    # Run the specified Python script
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"Successfully ran: {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    delete_files()               # Step 1: Delete all CSV, LOG, and TXT files
    run_script("MFCode.py")      # Run MFCode.py
    run_script("Benchmark.py")
    run_script("Historical_Returns.py")
    run_script("Index_Latest.py")
    run_script("Peer_Comparison.py")
    run_script("Returns_Data.py")
    run_script("Scheme_Risk.py")
    run_script("commit_files.py")  # Step 3: Run commit_files.py
