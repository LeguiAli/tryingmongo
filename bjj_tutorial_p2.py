import pandas as pd
df= pd.read_csv("data_new_sep.csv")

# Correct the column names
df.columns = ['Link', 'Name', 'Sub']
df['Sub'].isna().value_counts()

# We drop the 'None' values because they don't give us any value
df.dropna(subset=['Sub'], inplace=True)
df[['First Name','Last Name','Nickname','Team']] =df['Name'].str.split("|", expand=True)

# Split the 'Sub' column into 'Id', 'Opponent', 'W/L', 'Method', 'Competition', 'Weight', 'Stage', and 'Year'
df[['Id', 'Opponent', 'W/L', 'Method', 'Competition', 'Weight', 'Stage', 'Year']] = df['Sub'].str.split("|", expand=True)

def remove_repeated_substrings(s):
    # get the first half of the string
    first_half = s[:len(s)//2]
    # get the second half
    second_half = s[len(s)//2:]
    # compare the first half with the second half if they are both equal
    # we will only return the first half
    return first_half if first_half == second_half else s

# Apply the function to the 'Opponent' column
df['Opponent'] = df['Opponent'].apply(remove_repeated_substrings)

df= df.dtypes

# Check the unique values of each column (excluding NaN)
unique_values = df.nunique(dropna=True)

# Check for missing values in each column
missing_values = df.isnull().sum()

# Create a summary dataframe
#data_summary = pd.DataFrame({'Data Type': data_types,
#                             'Unique Values': unique_values,
#                             'Missing Values': missing_values})

#data_summary

df= df[df['W/L'].isin(['W', 'L', 'D'])]

# Remove rows where 'Weight', 'Stage', or 'Year' is missing
df= df.dropna(subset=['Weight', 'Stage', 'Year'])