# Guide d'utilisation du code du Dashboard

Le fichier suivant a pour but d'expliquer comment le code a été créé afin qu'il soit plus facile à modifier à l'avenir :smile:




## Index :card_index_dividers:

- [Necessary libraries](#bibliothèques-nécessaires) :blue_book:
- [How to launch the Dashboard](#comment-lancer-ou-gérer-le-programme) :raised_eyebrow:
- [Goal of the project](#goal-of-the-project) :file_folder:
- [Notebooks overview](#notebooks-overview) :framed_picture:
- [Web Dashboard](#web-dashboard) :nerd_face:
- [Analysis-Interpretation](#analysis-interpretation) :globe_with_meridians:
- [Conclusion](#conclusion) :globe_with_meridians:
- [Future direction](#future-direction) :arrow_up_small:


## Necessary libraries :blue_book:

Afin de faire fonctionner le programme, la bibliothèque suivante doit être installée:
- dash_bootstrap_components


## How to launch the Dashboard :raised_eyebrow:

Pour pouvoir visualiser le dashboard, il est nécessaire de taper dans le terminal de l'ordinateur:

python3 index.py

ou on peut aussi taper
python index.py


## Goal of the Project

This project aims to analyze the potential impact of the COVID-19 pandemy on the economy. The analysis is conducted using a combination of data preprocessing, visualization techniques, clustering analysis, and the development of an interactive web-based dashboard using Dash.

The primary goal of this project is to gain insights into how economic factors and COVID-19 metrics intersect and influence each other within various regions.

For the above reasons, the project was divided into 3 parts: one part dedicated to the analysis of European countries, another part dedicated to the analysis of American countries, and another part dedicated to the analysis of African and Asian countries, which is why this document contains explanatory sections dedicated to each continent mentioned. 

The idea was to be able to analyze and draw **conclusions about the global situation** once we had representative and aggregated data for each continent studied.


## Notebooks Overview

The project includes Jupyter notebooks for data preprocessing, analysis, and clustering which are in the different branches, because in the main branch we only put the code related to the Dashboard. 

These notebooks contain Python code and markdown cells documenting the steps taken in the analysis process. Key tasks performed in the notebooks include:


### Preprocessing-Africa-Asia

• Overview:
This code encompasses various tasks including data processing, clustering analysis, and data integration. It operates on socio-economic indicators for African and Asian countries as well as COVID-19 data. The primary objectives are to identify clusters of countries based on socio-economic factors and integrate COVID-19 data for further analysis.

• Steps:
••Data Loading and Preprocessing:

CSV files containing socio-economic indicators for African and Asian countries are loaded using pandas.
Data is preprocessed to handle missing values, scale features, and ensure uniform formatting.

••Clustering Analysis:
K-means clustering is performed to identify clusters of countries based on socio-economic indicators.
Elbow method and silhouette score are utilized to determine the optimal number of clusters.

••Data Visualization:
Visualizations such as line plots and scatterplots are generated to visualize clustering results and socio-economic trends.

••Data Integration:
COVID-19 data is integrated into the analysis by combining it with the socio-economic dataset.
The integrated dataset is prepared for further analysis, ensuring consistency in date formats and column names.

••Output Generation:
Processed dataframes are saved as CSV files for future use and analysis with dash.


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

• Various plots are created to visualize COVID-19 data, economic indicators, and their correlations. COVID-related data is merged with economic indicators data to create scatter plots and heatmaps between those two types of variables.

• The notebook aims to search for visually appealing representations of the data for better understanding. 

• The notebook aims to decide on the type of figure and the part of the data that will be used on the Dashboard, ensuring that the visualizations are informative and align with the project's objectives.


### Cluster_europe

• This notebook performs clustering analysis on economic and COVID-19 data for European countries.

• It utilizes KMeans clustering to group countries based on similarities in economic indicators and COVID-19 metrics.

• The analysis involves feature scaling, determining the optimal number of clusters, and assigning cluster labels to countries.


### Analysis

• This notebook provides detailed data preprocessing and merging steps tailored for countries in the Americas region.

• The preprocessing involves concatenating and preparing various data tables related to COVID-19 metrics and economic indicators specific to American countries.

• Importing datasets encompassing COVID-19 statistics, economic indicators such as GDP, education, poverty, and trade data.

• Cleaning the COVID-19 data by handling missing values, selecting pertinent columns, and aggregating data by month and location.

• Standardizing and cleaning economic indicator data, including merging different tables and ensuring consistency across variables.

• Utilizing techniques like K-nearest neighbors (KNN) imputation for filling missing values in economic indicator datasets.

• Assigning a continent label (America) to the preprocessed data and preparing it for subsequent analysis and visualization.

• Combining the preprocessed data from both America and Euope to create a comprehensive dataset for dashboard visualization. 


• Defining a Dash layout with multiple pages. Each page focuses on different aspects of the data and visualization components include maps, line charts, scatter plots, and dropdown menus for interactivity.

• Defining Callbacks to update the displayed data based on user interactions, such as selecting a country or a variable.

• This notebook outputs two files specific to American and european countries:

df_concatenado.csv -> economic factors for America and Europe
df_covid_combined.csv -> covid factors for America and Europe

The preprocessing steps ensure that the data is structured and cleaned for further analysis and visualization on the dashboard, facilitating insights into the intersection of economic factors and the COVID-19 pandemic in the Americas region.


## Web Dashboard

The project includes the development of an interactive web-based dashboard using Dash, a Python framework for building analytical web applications. The dashboard provides users with the ability to visualize and explore the analyzed data in a user-friendly manner.


### Pages and Layouts

The web dashboard consists of multiple pages, each focusing on different aspects of the data analysis. The layout and contents of each page are designed to facilitate data exploration and interpretation.


• **Page 1:** 

◦ The first page called *Customizable graphic for each country* shows an overview of all the countries studied. On this page it is possible to visualize the evolution of mostly economic variables but also certain variables related to COVID-19 in order to be able to compare at the same time the effects of the pandemic on the economic sector of each country.


• **Page 2:**

◦ The second page called *Covid Factor* is a page dedicated to show the evolution of total cases and total deaths linked to COVID-19 for each country.


• **Page 3:** 

◦ The third page called Selected Countries is a page dedicated to displaying information on particular countries representative of certain regions. The latter were defined using Clustering techniques detailed in another section. 

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

We selected countries that represent the diversity of the different continents, taking into account how their economy originally is and how they were impacted by the pandemic. With the help of the Notebook visualisation-before-cleaning and with all the preprocess made on our data, we searched if certains group of countries stood out according to different economic and covid related criterias. From this and the clustering step (which usually confirmed our analysis), we could identify for each continent 3 or 4 groups of countries with similarities, and we decided to select only 1 from each group based on the amount of data available for the features we want to analyse.
We also volontarily put aside countries impacted by a war or with extreme political situations, as Venezuela, Ukraine and Mali for example. 

We decided to make the deep analysis on the countries: Chile, Canada, Mexico, Finland, France, Romania, Italy, Morocco, Equatorial Guinea, Comoros, South Africa, Jordan, China, Kuwait, United Arab Emirates.


- Feature selection

We selected features that show how the pandemic impacted the countries, and the economics situation of those countries.

For exemple we decided to keep features that give a value relatively to the population size and the orginal situation of the country (for the case of excess_mortality_cumulative_per_million, it looks similar to total_deaths look for most countries, and we have more data for total_deaths so we chose total_deaths for our analysis).

The final features selected are the following:

◦ Covid table:

total_deaths: Total deaths attributed to COVID-19. Counts can include probable deaths, where reported.

total_cases_per_million: Total confirmed cases of COVID-19 per 1,000,000 people. Counts can include probable cases, where reported.

new_cases_smoothed_per_million: New confirmed cases of COVID-19 (7-day smoothed) per 1,000,000 people. Counts can include probable cases, where reported. 

stringency_index: Government Response Stringency Index: composite measure based on 9 response indicators including school closures, workplace closures, and travel bans, rescaled to a value from 0 to 100 (100 = strictest response)

weekly_hosp_admissions_per_million: Number of COVID-19 patients newly admitted to hospitals in a given week (reporting date and the preceeding 6 days)

HICP (only for European and American countries): The Harmonized Consumer Price Index (HICP) provides a standardized measure of inflation across EU countries

◦ Economic table: 

trade: Sum of exports and imports of goods and services, divided by gross domestic product, expressed as a percentage. This isalso known as the "trade openness index".

poorest_decile_threshold: level of income or consumption per person per day below which 10% of the population falls. This data isadjusted for inflation and differences in the cost of living between countries.

Gini: The Gini coefficient measures inequality on a scale from 0 to 1. Higher values indicate higher inequality. Depending on thecountry and year, the data relates to income measured after taxes and benefits, or to consumption, per capita.

Education: Total general government expenditure on education (all levels of government and all levels of education), given as a shareof GDP.

median_income: This data is adjusted for inflation and for differences in the cost of living between countries.

GDP: This data is expressed in US dollars. It is adjusted for inflation but does not account for differences in the cost of livingbetween countries.

richest_decile_threshold: This is the level of income or consumption per person per day below which 90% of the population falls. This data isadjusted for inflation and differences in the cost of living between countries.

Inflation (only for Asian and African countries): Inflation measured by consumer price index (CPI) is defined as the change in the prices of a basket of goods and services that are typically purchased by specific groups of households.

unemployment_rate: This indicator is measured in numbers of unemployed people as a percentage of the labour force and it is seasonally adjusted

- Data cleaning

We cleaned the data depending on the feature, the period for which the data is missing and using common sense. For exemple we replaced NaN from stringency_index by 0 as those values are missing because there were no measures taken anymore at the end of the pandemy for all the countries.
We used KNN imputers for variables where the data missing was randomly distributed over our features.


## Conclusion 

The project aims to provide valuable insights into the complex interactions between economic factors and the COVID-19 pandemic. Through comprehensive data analysis, visualization, and the development of an interactive dashboard, we strive to empower stakeholders with actionable information for decision-making and policy planning.

By leveraging advanced data analysis techniques and visualization tools, this project offers a deeper understanding of the economic impacts of the COVID-19 pandemic across different regions. The interactive web dashboard serves as a valuable resource for policymakers, researchers, and other stakeholders to explore trends, identify patterns, and make informed decisions.
