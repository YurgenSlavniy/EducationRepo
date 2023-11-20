# https://sql-academy.org

# INPUT:
Мы имеем базу данных с 4 мя таблицами. 

Trip
- id (INT) key to `Pass_in_trip:-trip`
- company (INT) key from `Company:-id`
- plane (VARCHAR) 
- town_from (VARCHAR)
- town_to (VARCHAR)
- time_out (DATETIME)
- time_in (DATETIME)

Company
- id (INT) key to `Trip:-company`
- name (VARCHAR)

Pass_in_trip
- id (INT)
- trip (INT) key from `Trip:-id`
- passenger (INT) key from `Passenger:-id`
- place (VARCHAR)

Passenger 
- id (INT) key to `Pass_in_trip:-passenger`
- name (VARCHAR)
*****************************************************
1) Print the names of all the people who are in the airline database
```
SELECT name FROM passenger;
```
2) Print the names of all airlines
```
SELECT name FROM company;
```
3) Print all trips made from Moscow
```
SELECT * FROM trip WHERE town_from = 'Moscow';
```
4) Print the names of people that end in "man"
```
SELECT name FROM passenger WHERE name LIKE '%man';
```
5) Print the number of trips completed on TU-134
```
SELECT COUNT(*) as count FROM trip WHERE plane = 'TU-134';
```
