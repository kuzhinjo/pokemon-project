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
1.) Height/Weight

2.) Type

3.) Happiness

4.) Legendary pokemon

5.) Weight

In this analysis, we explore the relationship between weight and other base stats of Pokémon in our dataset. Specifically, we focus on the correlation between weight and attack, defense, and hit points (HP). Understanding these stats is crucial for assessing a Pokémon’s abilities and potential success in battles.

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
Aditya - size/power scatter/bar graphs
Marshall - Happiness scatter/bar graphs
Trey - Types scatter/bar graphs
Matthew - is_legendary scattter/bar graphs
Rajeev - height/weight correlated to base stats
Eric - Narrative of case study

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
