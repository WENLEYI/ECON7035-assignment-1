import pandas as pd
import argparse

def clean_data(input1, input2):
    # Step 1: Merge the input data files based on the ID value
    contact_data = pd.read_csv(input1)
    other_data = pd.read_csv(input2)
    merged_data = pd.merge(contact_data, other_data, left_on='respondent_id', right_on='id', how='inner')
    merged_data.drop('id', axis=1, inplace=True)  # Remove redundant ID column

    # Step 2: Drop rows with missing values
    merged_data.dropna(inplace=True)

    # Step 3: Drop rows if the job value contains 'insurance' or 'Insurance'
    merged_data = merged_data[~merged_data['job'].str.contains('insurance|Insurance')]

    return merged_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='the path to the respondent_contact.csv file')
    parser.add_argument('input2', help='the path to the respondent_other.csv file')
    parser.add_argument('output', help='the path to the output file')
    args = parser.parse_args()

    cleaned_data = clean_data(args.input1, args.input2)
    cleaned_data.to_csv(args.output, index=False)

    print("Output file shape:", cleaned_data.shape)