# Data analysis on Crime Report
In the project, we are going to find the insights using python from the dataset which contains the information on the crimes reported in september 2022, West Yorkshire, UK.

## Dataset
Dataset has been taken from below URL:
https://data.police.uk/data/

## Setup
Software library used: Pandas

## General information on dataset
This dataset contain crimeid, location name, type of crime commited and the outcome type.

##some of the few important Insights from dataset:

1. "Voilence and Sexual harrasment" contributes to 41% and then "Public Order" which contribute 13% of of all the type of crime
![image](https://user-images.githubusercontent.com/68961996/210666641-6b028fad-157f-4b70-b099-e11b7cfeaa3f.png)

2. City which records highest number of crime in Leeds
 ![image](https://user-images.githubusercontent.com/68961996/210669320-8ae8d4cb-9fb3-4e4c-8db6-b11f6ab4c9c2.png)

3. Below bar graph shows crime type verses City and Leeds city records highest crime and "Voilence and sexual offence" crime type is highest
![image](https://user-images.githubusercontent.com/68961996/210667399-44cc8fd8-3e5a-49d8-b321-c609386ad944.png)

4.In the outcome recorded, the orange bar shows the outcome type before the end of sep and blue bar shows outcome type at the end of the month.
And it is seen that most of the records were files as "under investigation" and by the end of the month most of the record outcome type was "Unable to prosecute the suspect"
![image](https://user-images.githubusercontent.com/68961996/210668007-959a11a7-75b4-46d6-878f-5760da869ced.png)

5. Crime type verses Outcome type: Most of the crimes recorded comes under either "Unable tp prosecute the suspect" or "Investigation complete; no suspect identified" and almost all the cases for "Voilence and sexual offence" comes under these 2 type
![image](https://user-images.githubusercontent.com/68961996/210668734-e0ef3a91-0513-40a7-af47-7a807f67ebe2.png)

6. The last code as below, shows that all the "Under investigation" outcome before month end has no value/0/null in "Outcome type" and there are 12647 crimes with no outcome in the end of the month
data_U_I["Outcome type"].value_counts() 

                                     
