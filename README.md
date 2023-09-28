# Data Wrangling: EdTech Product Survey



## A. Background
Conjoint analysis is a statistical method based on surveys that can be used in market research to determine customer’s values regarding the attributes representing a particular product or service. This project uses survey data about preferences for skill programs offered in Pacmann, one of the EdTech companies in Indonesia. Using this data, the product team wants to determine the priorities in developing the skill programs based on several attributes, such as the list of skills, the type of the programs, and the program price. Before the data can be used to do the analysis, the data needs to be prepared in the correct format.

**Note:** The data used in this project are in Indonesian



## B. Objectives
This project is built to implement data wrangling skills by using the Pandas Library in Python. The highlighted steps in this project are structuring and cleaning the data.



## C. Dataset
1. There are two raw datasets saved in the folder `data`:
   - `conjoint_survey_organic.xlsx`: data containing the survey result obtained organically by the team.
      <img src="https://github.com/novitaaryanti/edtech-product-survey-wrangling-project/assets/138101831/f1bd0355-90df-484c-b634-938fdb22dd44" width="700"/>
   - `conjoint_survey_ads.csv`: data containing the survey result obtained with the help of ads.
      <img src="https://github.com/novitaaryanti/edtech-product-survey-wrangling-project/assets/138101831/8e77c1c5-4334-4d4d-8089-a57b9e42a0ce" width="700"/>
2. Both raw datasets have the same format:
   - `Column 1`: timestamp
   - `Column 2`: survey taker's phone number
   - `Columns 3 - 12`: each column represents a choice-based question regarding the offered product. There are ten choice-based questions in total.
3. Each choice-based question provides three skills programs (product A, product B, product C) to be chosen by the survey taker. Thus, for each question, there are four options:
   - option `A` for product A
   - option `B` for product B
   - option `C` for product C
   - option `D` if the survey taker chooses neither of the provided products.

    | Question 	| Program A                                                                 	| Program B                                                                  	| Program C                                                                  	|
    |----------	|---------------------------------------------------------------------------	|----------------------------------------------------------------------------	|----------------------------------------------------------------------------	|
    | 1        	| - Create Analytics Dashboard<br>- Tutorial Based<br>- Rp 500.000,0        	| - Perform Customer Segmentation<br>- Mentoring Based<br>- Rp 350.000,0     	| - Design AB Test Experimentation<br>- Mentoring Based<br>- Rp 300.000,0    	|
    | 2        	| - Create Analytics Dashboard<br>- Tutorial Based<br>- Rp 500.000,0        	| - Design Data Pipeline<br>- Mentoring Based<br>- Rp 300.000,0              	| - Perform Credit Scoring Analytics<br>- Mentoring Based<br>- Rp 550.000,0  	|
    | 3        	| - Perform Customer Segmentation<br>- Mentoring Based<br>- Rp 350.000,0    	| - Perform Customer Segmentation<br>- Tutorial Based<br>- Rp 450.000,0      	| - Design Data Pipeline<br>- Mentoring Based<br>- Rp 250.000,0              	|
    | 4        	| - Design AB Test Experimentation<br>- Mentoring Based<br>- Rp 500.000,0   	| - Perform Price Optimization<br>- Tutorial Based<br>- Rp 350.000,0         	| - Perform Credit Scoring Analysis<br>- Mentoring Based<br>- Rp 350.000,0   	|
    | 5        	| - Design Data Pipeline <br>- Mentoring Based<br>- Rp 400.000,0            	| - Perform Customer Lifetime Analysis<br>- Tutorial Based<br>- Rp 300.000,0 	| - Design AB Test Experimentation<br>- Tutorial Based<br>- Rp 300.000,0     	|
    | 6        	| - Perform Churn Analytics<br>- Tutorial Based<br>- Rp 450.000,0           	| - Perform Customer Segmentation <br>- Mentoring Based<br>- Rp 300.000,0    	| - Create Machine Learning Model<br>- Mentoring Based<br>- Rp 300.000,0     	|
    | 7        	| - Perform Customer Lifetime Analysis<br>- Tutorial Based<br>- Rp500.000,0 	| - Design Data Pipeline<br>- Mentoring Based<br>- Rp 550.000,0              	| - Deploy Machine Learning Model<br>- Tutorial Based<br>- Rp 350.000,0      	|
    | 8        	| - Perform Credit Scoring Analytics<br>- Mentoring Based<br>- Rp 300.000,0 	| - Design Data Pipeline<br>- Mentoring Based<br>- Rp 550.000,0              	| - Create Machine Learning Model<br>- Tutorial Based<br>- Rp 550.000,0      	|
    | 9        	| - Create Analytics Dashboard<br>- Mentoring Based<br>- Rp 250.000,0       	| - Design AB Test Experimentation<br>- Tutorial Based<br>- Rp 550.000,0     	| - Perform Customer Lifetime Analysis<br>- Mentoring Base<br>- Rp 350.000,0 	|
    | 10       	| - Perform Credit Scoring Analytics<br>- Mentoring Based<br>- Rp 400.000,0 	| - Perform Churn Analytics<br>- Mentoring Based<br>- Rp 450.000,0           	| - Perform Churn Analytics<br>- Tutorial Based<br>- Rp 500.000,0            	|

   The survey taker can choose more than one product by selecting the option for products desired.
