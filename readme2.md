# 2024- Fall- DSA- 210 Project Personal Expense Analysis 
 
 Description 
 This depository contains the  law and data for my 2024 Fall Semester's DSA 210  design. The  end of this  design is to  dissect my  particular charges from October 1st to December 30th, identify patterns, and  estimate  sale actions to uncover correlations among parameters  similar as time,  quantum, and  sale  order. 
 
--- 
 
 Table of Contents 
 1.( provocation)(#motivation) 
 2.( Data Source)(#data- source) 
 3.( Data Preprocessing)(#data- preprocessing) 
 4.( Tools Used)(#tools- used) 
 5.( Analysis and Visualizations)(#analysis- and- visualizations) 
-( sale frequence Analysis)(#transaction-  frequence- analysis) 
-( Time- Grounded Patterns)(#time- grounded- patterns) 
-( Top expenditure orders)(#top-  expenditure-  orders) 
-( 3- Month Trend Analysis)(# 3- month- trend- analysis) 
-( Statistical Tests)(#statistical- tests) 
 6.( Findings)(#findings) 
 7.( Limitations)(#limitations) 
 8.( unborn Work)(#future- work) 
 
--- 
 
 provocation 
 The primary  thing of this  design is to more understand my spending habits by  assaying my bank account deals. This includes exploring 
 
- When deals  do most  constantly. 
- Which  orders dominate my spending. 
- How my charges change over time. 
- perceptivity that can help optimize my  fiscal habits. 
 
--- 
 
 Data Source 
- ** Dataset ** The dataset was exported from Akbank's mobile  operation in CSV format. 
- ** Data Masking ** particular information  similar as current balances and income deals were removed using the nobalance.py script to  insure  sequestration. 
 
 The  gutted dataset includes the following  crucial fields 
- ** DateTime ** Date and time of the  sale. 
- ** TransactionAmount ** The  quantum of the  sale. 
- ** Description ** The  sale  order or place. 
 
--- 
 
 Data Preprocessing 
 To prepare the dataset for analysis 
 1. Converted date and time strings to datetime objects for easier manipulation. 
 2. Parsed and formalized  sale  quantities, removingnon-numeric characters and formatting inconsistencies. 
 3. Dropped unused or  inapplicable columns( e.g., raw balance information). 
 4. uprooted  fresh features  similar as 
- Day of the week. 
- Hour of the day. 
-Yearly trends. 
 
--- 
 
 Tools Used 
 The  design relies on the following tools and libraries 
 
- ** Python ** Core programming language for data analysis. 
- ** Pandas ** For data cleaning, structuring, and manipulation. 
- ** NumPy ** For numerical operations and  computations. 
- ** Matplotlib & Seaborn ** For creating static visualizations. 
- ** Scipy ** For conducting statistical tests. 
- ** Jupyter Tablet ** For attestation and interactive  disquisition. 
 
--- 
 
 Analysis and Visualizations 
 
 sale frequence Analysis 
- ** Day of the Week ** A bar map visualizes the distribution of  sale counts across the days of the week. 
- ** Hourly exertion ** Another bar map illustrates the number of deals for each hour of the day. 
 
 Time- Grounded Patterns 
- ** Heatmap ** A heatmap shows the  crossroad of days of the week and hours of the day,  pressing peak  sale times. 
- ** KDE Plot ** A  viscosity plot visualizes  sale  quantities by the time of day, offering  perceptivity into high- value deals. 
 
 Top expenditure orders 
- ** Top Places ** A bar map highlights the top 10  sale  orders or  locales grounded on  frequence. 
 
 3- Month Trend Analysis 
- ** diurnal Counts ** A line map displays  sale counts over the last three months. 
- ** Retrogression Analysis ** A direct retrogression model evaluates whether  sale  frequence is trending up or down over this period. 
 
 Statistical Tests 
- ** T- Test ** A two- sample t- test compares  sale  quantities between morning( before 12 PM) and evening( after 12 PM) hours to determine if spending  geste 
             varies significantly by time. 
 
--- 
 
 Findings 
 1. ** sale Patterns ** 
- Deals peak during specific hours of the day and days of the week. 
-High-  frequence  exertion aligns with typical work or  rest hours. 
 
 2. ** Spending Habits ** 
-Certain  orders or  merchandisers dominate  sale counts. 
- No significant differences in  sale  quantities grounded on the time of day. 
 
 3. ** 3- Month Trends ** 
- sale  frequence shows a stable or slightly  adding  trend. 
 
--- 
 
 Limitations 
 Data Limitations 
- ** sequestration enterprises ** Some data fields were  barred to maintain  particular  sequestration. 
- ** Sample Size ** The dataset covers only a 3- month period, limiting the  compass for long- term trend analysis. 
 
 Methodological Limitations 
- ** Subjectivity in Categorization ** sale descriptions may not directly reflect spending  orders. 
- ** Lack of Contextual Data ** No information about  sale intent or external factors affecting spending. 
 
--- 
 
 unborn Work 
 1. ** Longitudinal Analysis ** Expand the dataset to cover a full time or multiple times to observe long- term trends. 
 2. ** Advanced ways ** Incorporate machine  literacy models to  prognosticate  unborn spending patterns or identify anomalies. 
 3. ** Interactive Visualizations ** make a web- grounded dashboard for dynamic  disquisition of the dataset. 
 4. ** Detailed Categorization ** apply NLP  ways to more classify  sale descriptions into meaningful  orders. 
 
--- 
 
 Depository Structure 
- ** analysis.py ** Main script for data cleaning, analysis, and visualization. 
- ** nobalance.py ** Script for masking sensitive data. 
- ** data_nobalance.csv ** Cleaned dataset used in the analysis. 
- ** Figure_X.png ** Visualizations generated by the analysis script. 
- ** README.md ** design attestation( this  train). 
 
--- 
 
 Script  prosecution and visualization  labors are included in this depository for reference. 
