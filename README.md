# SQLite-Roster-Database-Project
This project demonstrates how to use Python, SQLite3, and JSON to manage and query a relational database of users, courses, and membership roles.  The program reads data from a JSON file, inserts it into a database (roster.sqlite), and performs queries to retrieve and display information.

Features
1. Creates three tables:
   User: Stores unique users.
   Course: Stores unique course titles.
   Member: Links users and courses with their role.
2. Reads JSON data (roster_data.json) and populates the database.
3. Prevents duplicates using INSERT OR IGNORE.
4. Updates existing membership records using INSERT OR REPLACE.

Runs sample SQL queries:
1. List of users, courses, and roles (with sorting).
2. Concatenated User.name + Course.title + role converted to hex.

Requirements
1. Python 3.x
2. SQLite3 (built-in with Python)

JSON file (roster_data.json) with data in the format:

[
  ["User Name", "Course Title", 1],
  ["Another User", "Another Course", 0]
]

Usage
1. Clone this repository:

git clone https://github.com/your-username/sqlite-roster.git
cd sqlite-roster
2. Run the Python script:
python roster.py
3.Output will show:
A list of users, courses, and roles (limited by query).
A computed concatenated HEX string (XYZZY...).

Example Output
. UserA CourseX 1
. UserB CourseY 0
. XYZZY4A6F686E446F650000

Learning Outcomes
1. Understanding of relational databases with SQLite
2. Use of JOIN operations in SQL.
3. Safe insertion with INSERT OR IGNORE and INSERT OR REPLACE.
4. Practical use of JSON parsing in Python.

License
. This project is open-source and available under the MIT License.
