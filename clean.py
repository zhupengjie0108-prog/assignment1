import pandas as pd
import sys

def main():
    contact_file = sys.argv[1]
    other_file = sys.argv[2]
    output_file = sys.argv[3]

    df1 = pd.read_csv(contact_file)
    df2 = pd.read_csv(other_file)

    merged = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged = merged.drop(columns=['id'])

    merged = merged.dropna()

    insurance_mask = merged['job'].str.contains('insurance', case=False)
    merged = merged[~insurance_mask]

    merged.to_csv(output_file, index=False)

if __name__ == '__main__':
    main()
