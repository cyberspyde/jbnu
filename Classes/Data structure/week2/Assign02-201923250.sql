/*** Assignment #2 - SQLite ***/
/* Rename this file as Assign02-UniIDNum.sql when submitting
   example: Assign02-202012345.sql
   
   To check: read in this file inside sqlite by:
   c:\sqlite3 myDatabase
   sqlite> .read Assign02-202012345.sql
   
   
/* Open a terminal, type the following command where "myDatabase" is the database name you will use. WARNING: Sqlite will still run even if no database name is given but all your data will not be saved.

sqlite3 myDatabase

*/

/* always enable "headers" and Foreign Key constraint*/
.header ON
PRAGMA foreign_keys = ON;
.mode column

/* SQLite system commands (not SQL)
.help - lists other . commands
.headers on/off - show/hide column headers in query results
.mode - separate the columns in each tuple/row 
.show - see how we have set our parameters
.read 'fileSchema.sql' - execute SQL code in input file
.import 'fileData.txt' TableName - loads data in  input file to table TableName, make sure that separators are used correctly!
.exit - exit sqlite3
*/

/* SQL commands. They must end with a semi-colon ";" so SQLite will know it is end of the statement */

/* Drop Tables*/
DROP TABLE teachingLoad;
DROP TABLE subject;
DROP TABLE teacher;

/* Create tables */
CREATE TABLE subject(
       sDept VARCHAR(6),
       sCode INTEGER,
       sTitle VARCHAR(75),
       PRIMARY KEY (sDept, sCode)
);

CREATE TABLE teacher(
       tUname VARCHAR(8),
       tFname VARCHAR(50),
       tLname VARCHAR(50),
       tStartDate CHAR(10),
       PRIMARY KEY (tUname)
);

CREATE TABLE teachingLoad(
       lUname VARCHAR(8),
       lDept VARCHAR(6),
       lCode INTEGER,
       PRIMARY KEY (lUname, lDept, lCOde),
       FOREIGN KEY (lUname) REFERENCES teacher(tUname),
       FOREIGN KEY (lDept, lCode) REFERENCES subject(sDept, sCode)
);


/* Sample data */
INSERT INTO subject
       VALUES('COE', 111, 'Algebra');
INSERT INTO subject
       VALUES('COE', 114, 'Trigonometry');
INSERT INTO subject
       VALUES('COE', 214, 'Differential Calculus');
INSERT INTO subject
       VALUES('COE', 312, 'Differential Equations');

INSERT INTO teacher
       VALUES('jha', 'Janin', '', date('2018-11-01'));
INSERT INTO teacher
       VALUES('mikki', 'Mikki', '', '2016-09-01');
INSERT INTO teacher
       VALUES('sattav', 'Soheil','', '2015-07-01');
INSERT INTO teacher
       VALUES('bigboy', 'Khan', '',date('2012-02-01'));

INSERT INTO teachingLoad
       VALUES('jha', 'COE', 111);
INSERT INTO teachingLoad
       VALUES('mikki', 'COE', 214);
INSERT INTO teachingLoad
       VALUES('sattav', 'COE', 111);
INSERT INTO teachingLoad
       VALUES('sattav', 'COE', 114);
INSERT INTO teachingLoad
       VALUES('bigboy', 'COE', 111);
INSERT INTO teachingLoad
       VALUES('jha', 'COE', 312);
INSERT INTO teachingLoad
       VALUES('sattav', 'COE', 312);
INSERT INTO teachingLoad
       VALUES('bigboy', 'COE', 114);
INSERT INTO teachingLoad
       VALUES('mikki', 'COE', 114);



/* SAMPLE UPDATE */

-- 1) Add last name for all the teachers in table teacher
--    your answer must be different from all others in class
/* SQL Statement */
/** Use UPDATE **/
UPDATE teacher SET tLname = 'Qodirjon' where tUname = 'jha';
UPDATE teacher SET tLname = 'Adam' where tUname = 'mikki';
UPDATE teacher SET tLname = 'Abraham' where tUname = 'sattav';
UPDATE teacher SET tLname = 'McDonals' where tUname = 'bigboy';


/* Sample queries */

