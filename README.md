# File Handling & Exception Handling Assignment

## Description
This Python program demonstrates **file reading, writing, and error handling**.  
It allows the user to:  
1. Enter a filename to read.  
2. Choose a modification type:  
   - **Uppercase** → converts all text to uppercase.  
   - **Line Numbers** → adds line numbers to each line.  
3. Save the modified content into a new file (`output.txt`).  

## Error Handling
The program gracefully handles:  
- **FileNotFoundError** → if the file does not exist.  
- **PermissionError** → if the file cannot be accessed.  
- **Other exceptions** → unexpected errors.
