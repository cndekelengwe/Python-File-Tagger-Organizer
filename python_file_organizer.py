from pathlib import Path 
import subprocess
import plistlib
import subprocess

# Gets files from downlaod and saves it
download_folder = Path.home() / "Downloads" # gets the downloads
# print(user_folder)

# for file in download_folder.iterdir():  # .iterdir() -  allows to loop through 
#     print(file.name)

# basically allows to be saved in apple tag in programming language (needs a different version of python)
# def add_finder_tag(file_path, tag_name):
#     tag_data = [f"{tag_name}\n0"] #weird format in which finder stores tags

#     # Mac-specifi part aka the data in a special Apple formart called Property List (plist)
#     plist_data = plistlib.dumps(tag_data, fmt=plistlib.FMT_BINARY)

#     os.setxattr(
#         file_path,
#         b"com.apple.metadata:_kMDItemUserTags",
#         plist_data
#     )

action = input("Would you like to create a tag or remove a tag? (create/remove): ").lower()
if action == "create":
    def add_finder_tag(file_path, tag_name):
        subprocess.run(
            ["tag", "-a", tag_name, str(file_path)],
            check=True
        )

    while True:
        try:
            file_amt = int(input("Type in how many folder/tag you would like to organize: "))
            break
        except ValueError:
            print("Please make sure to type in a whole number")

    tagged_files = {} 

    for file in range(file_amt):
        # Get the tag/folder name and eventually a list of associated file names
        tag_name = input("Please enter your preferred tag name: ")
        files_name = input("Please enter names associated with the tag name (separated by commas and a space): ")

        file_list = files_name.split(", ") # Split the input at commas
        matched_files = []
        matched_files1 = []

        # loops through files_name given by user 
        for name in file_list:
            #checks names against downloads folder
            for actual_file in download_folder.iterdir():
                # Is it a file?
                if actual_file.is_file():
                    # Does its name contain the keyword?
                    if name.lower() in actual_file.name.lower():
                        matched_files.append(actual_file.name) # .name gives onlt the name of file not its entire tag
                        matched_files1.append(actual_file)
                        
        
        tagged_files[tag_name] = matched_files
        print(tagged_files)
        confirmation = input(f"\nApply the tag '{tag_name}' to all these files? (yes/no): ").lower()
        if confirmation in [ "yes", "y"]:
            print("The files above were tagged")
            for file in matched_files1:
                add_finder_tag(file, tag_name)
                #print("The files above were tagged")
        else:
            print("No files were tagged.")

        tagged_files.clear()




    #Permenanatly saving tag folder

    # if confirmation == "yes":
    #     with open("tags.json", "w") as file:
    #         json.dump(tagged_files, file, indent=4)
    #     print("Tags saved.")
    # else:
    #     print("Changes discarded.")

elif action == "remove":
    tag_name = input("Enter the Tag name to be removed: ")
    def remove_finder_tag(file_path, tag_name):
        subprocess.run(
            ["tag", "-r", tag_name, str(file_path)],
            check=True
        )
    result = subprocess.run( ["tag", "-f", tag_name],capture_output=True, text=True)
    files = result.stdout.splitlines()
    for file in files:
        print(Path(file).name)

    confirmation = input(f"\n Confirming to remove '{tag_name}' assiociated with all these files? (yes/no): ").lower()
    if confirmation in ["yes", "y"]:
        for file in files:
            remove_finder_tag(file,tag_name)        
        
        print(f"\n {tag_name} has been deleted")
    
    else:
        print(f"\n {tag_name} has not been removed")

        

else:
    print("Invalid option")