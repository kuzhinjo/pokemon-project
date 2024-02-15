# Pokemon Project
> Authored by: Aditya Jamwal, Rajeev Kuzhinjedath, Matthew Sanders, Marshall Mayers, Eric Pugh, Trey Brewer
## Installation



### Steps:
- Import CSV into Google Colab (https://colab.research.google.com)
- Each file in the repo will contain differant aspects and research that is contained in the presentation, most files have the same dependecies (pandas, matplotlib)
- Install the dependencies for any given file
- Run all cells to see outputs generated

## Features
 > Each feature represents comparsions against various points of data
- Correlations between various rows of data
- Scatter plots
- Box plots
- Bar Graphs
- Linear Regression

## Analysis
1.) Height/Weight (Rajeev)

2.) Type (Trey)
2.) Type
Type analysis was focused on attack, defense, and capture rate as it correlates to the types of Pokemon.  We believe this is important to understand because if we are constructing a Pokemon team we would want to know how to build our attack and defense line up accordingly and how difficult it would be to capture these pokemon.

* Data Preparation
    1. We began by building a dataframe which consisted of type, sub type, attack, defense, and capture along with other base stats.  We had to account for the fact that not every Pokemon had a subtype.

* Exploratory Data Analysis
    1. Type with highest attack:
        * We created a bar graph depicting the highest attack value on average by type
        * We also created a bar graph depicting the highest attack value on average for the the sub type
    2. Type with highest defense:
        * We created a bar graph depicting the highest defense value on average by type
        * We also created a bar graph depicting the hightest defense value for sub type
    3. Capture Rate:
        * Created a bar graph depicting the capture rate for the highest rated attack/defense types of Pokemon
* Findings
    1. We discovered that the Pokemon Type Dragon and more specifically the sub type Electric Dragons would have the highest attack value on average
    2. We also discovered that the type Steel Pokemon would have the highest Defense value on average and the electric sub type has the highest defense on average as well.
    
In summary we are seeing Dragon and Steel Pokemon are the top Pokemon for attack and defense as well as the eletric sub type for each average the highest defense

3.) Happiness (Marshall)

4.) Legendary pokemon (Matthew)

5.) Weight (Aditya)

In this weight analysis, we explore the relationship between weight and other base stats of Pokémon in our dataset. Specifically, we focus on the correlation between weight and attack, defense, and hit points (HP). Understanding these stats is crucial for assessing a Pokémon’s abilities and potential success in battles.

* Data Preparation
    1. Handling Missing Values: Initially, we encountered missing weight values. To address this, we replaced these missing entries with zeroes. For instance, certain ghost-type Pokémon have no weight, and this adjustment ensures consistency in our analysis.
 
* Exploratory Data Analysis
    1. Weight Distribution:
        * We created a box plot to visualize the distribution of Pokémon weights.
        * The upper bound of the box plot was 141.65 kilograms.
        * We observed several outliers above this upper bound. As outliers can distort results, we removed them from further analysis.
         
* Linear Regression Analysis
    1. Weight vs. Attack:
        * We performed linear regression between weight and attack values.
        * The regression equation is: Weight = 0.5 * Attack - 3.4.
        * The correlation coefficient ® for this regression was 0.45.
    2. Weight vs. Defense:
        * Similarly, we conducted linear regression between weight and defense values.
        * The regression equation is: Weight = 0.5 * Defense - 2.3.
        * The correlation coefficient ® for this regression was 0.43.
    3. Weight vs. Hit Points (HP):
        * Finally, we explored the relationship between weight and HP.
        * The regression equation is: Weight = 0.6 * HP - 5.7.
        * The correlation coefficient ® for this regression was also 0.43.
          
* Findings and Implications
    * Weight and Attack: There is a moderate positive correlation between weight and attack. Heavier Pokémon tend to have higher attack stats.
    * Weight and Defense: A similar trend exists between weight and defense. Heavier Pokémon often exhibit stronger defensive capabilities.
    * Weight and HP: While the correlation is not as strong, weight still plays a role in determining HP. Heavier Pokémon may have slightly higher hit points.
      
In summary, understanding the interplay between weight and base stats can inform strategic decisions when assembling a Pokémon team. Trainers should consider these relationships to optimize battle performance.

3. The Impacts of Happiness

File Name: Happiness_code.ipynb

Findings and Implications:

    -Legendary Pokemon tend to be less happy
    Legendary Pokemon come at a price

    -The vast majority of Pokemon have an average base happiness level, with the bell curve naturally skewed towards “less happy”
    Most Pokemon have average happiness levels, with the bell curve naturally skewed towards “less happy”

    -Generally speaking, the “darker” the Pokemon’s demographic, the higher the average experience growth
    This could mean that darker Pokemon have more incentive for personal growth, or that hardship tends to build experience more quickly

    -Over the generations, base happiness averages are trending downwards, while the number of legendary pokemon is trending upward
    This furthers the suggestion that in soma capacity, legendary status is linked to base happiness

    -On average, the “darker” the Pokemon’s demographic, the less happy they are.
    This makes sense

    -High attack seems to, in some capacity, be related to happiness, less happy Pokemon generally have higher attack abilities

In summary, the base happiness of the pokemon you choose to have on your team can have an impactful effect, and the choice made should be driven by your gameplay style or intentions. If you're building a team with a focus on enduring and survival, Pokemon happiness will play into the bond you’re able to build with your Pokémon. For competitive play, there are strategic implications of in relevance to evolution & move effectiveness












## Assigned Tasks 
1) Aditya - size/power scatter/bar graphs
2) Marshall - Happiness scatter/bar graphs
3) Trey - Types scatter/bar graphs
4)  Matthew - is_legendary scattter/bar graphs
5)  Rajeev - [height/weight correlated to base stats](#5-height--weight-of-a-pokemon-correlate-with-its-various-base-stats)
6)  Eric - Narrative of case study (Thomas AI)


### 5. Height & Weight of a Pokemon Correlate with its various base stats

**File Name**: Pokemon-hw-corr.ipynb

**Findings**: There is a positive correlation with Height/Weight with Pokemon’s various other base stats like Hit Points/ Attack/ Defense/ Special Attack/ Special Defence/ Speed

- Height Vs Weight is having a strong positive correlation
- Height & Weight is having relatively similar positive correlation with all other base stats

![Alt text](<https://github.com/kuzhinjo/pokemon-project/blob/rajeev_branch/images/corr_h_vs_w_1.png>)

**Findings**: 
- Most of the base stats fall under height 5ft
- Most of the base stats fall under weight 200 kg

![Alt text](<https://github.com/kuzhinjo/pokemon-project/blob/rajeev_branch/images/corr_h_vs_w_2.png>)

## Tech

> Language and packages used for presentation slides:

- Python - Language/Platform
- Matplotlib - Enhanced graphing
- SciPy - Statistics, Regression
- Plotly - Enhanced graphing



## Development

Want to contribute? Great!

Pokemon project is open to contribute create your PR today! 
https://github.com/kuzhinjo/pokemon-project

## Source
Dataset: https://www.kaggle.com/datasets/rounakbanik/pokemon
Presentation: https://docs.google.com/presentation/d/1FgmIuxf7HZm4OATzsp8qCN_ysdtrYmqu8obk5Sn_ZGo/edit?usp=sharing
