import pandas as pd
import os

current_dir = os.getcwd()

file_list = os.listdir(current_dir)

# print(file_list)

df_list = []

for file in file_list:
    if file.endswith(".csv"):
        file_path = os.path.join(current_dir, file)
        # print(file_path)
        df = pd.read_csv(file_path, index_col=False)
        df_list.append(df)

con_df = pd.concat(df_list)

total_reviews = len(con_df)
valid_reviews = con_df.dropna()
invalid_reviews = total_reviews-len(valid_reviews)
prod_list = con_df['Product ID'].unique()

dict = {}

for prod_id in prod_list:
    ratings = con_df[con_df['Product ID']==prod_id]['Review Rating']
    avg_rating = float(ratings.mean())
    dict[prod_id] = avg_rating

avg_rating = sorted(dict.values())

top_3_dict = {}

for i in range(4):
    i = i+1
    key = list({j for j in dict if dict[j]==avg_rating[-i]})
    top_prod = key[0]
    top_3_dict[top_prod] = avg_rating[-i]


with open('summary.txt', 'w') as file:
    file.write("The Total Number of reviews processed: {}\n".format(total_reviews))
    file.write("The Total Number of valid reviews {}\n".format(len(valid_reviews)))
    file.write("The Total Number of invalid reviews {}\n".format(invalid_reviews))
    for key, value in list(top_3_dict.items()):
        file.write("Product ID: {}, Average Rating: {}\n".format(key, value))