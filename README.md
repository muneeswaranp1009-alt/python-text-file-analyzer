# Python text file analyzer

A beginner friendly python project that analyses a given text file with useful statistics such as the total number of lines, words and characters.

The script reads text file from the projects directory, processes it and outputs the required results to the terminal.

## Features

- Reading from a .txt file

- Counting total lines

- Counting total words

- Counting total characters

- Handling filenotfounderror

- Exception handling

- UTF-8 encoding to read text files

## Technologies

- Python

- The os module

- File handling

- Exception handling

## How it works

This application uses the os module to search for a text file from where the python file is being run.

Once the file is located, the application reads through the file and analyses the file by counting the total number of lines, words and characters in the text file.

The results are then displayed in the terminal.

## Project structure

python-text-file-analyzer/

├── Txt file analyzer.py

└── text.txt

## How to use

1. This project needs python to be installed in your device

2. Clone this repository

3. Make sure Txt file analyzer.py and text.txt are in the same folder

4. cd into the project folder in your terminal

5. Then run the python file by running this command in your terminal

python "Txt file analyzer.py"

6. Finally check your terminal to view the results of the text file analysis.

## Example of what to expect

--- File Analysis: text.txt ---

Total Lines   : [Total line count]

Total Words   : [Total word count]

Total Characters : [Total character count]

## Errors handling

The application handles errors that may occur while reading a file such as file not found error.

The application also handles other generic errors and displays appropriate error messages in the terminal.

## What I learned

I learned how to read text files using python, the os module, string manipulation, counting words, lines and characters, functions, exceptions handling and file organisation among other skills.

## Acknowledgements

This project was developed as part of my python journey to master file handling, string manipulation and other soft skills.

## Possible enhancements

- Allowing users to provide a file path

- Counting total number of sentences in a text file

- Finding the most common words

- Finding the average word length

- Exporting the results to a file

- And many more

## Author

This project was developed as part of my python journey.
