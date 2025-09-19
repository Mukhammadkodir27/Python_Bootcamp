
# ! Pandas 1
# df['column_name'].value_counts().plot(kind='barh')
# df.index
# df.columns
# df.column_name.value_counts()
# df.describe()
# df.column_name.values
# df.info()
# df.column_name.sort_values().head()

# ! Indexing and Filtering
# df = pd.read_csv(csv_path, nrows=5, index_col="id")
# df = pd.read_csv(csv_path, nrows=5, index_col="id", usecols=["id", "artist"])
# or you could select the columns to use
# cols_to_use = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']
# df = pd.read_csv(csv_path, nrows=5, index_col='id', usecols=cols_to_use)
# pd.unique(df['column_name'])

# ! loc and iloc
# df.loc[row_number, "column_name"]
# df.iloc[row_number, column_number]
# df.iloc[:, :] or df.iloc[1:100, -500:-1] or df.iloc[1, :]    #* you need to specify
# df.loc[12:345, 'column_name']  #* check if it works or no

# ! data types of columns (variables)
# type(df['column_name'])
# pd.to_numeric(df['column_name'], errors=coerce)
# df['column_name'] = pd.to_numeric(df['column_name'], errors=coerce)
# df.loc[:, 'column_name'] = pd.to_numeric(df['column_name'], errors=coerce)
# df = df.assign('new_column')  #* used to add a new column to the dataframe

# ! max() and idxmax()
# one is used to return a value while the other to return the index position of that value
# df['column_name'].max()   # * returns max element value
# df['column_name'].idxmax()   # * returns max element value index position
# df.loc[df['column_name'].idxmax(), :]   # * returns all columns where row is max

# ! Filtering
# specific_user = df['students'] == 'Name, Surname'
# specific_user.value_counts()
# df[specific_user]
# real case example
# boy_khamidov = df['students'] == 'Boy, Khamidov'
# boy_khamidov.value_counts()
# df[boy_khamidov]

# ! save df as an excel file
# df.to_excel('location/filename.xlsx')
# df.to_csv('location/filename.csv')

# ! read excel file or sheet
# df = pd.read_excel(excel_path)
# df = pd.read_excel(excel_path, sheet_name='sales', header=None)

# ! random choice, shuffle, sample
# import random
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
# print(random.shuffle([1, 2, 3, 4, 5, 6, 7, 8]))
# print(random.choices([1, 2, 3, 4, 5, 6, 7, 8], k = 2))
# print(random.sample(range(1, 100), 10)) #* from 1 to 100, sample 10 elements

# ! replace
# df['column_name'].replace(to_replace=["yes", "no"], value=[1, 0], inplace=True)

# ! rename columns
# df.rename(columns={'Column_Name': 'New_Column_Name'}, inplace=True)

# ! $75 sign problems in numbers
# pd.to_numeric(df['column_name'])
# df['column_name'].str.replace('$', '')   # * when these is a string like $75.0 pandas cant recognize this

# ! str functions in columns
# df['Column_Name'].str.title()
# df['Column_Name'].str.strip()

# ! astype -> changing data types of variables
# df['column_name'] = df['column_name'].astype(int)
# df['column_name'] = df['column_name'].astype(float)

# ! NA values
# df['column_name'].isna()
# df.column_name.isna().sum()
# df.column_name.isna().sum(axis=0)
# df.column_name.isna().any()
# df.column_name.isna().all()
# df[df.column_name.isna().any(axis=1)]

# ! NOT NA values
# df.notna()  #* opposite for isna()
# df.notna().sum()
# df.notna().sum(axis=0)
# df.notna().all()
# df.notna().any()

# ! duplicated values
# df.duplicated()
# df.duplicated().sum()

# ! drop missing - duplicated values
# df.dropna(inplace = True)
# df.drop_duplicates(inplace = True)
# (skipna = True)

# ! Visualizations of N/A
# plt.figure(figsize=(6, 6))
# sns.heatmap(df.isna())
# sns.heatmap(df.notna())

# ! skipna & fillna
# df['Column_Name'].mean(skipna=True)
# df['Column_Name'] = df['Column_Name'].fillna(
#     df['Column_Name'].mean(skipna=True))
# most_freq = df['Column_Name'].value_counts().idxmax()
# df['Column_Name'] = df['Column_Name'].fillna(most_freq)

