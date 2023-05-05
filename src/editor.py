import shutil
import os


def fileInit(file_type: str, file_path: str, columns: tuple):
    """ 
        Create a new file of the specified type if it doesn't exist, and write a header row if the file is a CSV.

    Args:
        file_type: A string representing the type of file to create. Valid options are 'json' and 'csv'.
        file_path: A string representing the path to the file to create.
        columns: A list of strings representing the CSV column names to write to the file.

    Returns:
        None.

    Raises:
        None.

    Example usage:
        fileInit('csv', 'data.csv', ['Name', 'Email', 'Phone'])
    """
    if file_type == 'json':
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('[]')

    elif file_type == 'xlsv':
        pass
    else:
        print("SOMETHING WRONG IN FILE TYPE - editor.py")


def fileCopy(file_path: str, Folder_Name: str, File_Prefix: str):

    try:
        # Create the target directory if it doesn't exist
        target_dir = os.path.join(os.getcwd(), Folder_Name)
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        # Copy the file with a new filename
        new_file_path = os.path.join(
            target_dir, f"{File_Prefix}-{os.path.basename(file_path)}")
        shutil.copy(file_path, new_file_path)

        print("ALL GOOD COPY")
    except FileNotFoundError as fnfe:
        print(f"File not found error: {fnfe}")
        print("SOMETHING WENT WRONG IN FILE COPY")
    except PermissionError as pe:
        print(f"Permission error: {pe}")
        print("SOMETHING WENT WRONG IN FILE COPY")
    except Exception as e:
        print(f"Error copying file: {e}")
        print("SOMETHING WENT WRONG IN FILE COPY")
