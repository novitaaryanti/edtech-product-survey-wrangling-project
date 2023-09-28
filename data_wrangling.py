import os
import pandas as pd


# Dictionary containings all details of available program options from provided questions
dict_program = {
    1: {
        'A': ("Create Analytics Dashboard", "Tutorial Based", "Rp 500.000,0"),
        'B': ("Perform Customer Segmentation", "Mentoring Based", "Rp 350.000,0"),
        'C': ("Design AB Test Experimentation", "Mentoring Based", "Rp 300.000,0")
    },
    2: {
        'A': ("Create Analytics Dashboard", "Tutorial Based", "Rp 500.000,0"),
        'B': ("Design Data Pipeline", "Mentoring Based", "Rp 300.000,0"),
        'C': ("Perform Credit Scoring Analytics", "Mentoring Based", "Rp 550.000,0")
    },
    3: {
        'A': ("Perform Customer Segmentation", "Mentoring Based", "Rp 350.000,0"),
        'B': ("Perform Customer Segmentation", "Tutorial Based", "Rp 450.000,0"),
        'C': ("Design Data Pipeline", "Mentoring Based", "Rp 250.000,0")
    },
    4: {
        'A': ("Design AB Test Experimentation", "Mentoring Based", "Rp 500.000,0"),
        'B': ("Perform Price Optimization", "Tutorial Based", "Rp 350.000,0"),
        'C': ("Perform Credit Scoring Analysis", "Mentoring Based", "Rp 350.000,0")
    },
    5: {
        'A': ("Design Data Pipeline", "Mentoring Based", "Rp 400.000,0"),
        'B': ("Perform Customer Lifetime Analysis", "Tutorial Based", "Rp 300.000,0"),
        'C': ("Design AB Test Experimentation", "Tutorial Based", "Rp 300.000,0")
    },
    6: {
        'A': ("Perform Churn Analytics", "Tutorial Based", "Rp 450.000,0"),
        'B': ("Perform Customer Segmentation", "Mentoring Based", "Rp 300.000,0"),
        'C': ("Create Machine Learning Model", "Mentoring Based", "Rp 300.000,0")
    },
    7: {
        'A': ("Perform Customer Lifetime Analysis", "Tutorial Based", "Rp500.000,0"),
        'B': ("Design Data Pipeline", "Mentoring Based", "Rp 550.000,0"),
        'C': ("Deploy Machine Learning Model", "Tutorial Based", "Rp 350.000,0")
    },
    8: {
        'A': ("Perform Credit Scoring Analytics", "Mentoring Based", "Rp 300.000,0"),
        'B': ("Design Data Pipeline", "Mentoring Based", "Rp 550.000,0"),
        'C': ("Create Machine Learning Model", "Tutorial Based", "Rp 550.000,0")
    },
    9: {
        'A': ("Create Analytics Dashboard", "Mentoring Based", "Rp 250.000,0"),
        'B': ("Design AB Test Experimentation", "Tutorial Based", "Rp 550.000,0"),
        'C': ("Perform Customer Lifetime Analysis", "Mentoring Based", "Rp 350.000,0")
    },
    10: {
        'A': ("Perform Credit Scoring Analytics", "Mentoring Based", "Rp 400.000,0"),
        'B': ("Perform Churn Analytics", "Mentoring Based", "Rp 450.000,0"),
        'C': ("Perform Churn Analytics", "Tutorial Based", "Rp 500.000,0")
    }
}


def merge_data(data_path):
    """
    Function to combine or merge all the available raw datasets

    :param data_path: String containing the directory of raw dataset's folder
    :return: DataFrame as a result of merging all available raw datasets
    """

    # A list container to put all DataFrame obtained from raw datasets
    df_list = []

    # Loop for all items in the 'data' folder
    for file in os.listdir(data_path):
        # If the file in Excel spreadsheet (extension = .xlsx), then read the data using function for Excel
        # Add the obtained DataFrame to the list container
        if file.endswith('.xlsx'):
            df_temp = pd.read_excel(os.path.join(data_path, file))
            df_list.append(df_temp)
        # If the file in CSV (extension = .csv), then read the data using function for CSV
        # Add the obtained DataFrame to the list container
        elif file.endswith('.csv'):
            df_temp = pd.read_csv(os.path.join(data_path, file))
            df_list.append(df_temp)

    # Combine all the DataFrame in the list container
    df_merged = pd.concat(df_list, ignore_index=True)

    # Return the result of DataFrame merging
    return df_merged


