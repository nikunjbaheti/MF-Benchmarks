import os
import glob
import subprocess
from datetime import datetime

# Set the working directory
working_directory = "/home/nikunj/MF_Benchmarks"
log_file = os.path.join(working_directory, "log.txt")

def delete_files():
    # Change to the specified working directory
    os.chdir(working_directory)
    # Get a list of all CSV, LOG, and TXT files in the working directory
    file_types = ["*.csv", "*.log", "*.txt"]
    files_to_delete = []
    for file_type in file_types:
        files_to_delete.extend(glob.glob(file_type))

    # Delete each file and log the deletion
    with open(log_file, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"\n[{timestamp}] Deleting all CSV, LOG, and TXT files...\n")
        
        for file in files_to_delete:
            try:
                os.remove(file)
                log.write(f"[{timestamp}] Deleted: {file}\n")
                print(f"Deleted: {file}")
            except Exception as e:
                log.write(f"[{timestamp}] Error deleting {file}: {e}\n")
                print(f"Error deleting {file}: {e}")

def run_script(script_name):
    # Run the specified Python script and log the output
    try:
        result = subprocess.run(["python", os.path.join(working_directory, script_name)], 
                                check=True, capture_output=True, text=True)
        print(f"Successfully ran: {script_name}")
        
        # Log the success message and script output to log.txt
        with open(log_file, "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] Successfully ran: {script_name}\n")
            log.write(result.stdout + "\n")
            
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        
        # Log the error to log.txt
        with open(log_file, "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] Error running {script_name}:\n{e.stderr}\n")

if __name__ == "__main__":
    delete_files()                 # Step 1: Delete all CSV, LOG, and TXT files
    run_script("MFCode.py")        # Run MFCode.py
    run_script("Benchmark.py")
    run_script("Historical_Returns.py")
    run_script("Index_Latest.py")
    run_script("Peer_Comparison.py")
    run_script("Returns_Data.py")
    run_script("Scheme_Risk.py")
    run_script("commit_files.py")  # Step 3: Run commit_files.py