5. The data is considered invalid if the survey taker chooses option ‘D’ alongside another option for at least one question.



## D. Workflow
This program contains two modules, which are `main.py` and `data_wrangling.py`:
1. Module `main.py` includes `main()` as the entry point of the data wrangling program. This is where all the functions from `data_wrangling.py` will be called to obtain the expected data structure.
2. Module `data_wrangling.py` includes:
   - Dictionary `dict_program` contains all the details of available program options in each question.
   - Function `merge_data()` to merge all the available raw datasets in the folder `data`.
   - Function `remove_invalid_val()` to remove all invalid data from the DataFrame.
   - Function `get_program_details()` to get all the details about each program from the choice-based questions, which will be used while structuring the data in the expected structure.
   - Function `get_clean_data()` to get the expected structure of data, which is considered the clean data.
   - Function `output_clean_data()` to get the cleaned data as a new CSV file.

### 1. Merge all raw data into one dataset
Loop for all items in the  `data` folder, then combine all files that end with either `.xlsx` or `.csv` as a new DataFrame. This step is done by calling the function `merge_data()`. 
### 2. Remove irrelevant data
- The duplicate and missing data will be removed from the DataFrame by sequentially calling the built-in functions `drop_duplicates()` and `dropna()`.
- As the feature variable `Timestamp` data does not affect the analysis, the column `Timestamp` will be removed from the DataFrame by calling the built-in function `drop()`.
- Next, the invalid value in which the option ‘D’ is chosen alongside another option for at least one question will also be removed by calling the function `remove_invalid_val()`.
### 3. Get all the details of the program while structuring the data
- Structuring the data by calling the function `get_clean_data()`. The details include `user_phone`, `choice`, `skill`, `bentuk_program`, and `harga_program`. Each answered question by each survey taker will be divided into 3 rows, each for opinion about programs A, B, and C. 
- While structuring the data as a new DataFrame, the function `get_program_details()` will be called in order to obtain the program details from the dictionary `dict_program`.
### 4. Save the cleaned data as a new CSV file named `clean_data.csv`
The cleaned DataFrame will be saved in the workspace folder by calling the function `output_clean_data()`



## E. Result & Conclusions

![image](https://github.com/novitaaryanti/edtech-product-survey-wrangling-project/assets/138101831/7b2ab7f8-884d-4000-9172-66807edbf0a1)

From this program, the obtained cleaned data named `clean_data.csv` has several features:
- `user_phone` which contains the survey taker's phone number
- `choice` which represents the survey taker's choice regarding the program offered in each question (0 as 'No' and 1 as 'Yes')
- `skill` which contains the name of the skill program
- `bentuk_program` which contains the type of program (Mentoring Based / Tutorial Based)
- `harga_program` which contains the price of the program in Indonesian Rupiah (IDR)

Each row represents the opinion regarding the program including the type and the price. Thus, this data can now be used to do the analysis on which skill program should be prioritized to be developed.



## F. Future Work
This dataset can be used to do analysis or to be visualized using data visualization, such as Tableau.
