# acarsdeco2-parser
A set of scripts to parse acarsdeco2 output, save them to DB and provide simple web UI to view saved data.

## prerequisites
* acarsdeco2 - running with ```--net``` parameter
* MySQL 
* python

## installation
Create database on your MySQL server and create table using ```messages.sql``` script.
After that just run ```python acarsdeco2-parser``` and check the database for data.
