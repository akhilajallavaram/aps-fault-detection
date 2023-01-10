import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_file_path = "aps_failure_training_set1.csv"
database_name = "aps"
collection_name = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f'rows and columns: {df.shape}')

    #convert dataframe to json so that we can dump these record into mongodb
    df.reset_index(drop=True,inplace=True)

    json_record =list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json to mongodb
    client[database_name][collection_name].insert_many(json_record)