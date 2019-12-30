#%% 
import pandas as pd

#%%
file_path = r"path"

df = pd.read_csv(file_path,sep='\t')
df



# %%
df.head()

# %%
df = df.drop(columns = ['Notes', 'State Code','Year Code','Crude Rate'])

# %%
df = df.dropna(how = "all")

# %%
df.head(20)

# %%
base_df = df.groupby(['Year','State']).sum().reset_index()

# %%
base_df.head(10)

# %%
by_race_file_path = r"path"

df_byRace = pd.read_csv(by_race_file_path, sep= '\t')
# %%
df_byRace

# %%
df_byRace = df_byRace.drop(columns = ['Notes', 'State Code','Year Code','Population','Crude Rate','Race Code'])


# %%
df_byRace = df_byRace.dropna(how= 'all')

# %%
df_byRace.head(10)

# %%
df_byRace.Race.unique()

# %%
df_byRace.groupby(['Year','State']).sum().reset_index()


# %%

df_byRace[df_byRace['State'] == "Alaska"]

# %%
base_df

# %%
df.loc[df['State']== 'Alaska']

#%%

# %%
base_df['Black or African American_Death'] 

#%%

df_byRace[df_byRace['Year'] == 1999.0][df_byRace["State"] == "Alabama"][df_byRace['Race']=='Black or African American']['Deaths']

# %%
