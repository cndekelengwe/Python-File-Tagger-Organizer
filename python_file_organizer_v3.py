from pathlib import Path
import subprocess

# Folder where the program looks for files
download_folder = Path.home() / "Downloads"


# Adds one Finder tag to one file
def add_finder_tag(file_path, tag_name):
    subprocess.run(
        ["tag", "-a", tag_name, str(file_path)],
        check=True
    )


# Removes one Finder tag from one file
def remove_finder_tag(file_path, tag_name):
    subprocess.run(
        ["tag", "-r", tag_name, str(file_path)],
        check=True
    )


# Returns every file that currently has the given tag
def get_tagged_files(tag_name):
    result = subprocess.run(
        ["tag", "-f", tag_name],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()


# Displays the files connected to a tag
def display_tagged_files(tag_name):
    files = get_tagged_files(tag_name)

    print(f"\nFiles currently tagged with '{tag_name}':")

    if len(files) == 0:
        print("No files are currently using this tag.")
    else:
        for file in files:
            print("-", Path(file).name)

    return files


# Finds files in Downloads using words entered by the user
def find_matching_files():
    words = input(
        "Enter names associated with files you would like to add to tag "
        "(separated by comma and space, such as: Physics, Math): "
    )

    word_list = words.split(", ")
    matched_files = []

    for word in word_list:
        word = word.strip()

        for actual_file in download_folder.iterdir():
            if actual_file.is_file():
                if word.lower() in actual_file.name.lower():
                    if actual_file not in matched_files:
                        matched_files.append(actual_file)

    return matched_files


def yes_or_no(choice):
    while choice not in ["yes", "y", "no", "n"]:

        print("Please enter yes or no.")

        choice = input("Enter yes or no: ").lower()

    return choice


# Shows matched files and lets the user remove unwanted matches
def edit_matched_files(matched_files):
    while True:
        if len(matched_files) == 0:
            print("No files are currently selected.")
            break

        print("\nCurrently selected files:")

        for file in matched_files:
            print("-", file.name)

        choice = input(
            "\nWould you like to remove a file from this list? "
            "(yes/no): "
        ).lower()

        choice = yes_or_no(choice)

        if choice in ["no", "n"]:
            break

        file_name = input(
            "Enter the name of the file you want to remove: "
        )

        file_removed = False

        for file in matched_files:
            if file_name.lower() == file.name.lower():
                matched_files.remove(file)
                file_removed = True
                print(f"{file.name} was removed from the list.")
                break

        if not file_removed:
            print("That file was not found in the selected files.")

    return matched_files


# Adds selected files to a tag
def add_files_to_tag(tag_name):
    matched_files = find_matching_files()

    if len(matched_files) == 0:
        print("\nNo matching files were found.")
        return

    matched_files = edit_matched_files(matched_files)

    if len(matched_files) == 0:
        print("\nThere are no files left to tag.")
        return

    print(f"\nFiles that will receive the '{tag_name}' tag:")

    for file in matched_files:
        print("-", file.name)

    confirmation = input(
        f"\nApply the tag '{tag_name}' to these files? (yes/no): "
    ).lower()

    confirmation = yes_or_no(confirmation)

    if confirmation in ["yes", "y"]:
        for file in matched_files:
            add_finder_tag(file, tag_name)

        print("\nThe files were tagged.")
    else:
        print("\nNo files were tagged.")


# Removes the tag from one specific tagged file
def remove_specific_file(tag_name):
    files = display_tagged_files(tag_name)

    if len(files) == 0:
        return

    file_name = input(
        "\nEnter the name of the file you want removed from this tag: "
    )

    file_found = False

    for file in files:
        file_path = Path(file)

        if file_name.lower() == file_path.name.lower():
            remove_finder_tag(file_path, tag_name)

            print(
                f"\n'{tag_name}' was removed from "
                f"'{file_path.name}'."
            )

            file_found = True
            break

    if not file_found:
        print("\nThat file was not found under this tag.")


def add_specific_file(tag_name):
    file_name = input(
        "\nEnter the name of the file you want to add to this tag: "
    )

    file_found = False

    for file in download_folder.iterdir():
        if file.is_file():
            if file_name.lower() == file.name.lower():
                add_finder_tag(file, tag_name)

                print(
                    f"\n'{tag_name}' was added to "
                    f"'{file.name}'."
                )

                file_found = True
                break

    if not file_found:
        print("\nThat file was not found.")


# Removes a tag from every file using it
def remove_entire_tag(tag_name):
    files = display_tagged_files(tag_name)

    if len(files) == 0:
        return

    confirmation = input(
        f"\nRemove '{tag_name}' from all of these files? "
        "(yes/no): "
    ).lower()

    confirmation = yes_or_no(confirmation)

    if confirmation in ["yes", "y"]:
        for file in files:
            remove_finder_tag(Path(file), tag_name)

        print(f"\n'{tag_name}' was removed from all files.")
    else:
        print(f"\n'{tag_name}' was not removed.")


# Menu used to edit one tag
def edit_tag(tag_name):
    while True:
        if len(display_tagged_files(tag_name)) == 0:
            break

        print("\nWhat would you like to do?")
        print("1. Add files to this tag")
        print("2. Remove a specific file from this tag")
        print("3. Remove this tag from all files")
        print("4. Finish editing this tag")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_specific_file(tag_name)

        elif choice == "2":
            remove_specific_file(tag_name)

        elif choice == "3":
            remove_entire_tag(tag_name)

        elif choice == "4":
            break

        else:
            print("\nPlease choose a number from 1 to 4.")
            continue

        another_file = input(
            "\nWould you like to make another change? (yes/no): "
        ).lower()

        another_file = yes_or_no(another_file)

        if another_file not in ["yes", "y"]:
            break


# Main program
while True:
    action = input(
        "\nWould you like to create, edit, or remove a tag? "
        "(create/edit/remove/quit): "
    ).lower()

    if action == "create":
        tag_name = input("Please enter your preferred tag name: ")

        add_files_to_tag(tag_name)

        another = input(
            "\nWould you like to work with another tag? (yes/no): "
        ).lower()

        another = yes_or_no(another)

        if another not in ["yes", "y"]:
            break

    elif action == "edit":
        tag_name = input("Enter the tag name you would like to edit: ")
        edit_tag(tag_name)

    elif action == "remove":
        tag_name = input("Enter the tag name you would like to remove: ")
        remove_entire_tag(tag_name)

    elif action == "quit":
        break

    else:
        print(
            "\nInvalid option. "
            "Please type create, edit, remove, or quit."
        )