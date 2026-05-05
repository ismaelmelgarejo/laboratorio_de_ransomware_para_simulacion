import os
import shutil

def simulate_encryption(files, output_dir):
    encrypted_files = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in files:
        filename = os.path.basename(file)
        new_name = filename + ".encrypted"

        destination = os.path.join(output_dir, new_name)

        shutil.copy(file, destination)
        encrypted_files.append(destination)

    return encrypted_files