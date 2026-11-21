import numpy as np
import pandas as pd

lt = pd.read_csv("C:\\Users\\meani\\OneDrive\\Documents\\PYTHON LESSONS\\class28\\Class28_football_results.csv")
print(lt.shape)
print(lt.head())
lt.info()
print(lt.describe())

print(lt.isna().sum())
print('Duplicates:', lt.duplicated().sum())
print(lt['team'].value_counts())
print(lt[lt['played'] > 38])

clean = lt.drop_duplicates().copy()
clean['team'] = clean['team'].str.strip().str.upper()
clean['played'] = clean['played'].where(clean['played'] <= 38)

print(len(lt), len(clean))
print(clean['team'].value_counts())
print(clean.isna().sum())
if clean['played'].isna().any():
    clean['played'] = clean['played'].fillna(clean['games_won'] + clean['games_drew'] + clean['games_lost'])

if clean['games_won'].isna().any():
    clean['games_won'] = clean['games_won'].fillna(clean['played'] - (clean['games_drew'] + clean['games_lost']))

if clean['games_drew'].isna().any():
    clean['games_drew'] = clean['games_drew'].fillna(clean['played'] - (clean['games_won'] + clean['games_lost']))

if clean['games_lost'].isna().any():
    clean['games_lost'] = clean['games_lost'].fillna(clean['played'] - (clean['games_won'] + clean['games_drew']))

print(clean.isna().sum())

clean.info()

# ------------QUESTIONS-----------------
print("League winners are:", clean.sort_values("points", ascending=False).head(1)[["team", "points"]])
print("Relegated teams are:", clean.sort_values("points", ascending=False).tail(3)[["team", "points"]])
print("Champions League qualifiers are:", clean.sort_values("points", ascending=False).head(4)[["team", "points"]])
print("Europa League qualifier is:", clean.sort_values("points", ascending=False).head(5).tail(1)[["team", "points"]])
print("Conference League qualifier is:", clean.sort_values("points", ascending=False).head(6).tail(1)[["team", "points"]])

clean.to_csv("C:\\Users\\meani\\OneDrive\\Documents\\PYTHON LESSONS\\class28\\Class28_football_results_clean.csv", index=False)