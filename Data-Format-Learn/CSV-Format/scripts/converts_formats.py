import pandas as pd 

def convert_file(input_path):
    df = pd.read_csv(input_path)

    df.to_json("Data-Format-Learn/CSV-Format/data/clean_data1.json",orient="records",indent=4)

    df.to_excel("Data-Format-Learn/CSV-Format/data/clean_data2.xlsx",index=False)

    df.to_parquet("Data-Format-Learn/CSV-Format/data/clean_data3.parquet",engine="pyarrow")

    df.to_html("Data-Format-Learn/CSV-Format/data/clean_data4.html")

    print("All Converted successfully !")

if __name__ == "__main__":
    convert_file("Data-Format-Learn/CSV-Format/data/messy_data.csv")