# ! Data Inspection
# df.size
# pd.options.display.max_rows = 50
# pd.options.display_min_rows = 10
# # by default they are
# pd.options.display.max_rows = 10
# pd.options.display.min_rows = None

# df.min(numeric_only = True)
# df.max(numeric_only = True)
# df.mean(numeric_only = True)
# df.mean(numeric_only = True).sort_values()
# df.sort_values(by = ['Age', 'Year', 'Grade'])

# ! unique, nunique, nlargest, nsmallest
# df.sort_values(by = 'Column_Name', ascending = True)
# len(df['column_name'].unique())
# df['column_name'].nun
# df['column_name'].nlargest(3)  # * return 3 largest values
# df['column_name'].nsmallest(3)  # * return 3 smallest values

# ! WHERE Statement in df
# df[df['column_Sex'] == 'Male']

# ! Drop Columns & Insert New Columns & Drop Rows & Count() & Rank()
# df.drop(columns='Column_Name', inplace=True)
# df.insert(loc=5, column='New_Column_Name', value=New_Column_Name)
# rows_to_delete = list(range(1, 100))
# df.drop(index = rows_to_delete)

# df.count(axis=0)  # * rows
# df.count(axis=1)  # * columns
# df.count(axis='index')
# df.count(axis=0, numeric_only=True)
# df.count(axis=1, numeric_only=True)

# df['column_name'].rank()
# df['column_name'].rank(numeric_only = True)

#! Matplotlib
# plt.xlabel('X coordinates', fontsize=14, color='blue')
# plt.ylabel('Y coordinates', fontsize=14, color='red')
# df['column_name'].plot(label='Age', color='green', linestyle='--', linewidth=2, marker='d', markersize=7)

# ! Seaborn
# plt.figure(figsize=(5, 5))
# sns.countplot(data = df, x = 'column_name')
# sns.countplot(data = df, y = 'column_name')

# plt.figure(figsize=(5, 5))
# sns.countplot(data=df, x='column_name', hue='column_name')  # * hue -> add column

# plt.figure(figsize=(5, 5))
# sns.set(font_scale=1.5, palette='viridis')
# sns.countplot(data=df, x='column_name', hue='column_name')

# ? scatter plot
# sns.stripplot(data=df, x='column_name', y='column_name', jitter=True, hue='column_name', dodge=True)

# ? kinda scatter plot
# sns.swarmplot(data=df, x='column_name', y='column_name', hue='column_name', dodge=True)

# ? violin plot
# sns.violinplot(data=df, x='column_name', y='column_name', hue='column_name', dodge=True) #* ,split=True

# ? scatter plot and violion plot on the same container or plotting area
# sns.violinplot(data=titanic, x='Sex', y='Age', hue='Pclass', dodge=True)
# sns.swarmplot(data=titanic, x='Sex', y='Age', hue='Pclass', dodge=True, color='black')

# ? bar plot
# sns.barplot(data=titanic, x='Sex', y='Age', hue='Pclass', dodge=True)

# ? point plot
# plt.figure(figsize=(5, 5))
# sns.set(font_scale=1.5, palette='viridis')
# sns.pointplot(data=titanic, x='Pclass', y='Age', hue='Sex', dodge=True)

# ? joint plot - linear regression model
# sns.jointplot(data=titanic, x='Age', y='Fare', height = 6, kind = 'reg')  # * 'kde', 'scatter'
# * by 'reg' we can draw regression line
# * up and right side you can see frequency distribution

# ? linear regression model plot - or logistic regression model
# sns.lmplot(data=titanic, x='Age', y='Fare', aspect=1, height=6, col='Sex')
# * sns.lmplot(data=titanic, x='Age', y='Fare', aspect = 1, height = 6, row = 'Sex')
# * sns.lmplot(data=titanic, x='Age', y='Fare', aspect = 1, height = 6, hue = 'Sex')

# ? linear regression model plot
# sns.lmplot(data=titanic, x='Age', y='Survived', aspect=1, height=6, col='Sex', logistic=True)

# ? cross table
# pd.crosstab(titanic.Sex, titanic.Survived)

# ? heatmap
# sns.heatmap(pd.crosstab(titanic.Sex, titanic.Survived), annot=True, fmt='d', cmap='Reds', vmax=100)
# * vmax -> to set a limit, ex: above 100 is dark red
# * cmap -> color type
