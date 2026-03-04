import pandas as pd

def clean_data(input_path,output_path):
    df = pd.read_csv(input_path,comment="#")

    print("Original Shape : ",df.shape)

    df["age"] = pd.to_numeric(df["age"],errors="coerce")

    df = df.drop_duplicates()

    df = df.dropna()

    print("Cleaned Shape : ",df.shape)

    df.to_csv(output_path,index=False)
    print("Cleaned file saved successfully!")

if __name__ == "__main__":
    clean_data("Data-Format-Learn/CSV-Format/data/messy_data.csv","Data-Format-Learn/CSV-Format/data/clean_data.csv")
    