# Let's open and read the content of the uploaded Jupyter notebook to understand the analysis performed
import nbformat

notebook_path = '/mnt/data/Happiness_code.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Extract and print out a summary of the notebook cells to understand the analysis on Pokémon happiness
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        print(f"Code Cell {i}:\n{cell['source']}\n")
    elif cell['cell_type'] == 'markdown':
        print(f"Markdown Cell {i}:\n{cell['source']}\n")
STDOUT/STDERR
Code Cell 0:
import pandas as pd
pd.get_option("display.max_rows", None)
import matplotlib.pyplot as plt
df = pd.read_csv('pokemon.csv')

Code Cell 1:
df.iloc[773]['defense']

Code Cell 2:

df_happiness=df['base_happiness']
display(df_happiness)

Code Cell 3:




Code Cell 4:
# Sort the DataFrame based on the 'base_happiness' column in ascending order
df_sorted = df.sort_values('base_happiness')

# Count the number of Pokémon for each unique value of 'base_happiness'
pokemon_counts = df_sorted['base_happiness'].value_counts()

# Sort the counts in ascending order based on the 'base_happiness' values
pokemon_counts_sorted = pokemon_counts.sort_index()

# Plot the bar chart
plt.bar(pokemon_counts_sorted.index, pokemon_counts_sorted.values, width=15)
plt.xlabel('Happiness')
plt.ylabel('Number of Pokémon')
plt.title('Number of Pokémon by Happiness')
plt.legend()
plt.show()

Code Cell 5:
# Sort the DataFrame based on the 'base_happiness' column in ascending order
df_legendary = df.sort_values('is_legendary')
df_legendary = df_legendary[df['is_legendary'] != 0]

num_entries = df_legendary.shape[0]
print(num_entries)
# Count the number of Pokémon for each unique value of 'base_happiness'
pokemon_counts = df_legendary['base_happiness'].value_counts()

# Sort the counts in ascending order based on the 'base_happiness' values
pokemon_counts_sorted = pokemon_counts.sort_index()

# Plot the bar chart
plt.bar(pokemon_counts_sorted.index, pokemon_counts_sorted.values, width=8)
plt.xlabel('Happiness')
plt.ylabel('Number of Legendary Pokémon')
plt.title('Happiness of Legendary Pokémon')
plt.legend()
plt.show()

Code Cell 6:
pokemon_count_by_type = df['type1'].value_counts()
pokemon_count_by_type

Code Cell 7:
df_happiness_by_type = df.groupby('type1')[['base_happiness']].mean().sort_values('base_happiness', ascending=False)
df
df_happiness_by_type

plt.figure(figsize=(12, 8))  # Set the figure size for better readability
plt.bar(final_df['type1'], final_df['base_happiness'], color='dodgerblue')  # Create a bar chart
plt.xlabel('Type 1')  # Label for the x-axis
plt.ylabel('base_happiness')  # Label for the y-axis
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.title('base_happiness by Type')  # Title of the graph

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()  # Adjust layout to not cut off labels

plt.show()  # Display the plot



Code Cell 8:
df_experience_growth_by_type = df.groupby('type1')[['experience_growth']].mean().sort_values('experience_growth', ascending=False)
df_experience_growth_by_type

Code Cell 9:
# Group by 'type1' and calculate mean for both 'base_happiness' and 'experience_growth'
grouped_df = df.groupby('type1').agg({'base_happiness':'mean', 'experience_growth':'mean'})

# Sort by 'base_happiness' to maintain the desired order
sorted_df = grouped_df.sort_values('base_happiness', ascending=False)

# Drop the 'base_happiness' column if you only need 'experience_growth' in the final output
final_df = sorted_df.drop(columns=['base_happiness']).reset_index()

final_df

# Calculate the minimum and maximum values for 'experience_growth' with some padding
min_value = final_df['experience_growth'].min() * 0.95  # adding a small buffer by reducing the minimum value by 5%
max_value = final_df['experience_growth'].max() * 1.05  # adding a small buffer by increasing the maximum value by 5%

# Plotting the bar graph
plt.figure(figsize=(12, 8))  # Set the figure size for better readability
plt.bar(final_df['type1'], final_df['experience_growth'], color='dodgerblue')  # Create a bar chart
plt.xlabel('Type 1')  # Label for the x-axis
plt.ylabel('Average Experience Growth')  # Label for the y-axis
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.title('Average Experience Growth by Type')  # Title of the graph

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()  # Adjust layout to not cut off labels

plt.show()  # Display the plot

Code Cell 10:
# Group by 'type1' and calculate mean for both 'base_happiness' and 'experience_growth'
grouped_df = df.groupby('type1').agg({'base_happiness':'mean', 'weight_kg':'mean'})

# Sort by 'base_happiness' to maintain the desired order
sorted_df = grouped_df.sort_values('base_happiness', ascending=False)

