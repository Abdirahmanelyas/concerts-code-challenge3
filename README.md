Concerts Management System
This Python project allows users to manage concerts by adding bands, venues, and concert details using SQLite. The program interacts with an SQLite database (concerts.db) to store and manage the data using a class-based structure.

Features
Add a new band to the database using the Band class.
Add a new venue to the database using the Venue class.
Add a new concert by linking bands and venues using the Concert class.
Requirements
Python 3.x
SQLite3 (comes pre-installed with Python)
Project Structure
concerts.db: SQLite database file where band, venue, and concert information is stored.
main.py: The main Python script containing class-based methods to add bands, venues, and concerts.
Classes Overview:
Band:
Contains the method add_new_band() that allows adding a new band with details like name and hometown.
Venue:
Contains the method add_new_venue() that allows adding a new venue with details like title and city.
Concert:
Contains the method add_new_concert() that allows adding a concert by specifying band ID, venue ID, and the concert date.
Installation
Clone this repository or download the project files.

bash
Copy code
git clone https://github.com/Abdirahmanelyas/concerts-code-challenge3
cd concerts-management-system
Ensure Python 3.x is installed. You can check by running:

bash
Copy code
python --version
Set up the SQLite database:

The concerts.db file is created when you first run the script.
Usage
To add a new band, venue, and concert, run the main.py script:

bash
Copy code
python main.py
The script will prompt you to input:

Band details: Name and hometown of the band.
Venue details: Title and city of the venue.
Concert details: Band ID, Venue ID, and concert date.
Each entry will be stored in the concerts.db SQLite database.

Example Interaction:
bash
Copy code
Enter band name: Coldplay
Enter band hometown: London
Successfully added band: Coldplay from London

Enter venue title: Madison Square Garden
Enter venue city: New York
Successfully added venue: Madison Square Garden in New York

Enter band ID: 1
Enter venue ID: 1
Enter concert date (YYYY-MM-DD): 2024-10-05
Successfully added concert for Band ID 1 at Venue ID 1 on 2024-10-05
Database Schema
The database consists of three tables:

bands:

id (INTEGER PRIMARY KEY)
name (TEXT)
hometown (TEXT)
venues:

id (INTEGER PRIMARY KEY)
title (TEXT)
city (TEXT)
concerts:

id (INTEGER PRIMARY KEY)
band_id (INTEGER, foreign key to bands)
venue_id (INTEGER, foreign key to venues)
date (TEXT)
Contributing
Feel free to submit issues or pull requests if you'd like to contribute!

License
This project is licensed under the MIT License.

This README.md provides an overview of the system's functionality and instructions on how to use the script while reflecting the class-based structure of your Python project.