-- 2) What are all the subjects offered?
/* SQL statement */
SELECT *
FROM subject;
/* OUTPUT 
sTitle    
----------
Algebra   
Trigonomet
Analytic G
Differenti
*/ 

-- 3.a) First three subjects sorted by teacher name ascending
--    Hint: use LIMIT N
/* SQL statement */
SELECT lUname, lDept, lCode
FROM teachingLoad
ORDER BY lUname ASC 
LIMIT 3;
/* OUTPUT
lUname      lDept       number    
----------  ----------  ----------
bigboy      COE         111       
bigboy      COE         114       
jha         COE         111       
*/

-- 3.b) First four subjects sorted by teacher name in reverse order
/* SQL Statement */
SELECT * 
FROM teachingLoad
ORDER BY lUname DESC
LIMIT 4;
/* OUTPUT
lUname      lDept       number    
----------  ----------  ----------
sattav      CSE         312       
sattav      COE         114       
sattav      COE         111       
mikki       COE         214    
*/

-- 4) What's firstname & lastname of all teachers sorted by firstname?
-- Assign first name as 'First' and last name as 'Last'
/* SQL Statement */
SELECT tFname AS 'First', tLname AS 'Last' 
FROM teacher 
ORDER BY tFname ASC;
/* OUTPUT  
NOTE: Data for 'Last' will be different from given below
First       Last      
----------  ----------
Janin       Isle Girl 
Khan        Food God  
Mikki       Chillin   
Soheil      Bright One
*/

-- 5) What is the firstname of teacher with username of 'bigboy'?
--    Assign firstname as 'Name'
/* SQL Statement */
SELECT tFname AS 'Name'
FROM teacher
WHERE tUname = 'bigboy';
/* OUTPUT
Name      
----------
Khan    
*/

-- Using a string when number is expected,
--   SQLIte will try to convert it to equivalent number
-- Using a number when string is expected,
--   SQLIte will try to convert it to equivalent string
-- 6) What 'COE' subjects with level 100 are offered?
--     Try to treat field 'number' as both number & string
/* SQL Statement */
SELECT sDept, sCode, sTitle
FROM subject
WHERE sDept = 'COE' AND sCode > 99 AND sCode < '200';
/* OUTPUT
sDept       number      sTitle    
----------  ----------  ----------
COE         111         Algebra   
COE         114         Trigonomet
*/

-- 7) What subjects are taught by sattav and jha
/* SQL Statement */
SELECT *
FROM teachingLoad
WHERE lUname = 'jha' or lUname = 'sattav';
/* OUTPUT
lUname      lDept       number    
----------  ----------  ----------
jha         COE         111       
jha         COE         312       
sattav      COE         111       
sattav      COE         114       
sattav      CSE         312       
*/

-- 8) What subjects titles start with 'Differential'?
/* SQL Statement */
SELECT *
FROM subject
WHERE sTitle LIKE 'Differential%';
/* OUTPUT
sDept       number      sTitle               
----------  ----------  ---------------------
COE         214         Differential Calculus
COE         312         Differential Equation    
*/

-- 9) What if one of the subject titles starting 
--    with 'Differential' is mispelled as 'DifFerential?'
UPDATE subject
SET sTitle = 'DifFerential Eqns'
WHERE sTitle = 'Differential Equations';
/* SQL Statement */
SELECT *
FROM subject
WHERE sTitle LIKE 'Dif_erential%';
/* OUTPUT
sDept       number      sTitle               
----------  ----------  ---------------------
COE         214         Differential Calculus
COE         312         DifFerential Eqns    
*/

-- SQLite represent dates as strings in the format as yyyy-mm-dd
-- (http://www.sqlite.org/lang_datefunc.html).

-- 10) Which teachers started before 2016?
--    Hint: We can use "<,>,<=,>=,=" for date in string format
/* SQL Statement*/
SELECT * 
FROM teacher
WHERE tStartDate <= '2016-01-01';
/* OUTPUT
tUname      tFname      tLname      tStartDate
----------  ----------  ----------  ----------
sattav      Soheil      Bright One  2015-07-01
bigboy      Khan        Food God    2012-02-01
*/

