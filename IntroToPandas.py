import pandas as pd

print("--- Part 1: Pandas Series ---")
scores = [98500, 87279, 76430, 65126, 54801]
players = pd.Series(scores, index = ["CantCatchMeLol", "Xwkdwm234", "Goated_Gamer7", "johnnyenglish_0235", "TheRealSlimShady"])
print(players)

print()
print("--- Part 2: Pandas DataFrame ---")
data = {
    "Player": ["CantCatchMeLol", "Xwkdwm234", "Goated_Gamer7", "johnnyenglish_0235", "TheRealSlimShady"],
    "Score": [98500, 87279, 76430, 65126, 54801],
    "Wins": [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)

print()
print("--- Part 3: Accessing DataFrame Rows ---")
print("Row 0 (top player):")
print(df.loc[0])
print()
print("Rows 2 and 3 (middle players):")
print(df.loc[2:3])

print()
print("--- Part 4: Reading a CSV File ---")
full_df = pd.read_csv("leaderboard.csv")
print("First 5 rows of the leaderboard (head):")
print(full_df.head())
print()
print("Last 3 rows of the leaderboard (tail):")
print(full_df.tail(3))
print()
print("Dataset information:")
print(full_df.info())

print()
print("--- Part 5: Cleaning Data ---")
print("Rows with missing values removed (dropna):")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('Missing values replaced with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())