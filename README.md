
# Guide d'utilisation du code du Dashboard

Le fichier suivant a pour but d'expliquer comment le code a été créé afin qu'il soit plus facile à modifier à l'avenir :smile:





## Index :card_index_dividers:

- [Bibliothèques nécessaires](#bibliothèques-nécessaires) :blue_book:
- [Comment lancer le Dashboard](#comment-lancer-ou-gérer-le-programme) :raised_eyebrow:
- [Goal of the project](#goal-of-the-project) :file_folder:
- [Notebooks overview](#notebooks-overview) :framed_picture:
- [Web Dashboard](#web-dashboard) :nerd_face:
- [Analysis-Interpretation](#analysis-interpretation) :globe_with_meridians:
- [Conclusion](#conclusion) :globe_with_meridians:
- [Future direction](#future-direction)   :arrow_up_small:


## Bibliothèques nécessaires :blue_book:

Afin de faire fonctionner le programme, 3 bibliothèques ont été installées:
- dash
- dash_bootstrap_components


## Comment lancer le Dashboard:raised_eyebrow:

Pour pouvoir visualiser le dashboard, il est nécessaire de taper dans le terminal de l'ordinateur

    python3 index.py

## Goal of the Project

This project aims to analyze the potential impact of the COVID-19 pandemy on the economy. The analysis is conducted using a combination of data preprocessing, visualization techniques, clustering analysis, and the development of an interactive web-based dashboard using Dash.

The primary goal of this project is to gain insights into how economic factors and COVID-19 metrics intersect and influence each other within various regions.

For the above reasons, the project was divided into 3 parts: one part dedicated to the analysis of European countries, another part dedicated to the analysis of American countries, and another part dedicated to the analysis of African and Asian countries, which is why this document contains explanatory sections dedicated to each continent mentioned. 

The idea was to be able to analyze and draw **conclusions about the global situation** once we had representative and aggregated data for each continent studied.

## Notebooks Overview

The project includes Jupyter notebooks for data preprocessing, analysis, and clustering. These notebooks contain Python code and markdown cells documenting the steps taken in the analysis process. Key tasks performed in the notebooks include:

### Preprocessing-Africa-Asia

• blabla???

### Preprocessing-europe

• This notebook provides an extensive data preprocessing and merging to prepare our European data for analysis.

• Importing various data tables related to COVID-19, economic indicators, and inflation.

• Preprocessing of the COVID-19 data by cleaning missing values, selecting relevant columns, and aggregating the data by month and location.

• Cleaning and standardizing the inflation data, including merging different tables and standardizing the 'HICP' column.

• Merging the COVID-19 data with the standardized inflation data based on location and date.

• Preprocessing other economic indicator data tables, including education, GDP, Gini index, poverty, and trade data.

• Imputing missing values in the merged economic indicator data using the K-nearest neighbors (KNN) imputation method.

• Assigning a continent label to the data (Europe in this case) and prepared it for further analysis.

• This notebook results in the creation of 2 files concerning the countries France, Belgium, Finland, Poland, Romania, Hungary, Germany and Italy, :
- df_covid_HICP_europe.csv with the features: date,HICP,location,total_deaths,stringency_index,total_cases_per_million,new_cases_smoothed_per_million,weekly_hosp_admissions_per_million,continent,Year,Month.
- df_economics_europe.csv with the features: location,education,GDP,gini,median_income,poorest_decile_threshold,richest_decile_threshold,trade,continent,Year

### Visualisation-before-cleaning

• This notebook focuses on in-depth data analysis and visualization.

• It explores various datasets related to COVID-19 and economics.

• Visualizations include line plots, scatter plots, and correlation matrices, aiming to uncover relationships between different variables (such as GDP, education, Gini index, total deaths, stringency index, etc., over time or across different countries).

• This notebook was used to get a first idea of the quality of the data we gathered and to select only the relevent features and countries.


### Visualisation-after-cleaning

• This notebook experiments with different types of visualizations for our cleaned and preprossed tables, using libraries such as Matplotlib, Seaborn, Plotly, and Dash.

• Various plots are created to visualize COVID-19 data, economic indicators, and their correlations COVID-related data is merged with economic indicators data.

• The notebook aims to search for visually appealing representations of the data for better understanding. 

• The notebook aims to decide on the type of figure and the part of the data that will be used on the Dashboard, ensuring that the visualizations are informative and align with the project's objectives.


### Cluster_europe

• This notebook performs clustering analysis on economic and COVID-19 data for European countries.

• It utilizes KMeans clustering to group countries based on similarities in economic indicators and COVID-19 metrics.

• The analysis involves feature scaling, determining the optimal number of clusters, and assigning cluster labels to countries.

### Analysis

??? Where we make the analysis for america, concatenate and make the tables ready for the dash and do the clusters
• This notebook provides detailed data preprocessing and merging steps tailored for countries in the Americas region.

• The preprocessing involves concatenating and preparing various data tables related to COVID-19 metrics and economic indicators specific to American countries.

• Importing datasets encompassing COVID-19 statistics, economic indicators such as GDP, education, poverty, and trade data.

• Cleaning the COVID-19 data by handling missing values, selecting pertinent columns, and aggregating data by month and location.

• Standardizing and cleaning economic indicator data, including merging different tables and ensuring consistency across variables.

• Merging the cleaned COVID-19 data with standardized economic indicators based on location and date.

• Utilizing techniques like K-nearest neighbors (KNN) imputation for filling missing values in economic indicator datasets.

• Assigning a continent label (America) to the preprocessed data and preparing it for subsequent analysis and visualization.

• This notebook outputs two files specific to American countries:

    df_covid_economics_america.csv containing features like date, location, total_deaths, GDP, education, poverty, continent, Year, and Month.
    df_clusters_america.csv containing the clustered groups of American countries based on economic and COVID-19 metrics.

The preprocessing steps ensure that the data is structured and cleaned for further analysis and visualization on the dashboard, facilitating insights into the intersection of economic factors and the COVID-19 pandemic in the Americas region.

## Web Dashboard

The project includes the development of an interactive web-based dashboard using Dash, a Python framework for building analytical web applications. The dashboard provides users with the ability to visualize and explore the analyzed data in a user-friendly manner.

### Pages and Layouts

The web dashboard consists of multiple pages, each focusing on different aspects of the data analysis. The layout and contents of each page are designed to facilitate data exploration and interpretation.

• **Page 1:** 


        
◦ The first page called *Economic Factor* shows an overview of all the countries studied. On this page it is possible to visualize the evolution of mostly economic variables but also certain variables related to COVID-19 in order to be able to compare at the same time the effects of the pandemic on the economic sector of each country.

• **Page 2:**


◦ The second page called *Covid Factor* is a page dedicated to show the evolution of total cases and total deaths linked to COVID-19 for each country.

• **Page 3:** 

◦ The third page called Selected Countries is a page dedicated to displaying information on     particular countries representative of certain regions. The latter were defined using Clustering techniques detailed in another section. 

At the beginning, it is possible to select one of the countries to visualize certain variables specific to each country, for example the evolution of GDP, the evolution of the country's inequality, certain evolution of variables linked to COVID-19 and it is even possible to visualize the correlation between different variables through a 3D graph.


This section is immediately followed by generalized graphs showing the evolution of variables of all the selected countries as a whole, such as inflation, hospitalization rate, GDP, number of cases, etc.

### Dash Components and Callbacks

At the code level, it is structured in different folders, thus separating the codes in charge of creating the visualizations and managing the functions that allow the creation of the graphics. Both codes are located in folders called *layouts* and *callbacks* respectively. 


There are also the files *index.py*, *app.py*, *load_data.py* and *graph_description.json* that contain basic information to run the application. The JSON file contains the explanatory texts for each graph.


### Running the Dashboard

To run the web dashboard locally, follow these steps:

1. Ensure that all required Python libraries and dependencies are installed.

2. Run the index.py file, which serves as the entry point for the Dash application.

3. Open a web browser and navigate to the provided address to access the dashboard.


## Analysis/interpretation 

- Country selection

We selected countries that represent the diversity of the different continents, taking into account how their economy originally is and how they were impacted by the pandemic. We had for each continent 3 or 4 groups of countries with similarities, and we decided to select only 1 from each group base on the amount of data available for the features we want to analyse.

According to the amount of missing values of the total_cases_per_million feature, which is the one that varies a bit depending on the countries, we should remove the countries Bulgaria, Greece and Norway (which is ok because the ones left still represent well the diversity in Europe). 

- Feature selection

We selected features that show how the pandemic impacted the countries, and the economics situation of those countries.

For exemple we decided to keep features that give a value relatively to the population size and the orginal situation of the country (for the case of excess_mortality_cumulative_per_million, it looks similar to total_deaths look for most countries, and we have more data for total_deaths so we chose total_deaths for our analysis).

- Data cleaning

We cleaned the data depending on the feature, the period for which the data is missing and using common sense. For exemple we replaced NaN from stringency_index by 0 as those values are missing because there were no measures taken anymore at the end of the pandemy for all the countries.

We used KNN imputers for variables where the data missing was randomly distributed over our features...



-  Graph analysis

For France or Brazil we can see..

The inflation and total_death seem to be correlated but it is probably due to the fact that total death is cumulative and inflation grows with time, so both are evoluting the same way. But It is more interesting to look at non cumulative variables as they reflect the situation at a certain point, as the inflation rate does. 

From our analysis we found that there is no obvious correlation between the COVID-19 pandemics and the global economy. 


- Interpretation

Data not sufficient to analyze the impact of the pandemic on the global economy. First we had to select only a few countries...

Selected features try to capture adequately the economic aspects impacted by the pandemic but economy is linked to many other factors.. (geopolitical aspects to consider too-...)

To mitigate the gaps and limitation we have we could…


## Conclusion 

The project aims to provide valuable insights into the complex interactions between economic factors and the COVID-19 pandemic. Through comprehensive data analysis, visualization, and the development of an interactive dashboard, we strive to empower stakeholders with actionable information for decision-making and policy planning.

By leveraging advanced data analysis techniques and visualization tools, this project offers a deeper understanding of the economic impacts of the COVID-19 pandemic across different regions. The interactive web dashboard serves as a valuable resource for policymakers, researchers, and other stakeholders to explore trends, identify patterns, and make informed decisions.

## Future Directions

While the current version of the project offers valuable insights into the economic impacts of COVID-19, there are several avenues for future development and improvement:

• Enhanced data visualization: Implement more interactive and visually appealing charts and graphs to facilitate data exploration.

• Incorporation of additional data sources: Integrate data from other relevant sources to provide a more comprehensive understanding of the economic landscape.

• Machine learning models: Explore the use of advanced machine learning algorithms to predict future economic trends and pandemic impacts.

• User feedback and iteration: Gather feedback from users to identify areas for improvement and iterate on the dashboard design and functionality.

Continued development and refinement of the project will enable us to provide even greater value to stakeholders and contribute to a deeper understanding of the complex interactions between economics and public health crises like COVID-19.
