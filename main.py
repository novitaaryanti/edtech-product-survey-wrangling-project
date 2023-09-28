from data_wrangling import *


def main():
    """
    Function that acts as the entry point of the data wrangling program
    """

    # Get the current directory of project workspace
    os.getcwd()

    # Set the folder "data" as the directory to access all raw dataset
    data_path = "data"

    # Call merge_data function
    df = merge_data(data_path)

    # Remove all the duplicate data if any
    df = df.drop_duplicates()

    # Remove the column "Timestamp" as it is unnecessary for the current case of data wrangling
    df = df.drop("Timestamp", axis="columns")

    # Change all the column names to make it easier to access the DataFrame
    # The column names will be named by the question (1 to 10)
    # The column which contains the survey taker's phone number will be named as "user_phone"
    new_col_names = {col_name: str(idx) for idx, col_name in enumerate(df.columns)}
    df = change_columns_name(df, new_col_names)
    df.rename(columns={'0': "user_phone"}, inplace=True)

    # Delete all invalid value which contains a comma followed by option 'D'
    # Call remove_invalid_val
    inv_val = ", D. Tidak memilih semua product"
    df = remove_invalid_val(df, inv_val)

    # Call get_clean_data
    df_clean = get_clean_data(df)

    # Save the cleaned DataFrame as a new CSV file
    output_file_name = "clean_data.csv"
    output_clean_data(df_clean, output_file_name)


if __name__ == "__main__":
    main()
