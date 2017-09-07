# Script to import word info from Oxford English Dictionary
# This tool gives all the lexical information about a dictionary word
# Useful NLP tool

import pandas as pd
import requests
import json
import os
import time

language = 'en'
region = 'GB'
word_id = 'word'# insert word

# file.csv is the file that contains 
df_concepts = pd.read_csv("/Users/$USER/file.csv")

for i in range(len(df_concepts)):
    word_id = df_concepts.iloc[i,0]
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/'+ 'regions=' + region
    try:
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}, verify = True)
        data = (r.json())

        print("Fetching json... "+str(word_id))

        with open('/Users/$USER/output.json', 'a') as outfile:
            json.dump(data, outfile)
            outfile.write("\n")
    except:
        print("Couldn't find "+str(word_id)+" in the dictionary.")
    time.sleep(1)