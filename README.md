# Python-File-Tagger-Organizer
## Overview
The Python File Tag Organizer is a command-line application designed to help users organize files on macOS using Finder tags instead of moving files into folders. Rather than changing an existing folder structure, the program allows users to assign meaningful custom tags to files based on keywords they provide.

Unlike traditional folder-based organization, a single file can belong to multiple categories without being duplicated or moved. This makes it easy to locate related files while preserving the user’s existing organization system.

## Purpose
The purpose of this project is to provide a simple, flexible, and non-destructive way to organize files. Many users already have a folder structure they are comfortable with, but finding related files across different folders can still be difficult. By applying Finder tags, this program lets users categorize files without changing their locations.

The application automatically searches for matching files, allows users to review the results before making any changes, and then creates or removes Finder tags based on the user’s confirmation. This approach keeps files in their original locations while making them easier to search, filter, and organize within Finder.

## Features
  * Create custom Finder tags for matching files.
  * Remove existing Finder tags from files.
  * Search for files using user-provided keywords.
  * Preview matching files before applying any changes.
  * Keep files in their original locations without creating duplicates or moving them.
  * Allow a single file to belong to multiple categories through multiple Finder tags.


## Installation Guide
**Requirements**
Before running the program, make sure you have the following installed:
  Python 3.10 or later (installation instructions included below if needed).
  Homebrew (installation instructions included below if needed).
  The tag command-line utility (installation instructions included below).
  macOS (Finder tags are only supported on macOS).
**Note:** Throughout this guide, anything written in italics (for example: _hi_) is a command that should be typed directly into the Terminal.

**Step-By_Step Processs**

1. Download the Project, which can be found named as python_file_organizer.py in the main directory. Save the Python file in a folder that you can easily locate later. Ensure the file is saved with the .py extension.

2. Open the Terminal application on your Mac.
3. Type the following command into Terminal:
   
   ```_python3 --version_```

     a. If your Python version is 3.10 or later, skip to step 4.
   
     b. If you do not have Python 3.10 or later installed, download and install the latest version from:
        https://www.python.org/downloads/macos/
   
5. Install Homebrew (Only if Needed)
   
     a. First, try installing the tag utility by typing: _brew install tag_
        If you didn't receive an error, skip to step 5. But if you receive the error: zsh: command not found: brew
        then Homebrew is not installed.
   
     b. Install Homebrew by entering:
   
       ```_/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"_```


Once the installation is complete, Homebrew will display additional setup instructions.

Step 5: Add Homebrew to Your Terminal Path

Your username appears at the beginning of each Terminal line.

Example:

candacendekelengwe@Candaces-MacBook-Air

In this example, the username is:

candacendekelengwe

Replace username in the commands below with your own username.

Run each command one at a time:

echo >> /Users/username/.zprofile

Example:

echo >> /Users/candacendekelengwe/.zprofile

Next, type:

echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> /Users/username/.zprofile

Finally, type:

eval "$(/opt/homebrew/bin/brew shellenv zsh)"

To verify that Homebrew was installed successfully, type:

brew --version

If Homebrew is installed correctly, a version number will be displayed. The exact version may vary depending on when it was installed.

Step 6: Install the Tag Utility

Type:

brew install tag

Wait for the installation to finish before continuing.

Step 7: Navigate to the Project Folder

To determine your current directory, type:

pwd

Locate the folder containing your Python program.

Then use the cd command to navigate to that folder.

For example:

cd Downloads/File_organizer

You can easily find the folder path by opening Finder and locating your project folder.

Step 8: Run the Program

Run the program using:

python3 filename.py

Replace filename.py with the name of your Python file.

Example:

python3 python_file_organizer.py

The program will then guide you through c

