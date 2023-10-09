import os

def is_valid_file_path(file_path):

    # Check if the file path uses either double backslashes or forward slashes
    if "\\" in file_path or "/" in file_path:
        # Check if the file path exists (optional)
        if os.path.exists(file_path):
            return True
        else:
            return False
    else:
        return False

# Test cases
file_path1 = "C:/Users/ychaube/Desktop/lanadelray/pdf-compression-application/LICENSE"  # Valid path with double backslashes
file_path2 = "C:\\Users\\ychaube\\Desktop\\lanadelray\\pdf-compression-application\\LICENSE"      # Valid path with forward slashes
# file_path3 = "C:\Users\User\Documents\file.txt"      # Invalid path with single backslashes

print(is_valid_file_path(file_path1))  # True
print(is_valid_file_path(file_path2))  # True
# print(is_valid_file_path(file_path3))  # False
