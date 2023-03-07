' The STATION table is described as follows:
  
                      TABLE  :   CITY        
                    FIELD               TYPE  
                =============== | =============
                ID              |       NUMBER
                CITY            |       VARCHAR(21)
                STATE           |       VARCHAR(2)   
                LAT_N           |       NUMBER    
                LONG_W          |       NUMBER 

Where LAT_N is the northern latitude and LONG_W is the western longitude.
' 



'
    Weather Observation  Station 1

Query a list of CITY and STATE from the STATION table.'

'SOLUTION '
SELECT CITY,STATE FROM STATION;



'
     Weather Observation  Station 2

Query the following two values from the STATION table:
1. The sum of all values in LAT_N rounded to a scale of 2 Decimal Places
2. The sum of all values in LONG_W rounded to a scale of 2 Decimal Places'
'The Output must be in the form lat ,lon'

'SOLUTION'
SELECT  ROUND(SUM(LAT_N),2) AS lat  ,  ROUND(SUM(LONG_W),2) AS lon FROM STATION;



'
     Weather Observation  Station 3

Query a list of CITY names from STATION for cities that have an even ID number.
Print the results in any order, but exclude duplicates from the answer.'

'SOLUTION'
SELECT  DISTINCT CITY FROM STATION WHERE MOD(ID,2)=0;




'
     Weather Observation  Station 4


Find the difference between the total number of CITY entries in 
the table and 
the number of distinct CITY entries in the table.
'

'SOLUTION'
SELECT  COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;