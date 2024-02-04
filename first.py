import pandas as pd
import logging


logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_csv_file(csv_file):

    # here we Read the CSV file with the given path
    logging.info("Reading csv file from (csv_file)")
    df = pd.read_csv(csv_file)
    logging.info("successfully done reading csv file")
    return df


def saving_to_excel(df, excel_file):

    logging.info("exporting dataframe to excel file (excel_file)")
    df.to_excel(excel_file, index=False)
    logging.info("successfully exported the dataframe to excel")


def read_display(excel_file):

    # Here we specify the number of rows to read
    logging.info("reading 50 rows from the excel file")
    excel_df = pd.read_excel(excel_file, nrows=50)
    logging.info("successfully completed reading 50 rows ")
    # Here we print the rows that we read from Excel
    print(excel_df)


def main():
    try:
        csv_file = '/Users/jaideepsai/Desktop/PYTHON/data-sci/heart.csv'
        excel_file = 'heart_out.xlsx'
        # read csv file
        df = read_csv_file(csv_file)
        # saving dataframe to excell
        saving_to_excel(df, excel_file)
        # reading and printing 50 rows of excel file
        read_display(excel_file)

    except Exception as e:
        # logging.error("application failed and exiting ")
        print("application failed and exiting")


if __name__ == "__main__":
    # Calling the main function
    main()
