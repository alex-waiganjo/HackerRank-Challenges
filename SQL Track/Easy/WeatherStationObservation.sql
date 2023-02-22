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
TASK 1
Query a list of CITY and STATE from the STATION table.'

'SOLUTION '
SELECT CITY,STATE FROM STATION;


'
TASK 2
Query a list of CITY names from STATION for cities that have an even ID number.
Print the results in any order, but exclude duplicates from the answer.'

'SOLUTION'
SELECT  DISTINCT CITY FROM STATION WHERE MOD(ID,2)=0;