
# Guide d'utilisation du code du Dashboard

Le fichier suivant a pour but d'expliquer comment le code a été créé afin qu'il soit plus facile à modifier à l'avenir :smile:





## Index :card_index_dividers:
---

- [Bibliothèques nécessaires](#bibliothèques-nécessaires) :blue_book:
- [Comment lancer ou gérer le programme](#comment-lancer-ou-gérer-le-programme) :raised_eyebrow:
- [Goal of the project](#goal-of-the-project) :file_folder:
- [Notebooks overview](#notebooks-overview) :framed_picture:
- [Web Dashboard](#web-dashboard) :nerd_face:
- [Analysis-Interpretation](#analysis-interpretation) :globe_with_meridians:
- [Conclusion](#conclusion) :globe_with_meridians:
- [Formats de téléchargement de fichiers](#formats-de-téléchargement-de-fichiers)   :arrow_up_small:


## Bibliothèques nécessaires :blue_book:
---
Afin de faire fonctionner le programme, 3 bibliothèques ont été installées:
- dash_bootstrap_components


## Comment lancer ou gérer le programme :raised_eyebrow:
Pour pouvoir exécuter le programme, il est nécessaire de taper dans le terminal de l'ordinateur

    python3 manage.py runserver

Dans mon cas, j'utilise python 3 et je dois donc taper *python 3*.

Par ailleurs, si vous souhaitez modifier un modèle, c'est-à-dire un tableau de la base de données, vous devez écrire les modifications puis écrire

    python3 manage.py makemigrations

Et ensuite

    python3 manage.py migrate

De plus, le programme comporte une logique de *login* et *logout* ainsi que l'enregistrement d'utilisateurs normaux et d'un *superuser*. Ce dernier est celui qui a le pouvoir de modifier l'ensemble du site web à partir de l'onglet d'admin, qui est un onglet créé par défaut par Django. 

Pour créer un nouveau *superuser*, il suffit d'exécuter la ligne de code suivante et de suivre les instructions dans le terminal:

    python3 manage.py createsuperuser

Actuellement, les superutilisateurs créés avec leurs mots de passe respectifs sont:

    superuser1: fernandolalannev
    mot de passe: 123123

    superuser2: cdabancourt
    mot de passe: 123123

Ces données peuvent être modifiées à tout moment à partir de l'onglet "admin", accessible via le bouton de l'onglet accueil ou via l'URL suivante:

    http://127.0.0.1:8000/admin/


Pour comprendre le déroulement du programme, il est nécessaire de suivre le chemin suivant (dans le dossier CRUD) : *fichier html -> urls.py -> views.py -> fichiers html*

L'emplacement et la fonction des fichiers sont détaillés ci-dessous.


## Goal of the Project
This project aims to analyze the potential impact of the COVID-19 pandemy on the economy. The analysis is conducted using a combination of data preprocessing, visualization techniques, clustering analysis, and the development of an interactive web-based dashboard using Dash.
The primary goal of this project is to gain insights into how economic factors and COVID-19 metrics intersect and influence each other within various regions.
Notebooks Overview
The project includes Jupyter notebooks for data preprocessing, analysis, and clustering. These notebooks contain Python code and markdown cells documenting the steps taken in the analysis process. Key tasks performed in the notebooks include:
preprocessing-Africa-Asia
    • 
preprocessing-America
    • 
    • 
preprocessing-europe
    • This notebook provides an extensive data preprocessing and merging to prepare our data for analysis.
    • Importing various data tables related to COVID-19, economic indicators, and inflation.
    • Preprocessing of the COVID-19 data by cleaning missing values, selecting relevant columns, and aggregating the data by month and location.
    • Cleaning and standardizing the inflation data, including merging different tables and standardizing the 'HICP' column.
    • Merging the COVID-19 data with the standardized inflation data based on location and date.
    • Preprocessing other economic indicator data tables, including education, GDP, Gini index, poverty, and trade data.
    • Imputing missing values in the merged economic indicator data using the K-nearest neighbors (KNN) imputation method.
    • Assigning a continent label to the data (Europe in this case) and prepared it for further analysis
    • This notebook results in the creation of 2 files concerning the countries France, Belgium, Finland, Poland, Romania, Hungary, Germany and Italy, :
- df_covid_HICP_europe.csv with the features: date,HICP,location,total_deaths,stringency_index,total_cases_per_million,new_cases_smoothed_per_million,weekly_hosp_admissions_per_million,continent,Year,Month.
- df_economics_europe.csv with the features: location,education,GDP,gini,median_income,poorest_decile_threshold,richest_decile_threshold,trade,continent,Year

visualisation-before-cleaning
    • This notebook focuses on in-depth data analysis and visualization.
    • It explores various datasets related to COVID-19 and economics.
    • Visualizations include line plots, scatter plots, and correlation matrices, aiming to uncover relationships between different variables (such as GDP, education, Gini index, total deaths, stringency index, etc., over time or across different countries).
    • This notebook was used to get a first idea of the quality of the data we gathered and to select only the relevent features and countries.
    •  merge COVID-related data with economic indicators data and interpolate economic indicators to monthly frequency.
visualisation-after-cleaning
    • This notebook experiments with different types of visualizations for our cleaned and preprossed tables, using libraries such as Matplotlib, Seaborn, Plotly, and Dash.
    • Various plots are created to visualize COVID-19 data, economic indicators, and their correlations.
    • The notebook aims to provide visually appealing representations of the data for better understanding.
    • The notebook aims to decide on the type of figure and the part of the data that will be used on the Dashboard, ensuring that the visualizations are informative and align with the project's objectives.
cluster_europe
    • This notebook performs clustering analysis on economic and COVID-19 data for European countries.
    • It utilizes KMeans clustering to group countries based on similarities in economic indicators and COVID-19 metrics.
    • The analysis involves feature scaling, determining the optimal number of clusters, and assigning cluster labels to countries.
??
    • Where we concatenate and make the tables ready for the dash

Web Dashboard
The project includes the development of an interactive web-based dashboard using Dash, a Python framework for building analytical web applications. The dashboard provides users with the ability to visualize and explore the analyzed data in a user-friendly manner.
Pages and Layouts
The web dashboard consists of multiple pages, each focusing on different aspects of the data analysis. The layout and contents of each page are designed to facilitate data exploration and interpretation.
    • Page 1: 
        ◦ 
    • Page 2:
        ◦ 
    • Page 3: 
        ◦ 
Dash Components and Callbacks
The dashboard incorporates various Dash components and callback functions to create an interactive user experience.
    • Dash Components:
        ◦ HTML elements for structuring the layout, such as headers, paragraphs, and divs.
        ◦ Dash Core Components for interactive elements like dropdowns, sliders, and graphs.
        ◦ Dash Bootstrap Components for responsive design and styling.
    • Callbacks:
        ◦ Callback functions enable interactivity by updating the dashboard content in response to user inputs.
        ◦ Callbacks are used to update plot data, filter data based on user selections, and provide real-time feedback.
Running the Dashboard
To run the web dashboard locally, follow these steps:
    1. Ensure that all required Python libraries and dependencies are installed. You can use the requirements.txt file to install dependencies using pip install -r requirements.txt.
    2. Run the index.py file, which serves as the entry point for the Dash application.
    3. Open a web browser and navigate to the provided address to access the dashboard.
Analysis/interpretation 
- From our analysis we found that there is no obvious correlation between the COVID-19 pandemics and the global economy.

- We selected countries that represent the diversity of the different continents, taking into account how their economy originally is and how they were impacted by the pandemic.
Having only one value per country, we can still identify groups of countries which are often close to each other according to those criterias:
norway belgium/finland greece/italy bulgaria france/germany
Those countries represent well the diversity of the europe continent, also according to covid related graphs.
We should choose the ones which have the most data for the features we want to analyse.

Cannot show the relation between covid and economy according to this table only because only one value per country for the economy criterias ?


- We selected features that show how the pandemic impacted the countries, and the economics situation of those countries.
  excess_mortality_cumulative_per_million could be more interesting than total_deaths because it takes into consideration the 'usual' death ratio of the country as well as its population size. We can see with the graphs that the countries with the highest values are not the same depending on if the criteria "per million" was taken or not. 
excess_mortality_cumulative_per_million and total_deaths look quite similar for most countries, and we have more data for total_deaths so we could choose total_deaths for our analysis.
Let's select "total_deaths", "excess_mortality_cumulative_per_million", "stringency_index", "total_cases_per_million" for now.
Drop excess mortality column as it has too many missing values 

- We cleaned the data depending on the feature, the period for which the data is missing and using common sense. For exemple we replaced NaN from stringency_index by 0 as those values are missing because there were no measures taken anymore at the end of the pandemy for all the countries.
According to the amount of missing values of the total_cases_per_million feature, which is the one that varies a bit depending on the countries, we should remove the countries Bulgaria, Greece and Norway (which is ok because the ones left still represent well the diversity in Europe). 


-  For France or Brazil we can see..
Data not sufficient to analyze the impact of the pandemic on the global economy. First we had to select only a few countries...
Selected features try to capture adequately the economic aspects impacted by the pandemic but economy is linked to many other factors..
To mitigate the gaps and limitation we have we could…

Conclusion 
The project aims to provide valuable insights into the complex interactions between economic factors and the COVID-19 pandemic. Through comprehensive data analysis, visualization, and the development of an interactive dashboard, we strive to empower stakeholders with actionable information for decision-making and policy planning.
By leveraging advanced data analysis techniques and visualization tools, this project offers a deeper understanding of the economic impacts of the COVID-19 pandemic across different regions. The interactive web dashboard serves as a valuable resource for policymakers, researchers, and other stakeholders to explore trends, identify patterns, and make informed decisions.
Future Directions
While the current version of the project offers valuable insights into the economic impacts of COVID-19, there are several avenues for future development and improvement:
    • Enhanced data visualization: Implement more interactive and visually appealing charts and graphs to facilitate data exploration.
    • Incorporation of additional data sources: Integrate data from other relevant sources to provide a more comprehensive understanding of the economic landscape.
    • Machine learning models: Explore the use of advanced machine learning algorithms to predict future economic trends and pandemic impacts.
    • User feedback and iteration: Gather feedback from users to identify areas for improvement and iterate on the dashboard design and functionality.
Continued development and refinement of the project will enable us to provide even greater value to stakeholders and contribute to a deeper understanding of the complex interactions between economics and public health crises like COVID-19.
