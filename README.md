# ADC (Avada Discord Cleaner)

My program (Owl Tool) detects and removes simple token grabbers in Discord files. 
It checks critical files like index.js and package.json to see if they have been modified maliciously. 
If so, it replaces the files with a safe version. 
The software also closes Discord during cleaning and restarts the application when finished, while creating a log file for each cleaning session.

# False positive

If you have discord modifications like Vencord or BetterDiscord then my program may detect this as a "token grab" since the files are modified so if this happens change your password so as not to have any doubts.


## Installation (Beginner people)

1. First put the folder on ur desktop.
2. Second you do have the latest version of python installed on ur machine.
3. Third double click on "run.bat" and its gonna install dependancies + run the program ^^

## Installation (Intermediate people)
```bash
  pip install -r requirements.txt
  python3 main.py
```
## Credits

Made entirely with <3.

- Avada Kedavra (me)

## Usage

Its free and open-source project so you can use as ur own but dont forgot to put me in credits :)

