import pandas as pd

#---------Load-----
input_path= "C:/Users/Dr Junaid/Downloads/SQLiV3.csv.zip"
output_path= "C:/Users/Dr Junaid/Desktop/mysql/SQLiV3_cleaned.csv"
df= pd.read_csv(
    input_path,
    usecols=[0, 1],
    names= ['sentence', 'label'],
    header= 0,
    encoding= 'utf-8',
    on_bad_lines= 'skip'
)

#----------clean---------
df= df.dropna(subset= ['sentence'])                         # reomve empty sentence
df['sentence']= df['sentence'].astype(str).str.strip()      # trim whitespace
df= df.drop_duplicates(subset=['sentence'])                 # remove duplicate rows
df['label'] = pd.to_numeric(df['label'], errors= 'coerce')   # force label to numeric
df= df.dropna(subset=['label'])                             # drop rows with bad labels
df['label'] = df['label'].astype(int)                       


#------- save cleaned file-----------
df.to_csv(output_path, index= False)
print(f"cleaned file saved to: {output_path}")


#-------Analysis-------
print("\n--- Dataset shape---")
print(df.shape)

print("\n--- First 5 rowa---")
print(df.head())

print("\n--- label Distribution---")
print(df['label'].value_counts())

print("\n--- Average sentence Length---")
print (df['sentence'].str.len().mean())

print("\n--- Shortest Sentence---")
print (df.loc[df['sentence'].str.len().idxmin(), 'sentence'])

print("\n--- Longest Sentence---")
print (df.loc[df['sentence'].str.len().idxmax(), 'sentence'])