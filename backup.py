import shutil
import os
from datatime import datetime
import zipfile

def backup_and_zip_files(source_folder, backup_folder):
    # Ensure the backup folder exists
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    # Create a timestamp for unique folder names
    timestamp = datatime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_zip_filename = os.path.join(backup_folder, f"backup_{timestamp}.zip")
    # create a zip file
    with zipfile.zipFile(backup_zip_ilename, 'W', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the source folder and add files to the zip file
        for root, dirs, files in os.walk(source_folder):
          for file in files:
              # Get full file path
              file_path = os.path.join(root, file)
              # Add file to the zip file wih relative path
              zipf.write(file_path, os.path.relpath(file_path, source_folder))

    print(f"Backup completed and saved as {backup_zip_filename}")


backup_and_zip_files('TEXTS', 'BACKUP')
              
