# ghostBusinessEmailExtractor - version 1.0.0
# For tools contact me: https://t.me/ghostverse
import pandas as pd
import os

def extract_business_emails(input_file, output_file, free_email_domains):
    if not os.path.exists(input_file):
        print(f"Error: The input file '{input_file}' does not exist.")
        return

    # Read the input file into a DataFrame based on its format
    if input_file.lower().endswith('.xlsx'):
        df = pd.read_excel(input_file)
    elif input_file.lower().endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.lower().endswith('.txt'):
        # Read and process emails from the text file
        with open(input_file, 'r') as file:
            emails = file.read().replace('"', '').replace(' ', '').replace(';', '\n').split('\n')
            emails = [email for email in emails if email != '']
        df = pd.DataFrame({'emails': emails})
    else:
        print("Error: Unsupported file format. Please provide a .xlsx, .csv, or .txt file.")
        return

    # Check if 'emails' column exists before applying operations
    if 'emails' in df.columns:
        # Perform operations on the 'emails' column
        df['emails'] = df['emails'].str.lower()
        df = df.drop_duplicates(subset=['emails'])
        df = df[~df['emails'].str.split('@').str[1].isin(free_email_domains)]
        df = df.sort_values(by=['emails'])

        # Save the filtered business emails to the output file
        if not output_file.lower().endswith(('.xlsx', '.csv', '.txt')):
            print("Error: The output file should have .xlsx, .csv, or .txt extension.")
            return
        
        # Format the output file to avoid extra line breaks and spaces
        df.to_csv(output_file, index=False, header=True, line_terminator='\n')

        print(f"\nExtracted business emails have been saved to '{output_file}'.")
    else:
        print("Error: 'emails' column not found in the DataFrame.")
        return

if __name__ == "__main__":
    input_file = input("Enter the name of the email list file (e.g., input.xlsx, input.csv, input.txt): ")
    output_file = input("Enter the name of the output file to save the filtered business emails: ")

    free_email_domains = ["gmail.com", "gmail.ch", "gmail.co", "gmail.com.ng", "gmail.cm", "gmail.com.hk", "gmail.hk", "gmail.org", "@gmail.co.uk", "@gmail.com.au", "@gmail.ca", "@gmail.de", "@gmail.fr", "@gmail.it", "yahoo.com", "yahoo.co.id", "yahoo.fr", "yahoo.co.uk", "yahoo.com.hk", "yahoo.com.tw", "yahoo.com.hk", "yahoo.com.my", "yahoo.ca", "yahoo.com.de", "yahoo.de", "yahoo.co", "yahoo.co.in", "yahoo.co.za", "yahoo.no", "yahoo.it", "yahoo.com.ph", "yahoo.com.es", "yahoo.es", "yahoo.com.au", "yahoo.com.ar", "yahoo.com.br", "yahoo.com.in", "yahoo.com.gr", "yahoo.nz", "yahoo.com.mx", "yahoo.com.sg", "yahoo.sg", "yahoo.in", "yahoo.gr", "yahoo.ie", "yahoo.co.jp", "yahoo.co.ke", "yahoo.ro", "yahoo.com.vn", "yahoo.com.nz", "yahoo.cn", "yahoo.cm", "yahoo.co.kr", "yahoo.org", "yahoo.co.nz", "yahoo.dk", "yahoo.com.cn", "yahoo.co.tz", "yahoo.nl", "yahoo.pl", "yahoo.se", "yahoo.com.my", "yahoomail.com", "yahoo-inc.com", "ymail.com", "aol.com", "aol.co.uk", "aol.de", "hotmail.com", "outlook.com", "outlook.com.au", "outlook.com.br", "outlook.com.ar", "outlook.com.sg", "outlook.com.pe", "outlook.com.mx", "outlook.com.vn", "live.com", "live.co.uk", "live.com.au", "live.ca", "live.de", "live.nl", "live.hk", "verizon.net", "sbcglobal.net", "msn.com", "bellsouth.net", "comcast.net", "att.net", "cox.net", "vtext.com", "qq.com"]  # Add more free email domains if needed

    extract_business_emails(input_file, output_file, free_email_domains)