# Drop the 'base_happiness' column if you only need 'experience_growth' in the final output
final_df = sorted_df.drop(columns=['base_happiness']).reset_index()

final_df

# Calculate the minimum and maximum values for 'experience_growth' with some padding
min_value = final_df['weight_kg'].min() * 0.95  # adding a small buffer by reducing the minimum value by 5%
max_value = final_df['weight_kg'].max() * 1.05  # adding a small buffer by increasing the maximum value by 5%

# Plotting the bar graph
plt.figure(figsize=(12, 8))  # Set the figure size for better readability
plt.bar(final_df['type1'], final_df['weight_kg'], color='dodgerblue')  # Create a bar chart
plt.xlabel('Type 1')  # Label for the x-axis
plt.ylabel('weight_kg')  # Label for the y-axis
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.title('Average Weight by Type')  # Title of the graph

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()  # Adjust layout to not cut off labels

plt.show()  # Display the plot
print("indicates maybe heavy=unhappy?")

Code Cell 11:
# Group by 'type1' and calculate mean for both 'base_happiness' and 'experience_growth'
grouped_df = df.groupby('type1').agg({'base_happiness':'mean', 'base_total':'mean'})

# Sort by 'base_happiness' to maintain the desired order
sorted_df = grouped_df.sort_values('base_happiness', ascending=False)

# Drop the 'base_happiness' column if you only need 'experience_growth' in the final output
final_df = sorted_df.drop(columns=['base_happiness']).reset_index()

final_df

# Calculate the minimum and maximum values for 'experience_growth' with some padding
min_value = final_df['base_total'].min() * 0.95  # adding a small buffer by reducing the minimum value by 5%
max_value = final_df['base_total'].max() * 1.05  # adding a small buffer by increasing the maximum value by 5%

# Plotting the bar graph
plt.figure(figsize=(12, 8))  # Set the figure size for better readability
plt.bar(final_df['type1'], final_df['base_total'], color='dodgerblue')  # Create a bar chart
plt.xlabel('Type 1')  # Label for the x-axis
plt.ylabel('base_total')  # Label for the y-axis
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.title('Average base_total by Type 1')  # Title of the graph

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()  # Adjust layout to not cut off labels

plt.show()  # Display the plot
print("indicates maybe heavy=unhappy?")

Code Cell 12:
df['capture_rate'] = pd.to_numeric(df['capture_rate'], errors='coerce')

# Proceed with your original code, now that 'capture_rate' has been cleaned
# Group by 'type1' and calculate mean for both 'base_happiness' and 'capture_rate'
grouped_df = df.groupby('type1').agg({'base_happiness':'mean', 'capture_rate':'mean'})

# Sort by 'base_happiness' to maintain the desired order
sorted_df = grouped_df.sort_values('base_happiness', ascending=False)

# Drop the 'base_happiness' column if you only need 'capture_rate' in the final output
final_df = sorted_df.drop(columns=['base_happiness']).reset_index()

# Calculate the minimum and maximum values for 'capture_rate' with some padding
min_value = final_df['capture_rate'].min() * 0.95  # adding a small buffer by reducing the minimum value by 5%
max_value = final_df['capture_rate'].max() * 1.05  # adding a small buffer by increasing the maximum value by 5%

# Plotting the bar graph
plt.figure(figsize=(12, 8))
plt.bar(final_df['type1'], final_df['capture_rate'], color='dodgerblue')
plt.xlabel('Type 1')
plt.ylabel('Average Capture Rate')
plt.xticks(rotation=45, ha="right")
plt.title('Average Capture Rate by Type 1')

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()
plt.show()

Code Cell 13:
df['height_m'] = pd.to_numeric(df['height_m'], errors='coerce')

# Proceed with your original code, now that 'capture_rate' has been cleaned
# Group by 'type1' and calculate mean for both 'base_happiness' and 'capture_rate'
grouped_df = df.groupby('type1').agg({'base_happiness':'mean', 'height_m':'mean'})

# Sort by 'base_happiness' to maintain the desired order
sorted_df = grouped_df.sort_values('base_happiness', ascending=False)

# Drop the 'base_happiness' column if you only need 'capture_rate' in the final output
final_df = sorted_df.drop(columns=['base_happiness']).reset_index()

# Calculate the minimum and maximum values for 'capture_rate' with some padding
min_value = final_df['height_m'].min() * 0.95  # adding a small buffer by reducing the minimum value by 5%
max_value = final_df['height_m'].max() * 1.05  # adding a small buffer by increasing the maximum value by 5%

# Plotting the bar graph
plt.figure(figsize=(12, 8))
plt.bar(final_df['type1'], final_df['height_m'], color='dodgerblue')
plt.xlabel('Type 1')
plt.ylabel('Average height (m)')
plt.xticks(rotation=45, ha="right")
plt.title('Average height by type')

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()
plt.show()