def remove_invalid_val(df, inv_val):
    """
    Function to remove all invalid data.
    In this case, the data considered as invalid if the survey taker answers at least one question
    with option 'D' alongside with another option.
    This can be detected by checking if there is a comma in the value alongside with option 'D'.

    :param df: DataFrame to be checked
    :param inv_val: String which indicates whether the value is invalid or not
    :return: DataFrame which has valid values
    """

    # Removing all rows (symbolized as r) if the row contains the invalid value
    # Checked in all columns
    df = df[~df.apply(lambda r: r.str.contains(inv_val)).any(axis="columns")]
    df.reset_index(inplace=True, drop=True)

    return df


def get_program_details(df, df_new):
    """
    Function to get all details about each answers from the survey results.
    Each answered questions by each survey takers will be divided to 3 rows.
    Each for opinion about programs A, B, and C.

    :param df: DataFrame which contains the raw data
    :param df_new: DataFrame which has the criteria or details needed and considered as usable and structured data
    :return: DataFrame which has included the required details
    """

    # Loop for each row while checking each column which contains the question's answer
    for idx, row in df.iterrows():
        for col, val in row.items():
            # Exclude the column contains survey taker's phone number from the loop
            if col != df.columns[0]:
                # Set all choice as 0 for initial choice -> Equal to option 'D'
                choice_ctr = [0, 0, 0]

                # Do the checking one-by-one for option 'A', 'B', 'C'
                # It is acceptable to choose more than one option as long it is not option 'D'
                if 'A' in val:
                    choice_ctr[0] = 1
                if 'B' in val:
                    choice_ctr[1] = 1
                if 'C' in val:
                    choice_ctr[2] = 1

                # Get the details about each program from the program's dictionary
                program_set_a = dict_program[df.columns.get_loc(col)]['A']
                program_set_b = dict_program[df.columns.get_loc(col)]['B']
                program_set_c = dict_program[df.columns.get_loc(col)]['C']

                # Add new data regarding the opinion about each available program from the question
                # The details including 'user_phone', 'choice', 'skill', 'bentuk_program', and 'harga_program'
                # Program A
                df_new.loc[len(df_new.index)] = [df.iloc[idx, 0], choice_ctr[0], program_set_a[0],
                                                 program_set_a[1], program_set_a[2]]
                # Program B
                df_new.loc[len(df_new.index)] = [df.iloc[idx, 0], choice_ctr[1], program_set_b[0],
                                                 program_set_b[1], program_set_b[2]]
                # Program C
                df_new.loc[len(df_new.index)] = [df.iloc[idx, 0], choice_ctr[2], program_set_c[0],
                                                 program_set_c[1], program_set_c[2]]

    # Return the DataFrame which has included the required details
    return df_new


def get_clean_data(df):
    """
    Function to get the cleaned and the usabled DataFrame. The DataFrame will include:
    - user_phone: String containing sensored phone number of user who fill the survey
    - choice: Integer containing the choice of the user about the program (0 as 'No' and 1 as 'Yes')
    - skill: String containing the name of skill program
    - bentuk_program: String containing the type or form of the program (Mentoring / Tutorial based)
    - harga_program: String containing the price of the program in Indonesian Rupiah (IDR)

    :param df: DataFrame which contains the raw data
    :return: DataFrame which has been cleaned and ready to be used
    """

    new_data_template = {"user_phone": [], "choice": [], "skill": [], "bentuk_program": [], "harga_program": []}
    df_clean = pd.DataFrame(new_data_template)

    df_clean = get_program_details(df, df_clean)

    return df_clean


def output_clean_data(df, file_name):
    """
    Function to save the cleaned DataFrame as a CSV file

    :param df: DataFrame which has been cleaned and want to be saved as CSV file
    :param file_name: String containing the name of the expected CSV file
    :return: Show confirmation in which the DataFrame has been saved as a CSV file
    """

    # Save the DataFrame as CSV file with name 'file_name'
    df.to_csv(file_name, index=False)

    # Show the confirmation if the cleaned data has been saved as new CSV file in the intended directory
    return print(f"""
    The result of data wrangling has been saved as {file_name} !
    """)
