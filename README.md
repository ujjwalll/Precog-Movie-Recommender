# Precog Movies

Hi, I am Ujjwal Btech-CSE first year undergrad @ IIIT Delhi

It is a simple Web app I which you have to rate movies and you will be prediced different movies based on the movie that you rated at the web app.This project is deveoped for Precog @ IIIT Delhi for their membership program.

# How it works

HOME PAGE : 

It is the first page which you encounter when you open or intialises the app. It contains all the basic info about how app works and what are the things that are used etc.

REVIEW PAGE:

You are then redirected to the review page where you can see movie and you need to rate them so that smart ML algorithm which is running on the backend can understand your taste and recommend you the movies that suits your taste. If you don't know about the movie shown on the page, just refresh it it will show you a new movie every time.

FINAL PAGE:

This is the one of the page which shows you the movies that shows you, It will display 4 Details of the movie i.e. movie name, year of release, movie poster, genre.

# Technology Stack

1. Python is the core technology that supports the framework of this web app. This app uses FLASK framework, all the ML algorithm for recommendation by matrix factorization (ALS) is being implemented on the python itself.

2. Cascading style sheets (CSS) and java script is also used to create the Front end of the web app to make it a little bit stylish and good looking

3. SQLite3 is used as a database in the offline version of this app and at Heroku PostGreSql's are being used for the database purposes.

# How to install it on your PC's

Just Clone the repository on your system.

To make this application easy to use for all, I have done all the things in virtual environment, which I have also uploaded in the repository, To run this app follow the instructions below.

Open The Terminal

Go to the folder 

write following commands

1. source venv/bin/activate
2. cd src
3. cd app
4. python main.py

Here you go, the application is running on your terminal.
# Heroku App

Also deployed a heroku app for this application that you can find [here](https://precog-movies.herokuapp.com/)

# I love BROWNIES !!!!

I have also created a docker image of this project that you can find on my docker hub repository [here](https://cloud.docker.com/u/ujjwalll/repository/docker/ujjwalll/precog)

# DATABASE

The precribed limit was 200 movies in the task. But due to nature of being pushing the limits, I have choosen 10K movies dataset with 1 Lac rating.

# GRATITUDE

I thanks team Precog @ IIIT Delhi for giving me the opportunity to work on this wonderful project. 

# REFERENCES  

Matrix factorization and advanced analysis - Coursera - Univ. of Minnesota

Big data analytics - Recommender Systems - coursera - Yandex

Large-scale Parallel Collaborative Filtering for the Netflix Prize
-Yunhong Zhou, Dennis Wilkinson, Robert Schreiber and Rong Pan

W3school

Google

Stackoverflow

