# Ghost-Business-Email-Extractor
This script is designed for extracting business emails from various input sources, such as Excel files, CSV files, and text files.


### Features:

1. **Input File Compatibility:**
   - The script supports three input file formats: .xlsx (Excel), .csv (CSV), and .txt (Text).

2. **Input File Reading:**
   - The script reads the input file and loads it into a Pandas DataFrame based on its format.

3. **Email Extraction from Text File:**
   - If the input file is a text file (.txt), the script reads and processes emails from the file.

4. **Email Formatting:**
   - The script performs various operations on the 'emails' column, such as converting emails to lowercase, removing duplicates, and filtering out emails with domains listed in the `free_email_domains` list.

5. **Output File Handling:**
   - The filtered business emails are saved to an output file, which the user specifies.
   - The output file format must be one of .xlsx, .csv, or .txt. The script checks for the appropriate extension.

6. **Output File Formatting:**
   - The output file is formatted to avoid extra line breaks and spaces, and it includes a header.

7. **User Interaction:**
   - The script interacts with the user by prompting for the input file name and the output file name.

8. **Error Handling:**
   - The script includes error handling for cases such as non-existent input files, unsupported file formats, missing 'emails' column, and incorrect output file extensions.

9. **Free Email Domain Filtering:**
   - The script uses a predefined list of free email domains (e.g., Gmail, Yahoo, Outlook) to filter out non-business emails.

10. **Version Check:**
    - The main script is conditionally executed only when the script is directly run (not imported as a module).

### How to Use:

1. Run the script.
2. Enter the name of the input email list file when prompted (e.g., input.xlsx, input.csv, input.txt).
3. Enter the name of the output file to save the filtered business emails.
4. The script processes the input file, extracts and filters business emails, and saves them to the specified output file.

**Note:** Users can customize the `free_email_domains` list by adding more free email domains if needed.

This script can be useful for individuals or businesses looking to filter out non-business emails from a given list.
