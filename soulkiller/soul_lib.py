from datasets import load_dataset
import threading
import pandas as pd

# Creates a new column with the data you want as a DF and appends to another DF
def process_column(data, phase, column, result):
    new_data = pd.DataFrame(data[phase][column], columns=[column])
    result.append(new_data)


def data_2_pd(tag, phase):
    # Loads a dataset from Hugging Face
    data = load_dataset(tag)
    # Converts the features of a  dataset to a list for EZ use
    features = list(data[phase].features)
    # Creates a new dataset using the features as columns
    df = pd.DataFrame(columns=features)
    print("Converting to Pandas Dataframe")

    # spot for threads to vibe
    threads = []
    # spot to put the result back together
    result = []
    for column in df.columns:
        # Creates a thread telling it to run process column
        thread = threading.Thread(target=process_column, args=(data, phase, column, result))
        # appends the thread to the threads ls
        threads.append(thread)
        # starts running
        thread.start()

    # Joins all the threads together
    for thread in threads:
        thread.join()
    # combines the items from result and makes it a dataframe
    df = pd.concat(result, axis=1)

    return df

def test():
    print('up')

