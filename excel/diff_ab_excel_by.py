import os
import argparse
import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Output the difference between excels files given a target column")
    parser.add_argument("--a-file", type=str,
                        help="File path name for reduced file")
    parser.add_argument("--b-file", type=str,
                         help="File path name for reduced by file")
    parser.add_argument("--out-file", type=str,
                        help="Output file path to write the difference between a-file and b-file given the target-column contents in each row")
    parser.add_argument("--target-column", type=str,
                        help="Target column to remove rows from a-file when the contents are equal to the ones in b-file")

    args = parser.parse_args()
    

    assert os.path.exists(args.a_file), \
        f"{args.a_file} doesn't exists"

    assert os.path.exists(args.b_file), \
            f"{args.b_file} doesn't exists"
    
    df_a = pd.read_excel(args.a_file, engine='openpyxl')
    df_b = pd.read_excel(args.b_file, engine='openpyxl')

    assert args.target_column in df_a.columns, \
        f"There isn't a column named {args.target_column} in {a_filepath}"
    assert args.target_column in df_b.columns, \
        f"There isn't a column named {args.target_column} in {b_filepath}"
    
    df_a = df_a[~df_a[args.target_column].isin(df_b[args.target_column])]
    df_a.to_excel(args.out_file, index=False)
                
