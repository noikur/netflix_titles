# 📦 Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
from collections import Counter

# 🧭 Load the dataset
df = pd.read_csv(r"netflix_titles.csv")

# 🔍 Basic data overview
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.isnull().sum())

# 🧹 Data Cleaning

# 1️⃣ Fill missing countries with 'Unknown'
df['country'] = df['country'].fillna('Unknown')

# 2️⃣ Convert 'date_added' to datetime BEFORE extracting year
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 3️⃣ Extract the year from 'date_added'
df['year_added'] = df['date_added'].dt.year

# ✅ Check that 'year_added' was created properly
print(df['year_added'].head())

# Check unique content types (Movies vs TV Shows)
print(df['type'].value_counts())


# 1️⃣ Content Type Split
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df, palette='Set2')
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()


# 2️⃣ Content Added Over Time
content_by_year = df.groupby('year_added')['show_id'].count().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=content_by_year, x='year_added', y='show_id', marker='o')
plt.title('Content Added Over the Years')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.show()

# ------------------------------------------------------------
# 4️⃣ Most Common Genres
all_genres = df['listed_in'].dropna().str.split(', ')
genre_list = [genre for sublist in all_genres for genre in sublist]
genre_counts = Counter(genre_list).most_common(10)

genre_df = pd.DataFrame(genre_counts, columns=['Genre', 'Count'])

plt.figure(figsize=(10,5))
sns.barplot(x='Count', y='Genre', data=genre_df, palette='cool')
plt.title('Top 10 Genres on Netflix')
plt.show()

# ------------------------------------------------------------
# 5️⃣ Ratings Distribution
plt.figure(figsize=(10,5))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index, palette='magma')
plt.title('Distribution of Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.show()

# ------------------------------------------------------------
# 6️⃣ Interactive Plot (Optional)
fig = px.histogram(df, x='year_added', color='type', barmode='group',
                   title='Netflix Content Added per Year (Interactive)')
fig.show()
