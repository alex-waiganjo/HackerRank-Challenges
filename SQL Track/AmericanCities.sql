'Task 1
Query all columns for all American cities in the CITY table with populations
larger than 100000. The CountryCode for America is USA.
'


'Task 2
Query the NAME field for all American cities in the CITY table with populations
larger than 120000. The CountryCode for America is USA.
'


'TASK 3
Query all columns (attributes) for every row in the CITY table.
'

'TASK 4
Query all columns for a city in CITY with the ID 1661.
'

' TASK 5
Query all attributes of every Japanese city in the CITY table.
The COUNTRYCODE for Japan is JPN.
'


' TASK 6
Query the names of all the Japanese cities in the CITY table.
 The COUNTRYCODE for Japan is JPN.
'


' The CITY table is described as follows:
  
                      TABLE  :   CITY        
                    FIELD               TYPE  
                =============== | =============
                ID              |       NUMBER
                NAME            |       VARCHAR(17)
                COUNTRYCODE     |       VARCHAR(20)   
                DISTRICT        |       VARCHAR(20)     
                POPULATION      |       NUMBER 
' 

 'SOLUTION 1'  
 SELECT * from CITY WHERE  COUNTRYCODE='USA' AND POPULATION>100000; 


 'SOLUTION 2'
 SELECT NAME from CITY WHERE  COUNTRYCODE='USA' AND POPULATION>120000;          


 'SOLUTION 3'
 SELECT * from CITY; 


 'SOLUTION 4'
SELECT * FROM CITY WHERE ID=1661;


 'SOLUTION 5'
SELECT * FROM CITY WHERE COUNTRYCODE='JPN';


 'SOLUTION 6'
SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';