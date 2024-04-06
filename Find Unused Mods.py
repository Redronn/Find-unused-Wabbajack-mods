import os
import shutil

print("This script reads meta files of mods in the folder you specify to determine which\narchives are unused and then "
      "moves them to a folder named Unused Mods.\n")

# prompt for the directory to use
directory = input("Enter path to the modlists download folder that you want to clear unused mods from: ")

# specify the directory for unused mods
unused_mods_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Unused Mods')

# ensure the Unused Mods directory exists
os.makedirs(unused_mods_dir, exist_ok=True)

# iterate over all files in the directory
for filename in os.listdir(directory):
    # check if this is a .meta file
    if filename.endswith('.meta'):
        try:
            # flag to mark if file should be deleted
            should_delete = False
            # open the .meta file
            with open(os.path.join(directory, filename), 'r') as metafile:
                # read the file line by line
                for line in metafile:
                    # check if this line contains 'removed=true'
                    if 'removed=true' in line:
                        # get the name of the corresponding archive file
                        archive_filename = filename.replace('.meta', '')
                        should_delete = True
                        break
            # delete the .meta file if it contains 'removed=true'
            if should_delete:
                os.remove(os.path.join(directory, filename))
                # move the corresponding archive file to the Unused Mods directory
                shutil.move(os.path.join(directory, archive_filename), unused_mods_dir)
        except Exception as e:
            print(f"Couldn't process file {filename} due to error: {e}")
            continue
