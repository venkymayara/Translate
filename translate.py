# pip install google_trans_new 
# pip install pandas



import pandas as pd
from google_trans_new import google_translator



data = pd.read_csv("hindi.csv")
print(data)



translator = google_translator()
translations = {}
# print(data.columns)
for column in data.columns:
    unique = data[column].unique()
    for element in unique:
        translations[element] = translator.translate(element, lang_tgt='ar')         #lang_tgt='ta'

for i in translations.items():
    print(i)



data.replace(translations, inplace=True)
print(data)


