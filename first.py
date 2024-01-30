import pandas as pd
def main():
    # here we Read the CSV file with the given path
    csv_file = '/Users/jaideepsai/Desktop/PYTHON/data-sci/heart.csv'
    df = pd.read_csv(csv_file)
    #here the Excel file is created
    excel_file="heart_out.xlsx"
    df.to_excel(excel_file,index=False)
    #Here we specify the number of rows to read
    excel_df=pd.read_excel(excel_file,nrows=50)
    #Here we print the rows that we converted from CSV to Excel
    print(excel_df)

if __name__ == "__main__":
    # Call the main function
    main()