Code Cell 14:
import matplotlib.pyplot as plt

# Corrected line: Ensure you're converting the right column (e.g., 'height_m' or another column)
# df['height_m'] = pd.to_numeric(df['height_m'], errors='coerce') # Assuming you want to convert 'height_m'

# Group by 'generation' and calculate mean for 'base_happiness' (and another metric if needed)
grouped_df = df.groupby('generation').agg({'base_happiness':'mean'}) # Correctly aggregate 'base_happiness'

# Sort by 'base_happiness'
sorted_df = grouped_df.sort_values('base_happiness', ascending=False)

# No need to drop 'base_happiness' if you're plotting it
final_df = sorted_df.reset_index()

# Calculate min and max values for y-axis scaling
min_value = final_df['base_happiness'].min() * 0.95
max_value = final_df['base_happiness'].max() * 1.05

# Plotting the corrected graph
plt.figure(figsize=(12, 8))
plt.bar(final_df['generation'], final_df['base_happiness'], color='dodgerblue')
plt.xlabel('Generation')
plt.ylabel('Average Base Happiness') # Correct label
plt.xticks(rotation=45, ha="right")
plt.title('Average Base Happiness by Generation')

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()
plt.show()

Code Cell 15:
# Filter the DataFrame for Pokémon with type1 as "dark"
dark_type_pokemon = df[df['type1'] == 'dark']

# Group by 'generation' and count the number of Pokémon in each generation
generation_counts = dark_type_pokemon.groupby('generation').size()

# Plotting the results
plt.figure(figsize=(12, 8))
plt.bar(generation_counts.index, generation_counts.values, color='darkgray')
plt.xlabel('Generation')
plt.ylabel('Number of Dark Type Pokémon') # Updated label
plt.xticks(rotation=45, ha="right")
plt.title('Number of Dark Type Pokémon by Generation')

plt.tight_layout()
plt.show()

Code Cell 16:
import matplotlib.pyplot as plt

# Corrected line: Ensure you're converting the right column (e.g., 'height_m' or another column)
# df['height_m'] = pd.to_numeric(df['height_m'], errors='coerce') # Assuming you want to convert 'height_m'

# Group by 'generation' and calculate mean for 'base_happiness' (and another metric if needed)
grouped_df = df.groupby('generation').agg({'capture_rate':'mean'}) # Correctly aggregate 'base_happiness'

# Sort by 'base_happiness'
sorted_df = grouped_df.sort_values('capture_rate', ascending=False)

# No need to drop 'base_happiness' if you're plotting it
final_df = sorted_df.reset_index()

# Calculate min and max values for y-axis scaling
min_value = final_df['capture_rate'].min() * 0.95
max_value = final_df['capture_rate'].max() * 1.05

# Plotting the corrected graph
plt.figure(figsize=(12, 8))
plt.bar(final_df['generation'], final_df['capture_rate'], color='dodgerblue')
plt.xlabel('Generation')
plt.ylabel('Average Capture Rate by Generation') # Correct label
plt.xticks(rotation=45, ha="right")
plt.title('Average Capture Rate by Generation')

# Setting y-axis labels to display as full numbers
plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

# Dynamically setting the y-axis limits for more contrast
plt.ylim(min_value, max_value)

plt.tight_layout()
plt.show()

Code Cell 17:
# Filter the DataFrame for legendary Pokémon only
legendary_pokemon = df[df['is_legendary'] == 1]

# Group by 'generation' and count the number of legendary Pokémon in each generation
legendary_counts = legendary_pokemon.groupby('generation').size()

# Plotting the results
plt.figure(figsize=(12, 8))
plt.bar(legendary_counts.index, legendary_counts.values, color='gold')
plt.xlabel('Generation')
plt.ylabel('Number of Legendary Pokémon')  # Updated label
plt.xticks(rotation=45, ha="right")
plt.title('Number of Legendary Pokémon by Generation')

plt.tight_layout()
plt.show()

Code Cell 18:
import matplotlib.pyplot as plt

# Group by 'generation' and count the total number of Pokémon in each generation
total_counts = df.groupby('generation').size()

# Filter the DataFrame for legendary Pokémon only and group by 'generation' to count them
legendary_counts = df[df['is_legendary'] == 1].groupby('generation').size()

# Calculate the ratio of legendary Pokémon to the total number of Pokémon for each generation
ratios = legendary_counts / total_counts

# Plotting the results
plt.figure(figsize=(12, 8))
plt.bar(ratios.index, ratios.values, color='silver')
plt.xlabel('Generation')
plt.ylabel('Ratio of Legendary Pokémon')  # Updated label
plt.xticks(rotation=45, ha="right")
plt.title('Ratio of Legendary Pokémon to Total Pokémon by Generation')

plt.tight_layout()
plt.show()