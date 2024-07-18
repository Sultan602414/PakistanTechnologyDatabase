
# DBMS of Pakistan Science and Technology

This project aims to create a DBMS for managing the science and technology in Pakistan. The web application is built using Flask and provides functionalities for inserting, deleting, updating, searching, and displaying data across multiple tables. It aims to offer a comprehensive solution for managing various types of data efficiently.

## Requirements

### Libraries
- **Python 3.x**
- **Flask**
- **MySQL**
- **mysql-connector**

### Software
- **MySQL Command Line**
- **Web Browser**
- **Visual Studio Code** 

### Hardware
- **Computer with 4GB of RAM atleast**
- **Minimum 100 MB of free disk space**
## Installation

To run this project, you should have python and MySQL installed on your computer. The latest version of python 3.12 is recommended. You might also need an IDE like VSCode (Recommended) that could run the code. You can use anyother IDE that supports python. 

Download all the necessary packages to run the code by writing this code in terminal:

```bash
    pip install -r requirements.txt
```

You should have the database installed. For this, go to the MySQL Command line and paste the following code (Make sure to update the path):

```bash
    SOURCE path_to_sql_file/PakistanScienceandTechnology.sql
```

For your ease, the PakistanScienceandTechnology.sql is also provided in this folder as well.

## Usage Instruction
To run the project, open the folder in your IDE (VSCODE Recommended). Go to the file **app.py**. On line 19, you will see **password = ""**. Inside the quotation marks enter your password of MySQL. Run the code after inserting the password. You will see that database is connected on your terminal and a link to connect to your server.

```bash
    http://127.0.0.1:5000
```

Press ctrl+clink on this link or copy it in your browser. The application will run in your browser.

## Utilizing Features
On the web application, you will see a lot of features. You can easily update, delete, modify, search and display the data. Also there is an easy functionality for navigating between different pages. Here is a list of available features:

### Select Operation:
Choose the type of operation you want to perform: Insert, Update, Delete, or Search.

### Select Table:
Select the table on which you want to perform the operation.

### Insert Data:
Fill out the form fields to insert new data into the selected table.

### Update Data:
Select the data entry you wish to update and fill out the form with the new values.

### Delete Data:
Select the data entry you wish to delete.

### Search Data:
Use the search functionality to find specific data entries.

### Display Tables:
View all data entries in a tabular format.


## Key Directories and Files

### **static/**
- **script.js:** JavaScript file for client-side scripting.
- **style.css:** CSS file for styling the web pages.

### **templates/**
This directory contains all HTML templates used by the Flask application.

- **delete_forms/:** Contains HTML templates for delete operations.
  - `clients.html`
  - `freelancercompanyassignment.html`
  - `freelancers.html`
  - `indicator_value.html`
  - `scientist.html`
  - `software_development_companies.html`
  - `software_project.html`
  - `tech_indicator.html`
  - `telecommunication.html`
  - `telecommunication_stats.html`

- **display_tables/:** Contains the HTML template for displaying all tables.
  - `AllTables.html`

- **insert_forms/:** Contains HTML templates for insert operations.
  - `clients.html`
  - `freelancercompanyassignment.html`
  - `freelancers.html`
  - `indicator_value.html`
  - `scientist.html`
  - `software_development_companies.html`
  - `software_project.html`
  - `tech_indicator.html`
  - `telecommunication.html`
  - `telecommunication_stats.html`

- **search/:** Contains HTML templates for search operations.
  - `AllTables.html`
  - `OneSearch.html`
  - `TwoSearch.html`

- **update_forms/:** Contains HTML templates for update operations.
  - `clients.html`
  - `freelancercompanyassignment.html`
  - `freelancers.html`
  - `indicator_value.html`
  - `scientist.html`
  - `software_development_companies.html`
  - `software_project.html`
  - `tech_indicator.html`
  - `telecommunication.html`
  - `telecommunication_stats.html`

- **home.html:** The home page of the web application.
- **select_operation.html:** Page to select the operation (Insert, Update, Delete, Search, Display).
- **select_table.html:** Page to select the table for the chosen operation.

### **app.py**
The main application file that sets up the Flask app and defines the routes.

### **variables.txt**
Contains configuration variables required by the application.

This project is structured to separate different functionalities into specific directories and files, making it easy to maintain and extend. The **templates/** directory is organized by the type of operation, which helps in quickly locating the required HTML templates.

## Credits
- **Team Members:**
  - Anam Fatima
  - Sultan Haider
  - Abdul Qadeer

## Third-Party Resources

### Dataset Resource
- [OpenData - Science & Technology Dataset](https://opendata.com.pk/dataset?category=Science+%26+Technology&page=1) OpenData to download datasets related to Science & Technology.

### Flask Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
  Official documentation for Flask, a lightweight web application framework in Python.

### HTML Documentation
- [HTML Tutorial - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
  Comprehensive tutorials and references for HTML (HyperText Markup Language).

### CSS Documentation
- [CSS Tutorial - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS)
  Detailed guides and references for CSS (Cascading Style Sheets) by MDN Web Docs.

### JavaScript Documentation
- [JavaScript - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  Guides, tutorials, and references for JavaScript, the programming language of the web.

### ChatGPT for Help
- ChatGPT, an AI language model, was used to assist with technical queries and guidance.

