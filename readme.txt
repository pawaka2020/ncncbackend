To install PostgreSQL, type 'pip install psycopg2-binary'
pip install Flask Flask-SQLAlchemy psycopg2-binary
====

install postgreql from internet
then run sql shell


----
Server [localhost]: (press enter)
Database [postgres]: (press enter)
Port [5432]: (press enter)
Username [postgres]: (press enter)
Password for user postgres:(enter actual password you set when installing postgresql)

WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=#

===
at postgres=#, type 'CREATE DATABASE mydatabase;'
then connect to 'mydatabase' with '\c mydatabase'
check which database is connected with 'SELECT current_database();'
the header of the terminal should show the name of the database it's connected to ie 'mydatabase=#'
===

For the rest, just use ChatGPT
