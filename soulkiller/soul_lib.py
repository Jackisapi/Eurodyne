from datasets import load_dataset
import pandas as pd 


def data_2_pd(tag,phase):
    data = load_dataset(tag)
    features = list(data[phase].features)
    print(features)
    df = pd.DataFrame(columns=features)
    print(df)
    for column in df.columns:
        for item in data[phase][column]:
            row = pd.DataFrame({column:item})
            df.append(row)
            print(df)


data_2_pd('imdb','train')
