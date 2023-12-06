#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#read the dataset into a variable
df = pd.read_csv(r'F:\Data Analytics\New Personal Project - MySQL\all_seasons.csv')

# dropped the index column that came in the dataset
df1= df.drop('Unnamed: 0', axis=1)

df = df1

# Count the number of players who averaged over a specified threshold for each season.

def count_players_above_points_threshold(df, pts):
    # creating a dictionary to store the counts for each season
    season_counts = {}
    
    # loop through unique seasons
    for season in df['season'].unique():
        
        # filter for the current season
        season_df = df[df['season'] == season]
        
        #count the number of players with an average above the pts specified
        count = len(season_df[season_df['pts'] > pts])
        
        # store the count in the dictionary
        season_counts[season] = count
    return season_counts


# using the function above by passing pts and storing the function into a variable called results.

pts = 20
count_results = count_players_above_points_threshold(df, pts)

# prints the results by season in order

print("Number of players averaging over {} in each season:".format(pts))
for season, count in count_results.items():
    print(f"{season}: {count}")


count_avg_player_pts_df = pd.DataFrame(list(count_results.items()), columns =['Season', 'Player_Count'])

df_count = count_avg_player_pts_df

plt.style.use('seaborn-v0_8-darkgrid')
df_count.plot(x = 'Season', y = 'Player_Count', kind = 'line', title = 'Count of Players Average Over 20pts per Season', xlabel = 'Season', ylabel = 'Number of Players')



  # Count the number of players who averaged over a specified threshold for each season.
  # and identify the player with the highest average pts in each season


def player_info_above_threshold(df, pts):
    # creating a dictionary to store the counts for each season
    season_info = []
    
    # loop through unique seasons
    for season in df['season'].unique():
        
        # filter for the current season
        season_df = df[df['season'] == season]
        
        #count the number of players with an average above the pts specified
        count = len(season_df[season_df['pts'] > pts])
        
        # identify the player with the highest points in the current season
        max_player = season_df.loc[season_df['pts'].idxmax(),'player_name']
        
        # append the results to the list
        season_info.append({'Season': season, 'Player_Count': count, 'Top_Scorer': max_player})
        
        # convert the list of dictionaries to a Dataframe
        season_info_df = pd.DataFrame(season_info)
    
    return season_info_df

# passing the arguments into the function and storing into a variable
top_scorer_results = player_info_above_threshold(df, pts)

#printing the dataframe
print(top_scorer_results)

" plotting the count of the top scorers and annotating the top scorer of the season on the graph "

# store results in a readable variable
df_top_scorer = top_scorer_results

#increase the figsize

fig, ax = plt.subplots(figsize=(13,8))

# plot the data
ax.plot(df_top_scorer['Season'], df_top_scorer['Player_Count'], color = 'blue', label = 'Player Count')
ax.scatter(df_top_scorer['Season'], df_top_scorer['Player_Count'], color = 'red', s=50, label = 'Top_Scorer')

# annotate the points with the names of the top scorers 
for i, row in df_top_scorer.iterrows():
    ax.annotate(row['Top_Scorer'], (row['Season'], row['Player_Count']),
                textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color='red')

    
plt.title('Number of Players Averaging Over 20pts Each Season')
plt.xlabel('Season')
plt.ylabel('Player Count')
plt.legend()
plt.xticks(rotation='vertical')
plt.show()

#count of NBA players that averaged over the stated points, assists, and rebounds for each season

def player_stats_above_threshold(df, pts, ast, reb):
    # creating a dictionary to store the counts for each season
    season_info = []
    
    # loop through unique seasons
    for season in df['season'].unique():
        
        # filter for the current season
        season_df = df[df['season'] == season]
        
        #count the number of players with an average above the pts specified
        pts_count = len(season_df[season_df['pts'] > pts])
        ast_count = len(season_df[season_df['ast'] > ast])
        reb_count = len(season_df[season_df['reb'] > reb])
        
        # identify the player with the highest points in the current season
        # max_player = season_df.loc[season_df['pts'].idxmax(),'player_name']
        
        # append the results to the list
        season_info.append({'Season': season, 'Pts_Count': pts_count, 'Ast_Count': ast_count, 'Reb_Count': reb_count })
        
        # convert the list of dictionaries to a Dataframe
        season_info_df = pd.DataFrame(season_info)
    
    return season_info_df

# using the function above by passing pts and storing the function into a variable called results.

count_stats = player_stats_above_threshold(df, 20, 5, 8)

# prints the results by season in order

print(count_stats)


# plotting the count of players that passed a particular stat threshold

count_stats.plot(kind = 'line', x = 'Season')

plt.title("Count of Player That Averaged Over 20pts or 5ast or 8reb Over Season")
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()

#looking at the median points, assists, and rebounds for each season

def player_stats_median(df):
    # creating a dictionary to store the counts for each season
    season_info = []
    
    # loop through unique seasons
    for season in df['season'].unique():
        
        # filter for the current season
        season_df = df[df['season'] == season]
        
        # median stats
        pts_median = season_df['pts'].median()
        ast_median = season_df['ast'].median()
        reb_median = season_df['reb'].median()
        
        
        # append the results to the list
        season_info.append({'Season': season, 'Pts_Median': pts_median, 'Ast_Median': ast_median, 'Reb_Median': reb_median })
        
        # convert the list of dictionaries to a Dataframe
        season_info_df = pd.DataFrame(season_info)
    
    return season_info_df

print(player_stats_median(df))

# looking at the average points, assists, and rebounds each season

def player_stats_average(df):
    # creating a dictionary to store the counts for each season
    season_info = []
    
    # loop through unique seasons
    for season in df['season'].unique():
        
        # filter for the current season
        season_df = df[df['season'] == season]
        
        # average stats
        pts_mean = season_df['pts'].mean()
        ast_mean = season_df['ast'].mean()
        reb_mean = season_df['reb'].mean()
        
        
        # append the results to the list
        season_info.append({'Season': season, 'Avg_Pts': pts_mean, 'Avg_Ast': ast_mean, 'Avg_Reb': reb_mean })
        
        # convert the list of dictionaries to a Dataframe
        season_info_df = pd.DataFrame(season_info)    
    
    return season_info_df

print(player_stats_average(df))

