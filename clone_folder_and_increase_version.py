import os
import shutil

def update_file_version(file_path, previous_version, new_version):
    print('Updating file:', file_path)
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.replace(f'lesson{previous_version}', f'lesson{new_version}')

    with open(file_path, 'w') as f:
        f.writelines(lines)

def validate_existing_folder(version):
    current_path = os.getcwd()
    lesson_folder = f'lesson{version}'
    if not os.path.exists(os.path.join(current_path, lesson_folder)):
        print("The entered version number is incorrect. Please verify and enter again.")
        return False
    return True

def manipulate_files(previous_version, new_version):
    current_path = os.getcwd()
    previous_lesson = f'lesson{previous_version}'
    new_lesson = f'lesson{new_version}'

    # Copy lesson folder
    shutil.copytree(os.path.join(current_path, previous_lesson), os.path.join(current_path, new_lesson))

    # Rename subfolder
    os.rename(os.path.join(current_path, new_lesson, previous_lesson), os.path.join(current_path, new_lesson, new_lesson))

    # Update manage.py
    manage_py_path = os.path.join(current_path, new_lesson, 'manage.py')
    update_file_version(manage_py_path, previous_version, new_version)

    # Update asgi.py
    asgi_py_path = os.path.join(current_path, new_lesson, new_lesson, 'asgi.py')
    update_file_version(asgi_py_path, previous_version, new_version)

    # Update settings.py
    settings_py_path = os.path.join(current_path, new_lesson, new_lesson, 'settings.py')
    update_file_version(settings_py_path, previous_version, new_version)

    # Update settings.py (second occurrence)
    with open(settings_py_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.replace(f'lesson{previous_version}', f'lesson{new_version}')

    with open(settings_py_path, 'w') as f:
        f.writelines(lines)

def main():
    # Ask for the previous version number
    while True:
        previous_version = int(input("Enter the previous version number: "))
        if validate_existing_folder(previous_version):
            break

    # Calculate new version
    new_version = previous_version + 1

    # Perform file manipulations
    manipulate_files(previous_version, new_version)

    print("File manipulations completed successfully.")

if __name__ == "__main__":
    main()
