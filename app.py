from flask import Flask, render_template, request, jsonify, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# List of tables
tables = [
    'Clients', 'FreelancerCompanyAssignment', 'Indicator_Value',
    'Scientist', 'Software_Development_Companies', 'Software_House',
    'Software_Project', 'Tech_Indicator', 'Telecommunication', 'Telecommunication_Stats', 'Freelancers'
]

# Connecting to the dataBase
import mysql.connector as c
from mysql.connector import Error

dataBase = c.connect(
host="localhost", # Hostname of the MySQL server
user="root", # Username to log in to the MySQL server
password="", # Password to log in to the MySQL server
database="scienceandtechnology" # Name of the database to use
)

# Check if the connection is successful
if dataBase.is_connected():
    print("Successfully Connected")
    cursor = dataBase.cursor()

# Routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/select_operation')
def select_operation():
    return render_template('select_operation.html')

@app.route('/select_table/<operation>', methods=['GET', 'POST'])
def select_table(operation):
    if request.method == 'POST':
        selected_table = request.form['table']
        if operation == 'insert':
            return redirect(url_for('insert_form', table=selected_table))
        elif operation == 'delete':
            return redirect(url_for('delete_form', table=selected_table))
        elif operation == 'update':
            return redirect(url_for('update_form', table=selected_table))
        elif operation == 'display_all':
            return redirect(url_for('display_all', table=selected_table))
        elif operation == 'display_on_search':
            return redirect(url_for('display_on_search', table=selected_table))
    return render_template('select_table.html', operation=operation, tables=tables)

@app.route('/insert_form/<table>')
def insert_form(table):
    return render_template(f'insert_forms/{table.lower()}.html')

@app.route('/delete_form/<table>')
def delete_form(table):
    return render_template(f'delete_forms/{table.lower()}.html')

@app.route('/update/<table>', methods=['GET'])
def update_form(table):
    return render_template(f'update_forms/{table.lower()}.html')

@app.route('/display_on_search/<table>', methods=['GET'])
def display_on_search(table):
    if table == "Software_Project":
        return render_template(f'search/TwoSearch.html', table = table)
    return render_template(f'search/OneSearch.html', table = table)

@app.route('/display_all/<table>', methods=['GET'])
def display_all(table):
    if table == "Software_Development_Companies":
        table = "SoftwareDevelopmentCompanies"
    if table == "Software_House":
        table = "SoftwareHouse"
    if table == "Software_Project":
        table = "SoftwareProject"
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    rows = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]

    return render_template(f'display_tables/AllTables.html', table = table, rows=rows, col_names=col_names)


# ____________________________________________________________________________________________________________________________________
#                                             INSERTING IN TABLES
# ____________________________________________________________________________________________________________________________________

@app.route('/process_insert/<table>', methods=['POST'])
def process_insert(table):
    data = request.form
    # Process insertion based on table
    if table == 'Clients':
        sdc_id = data['sdc_id']
        client_name = data['client_name']
        
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Client")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO CLIENTS VALUES ({clients}, {sdc_id}, '{client_name}');"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            clients = int(clients) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}. "

    elif table == 'FreelancerCompanyAssignment':
        company_id = data['company_id']
        freelancer_id = data['freelancer_id']
        payment = data['payment']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into FreelancerCompanyAssignment")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO freelancercompanyassignment VALUES ({freelanceCompanyAssignment}, {company_id}, {freelancer_id}, {payment});"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            freelanceCompanyAssignment = int(freelanceCompanyAssignment) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Indicator_Value':
        indicator_code = data['indicator_code']
        indicator_name = data['indicator_name']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Indicator_Value")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO Indicator_Value VALUES ('{indicator_code}', '{indicator_name}');  "
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Scientist':
        name = data['name']
        discipline = data['discipline']
        qualification = data['qualification']
        affiliation = data['affiliation']
        tech_id = data['tech_id']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Scientist")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO Scientist VALUES ({Scientist}, '{name}', '{discipline}', '{qualification}', '{affiliation}', {tech_id});  "
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            Scientist = int(Scientist) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Software_Development_Companies':
        company_name = data['company_name']
        rating = data['rating']
        location = data['location']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into SoftwareDevelopmentCompanies")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO SoftwareDevelopmentCompanies VALUES ({SoftwareDevelopmentCompanies}, '{company_name}',{rating} , '{location}');  "
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            SoftwareDevelopmentCompanies = int(SoftwareDevelopmentCompanies) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Software_House':
        name = data['name']
        about = data['about']
        software_company = data['software_company']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Software_House")
        # Perform insertion logic (database operations)
        try:
            query = f" INSERT INTO SoftwareHouse VALUES ({SotwareHouse}, '{name}', '{about}', {software_company});"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            SotwareHouse = int(SotwareHouse) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}. "

    elif table == 'Software_Project':
        softwarehouse_id = data['softwarehouse_id']
        sdc_id = data['sdc_id']
        project = data['project']
        # Perform insertion logic (database operations)
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Client")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO SoftwareProject VALUES ({softwarehouse_id}, {sdc_id}, '{project}');"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Tech_Indicator':
        year = data['year']
        value = data['value']
        indicator_code = data['indicator_code']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Tech_Indicator")
        # Perform insertion logic (database operations)
        try:
            query = f" INSERT INTO tech_indicator VALUES ({TechIndicator}, {year}, {value},'{indicator_code}'); "
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            TechIndicator = int(TechIndicator) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Telecommunication':
        tsid = data['tsid']
        softwarehouse_id = data['softwarehouse_id']
        month = data['month']
        jazz = data['jazz']
        ufone = data['ufone']
        telenor = data['telenor']
        warid = data['warid']
        zong = data['zong']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Telecommunication")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO Telecommunication VALUES ({Telecommunication}, {tsid}, {tsid}, '{month}', {jazz}, {ufone}, {telenor}, {warid}, {zong});"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            Telecommunication = int(Telecommunication) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Telecommunication_Stats':
        cellular_mobile = data['cellular_mobile']
        wireless = data['wireless']
        year = data['year']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Telecommunication_Stats")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO Telecommunication_Stats VALUES ({telecommunication_stats}, {cellular_mobile},{wireless},{year});  "
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            telecommunication_stats = int(telecommunication_stats) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Freelancers':
        name = data['name']
        profession = data['profession']
        earning = data['earning']
        reviews = data['reviews']
        hourrate = data['hourrate']
        # Reading ID of Client
        with open("variables.txt", "r") as f:
            content = f.read()

        clients, freelanceCompanyAssignment, Scientist, SoftwareDevelopmentCompanies, SotwareHouse, TechIndicator, Telecommunication, telecommunication_stats, freelancer = content.split(" ")

        print("Inserting Into Client")
        # Perform insertion logic (database operations)
        try:
            query = f"INSERT INTO freelancers VALUES ({freelancer}, '{name}', '{profession}', {earning}, '{reviews}', '{hourrate}'); "
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            freelancer = int(freelancer) + 1
            with open("variables.txt", "w") as f:
                f.write(f"{clients} {freelanceCompanyAssignment} {Scientist} {SoftwareDevelopmentCompanies} {SotwareHouse} {TechIndicator} {Telecommunication} {telecommunication_stats} {freelancer}")
            print("Data Inserted Successfully.")
            result = "Data Inserted Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    else:
        result = "Table not found"

    # return render_template('success.html', result=result)
    flash(result)
    return render_template(f'insert_forms/{table.lower()}.html')

# ____________________________________________________________________________________________________________________________________
#                                             DELETING IN TABLES
# ____________________________________________________________________________________________________________________________________
@app.route('/process_delete/<table>', methods=['POST'])
def process_delete(table):
    data = request.form
    # Process deletion based on table
    if table == 'Clients':
        client_id = data['client_id']
        try:
            query = f"DELETE FROM Clients WHERE companyclient_id = {client_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'FreelancerCompanyAssignment':
        fca_id = data['assignment_id']
        try:
            query = f"DELETE FROM FreelancerCompanyAssignment WHERE freelancercompany_id = {fca_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Indicator_Value':
        indicator_code = data['indicator_code']
        try:
            query = f"DELETE FROM Indicator_Value WHERE indicator_code = '{indicator_code}';"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Scientist':
        scientist_id = data['scientist_id']
        try:
            query = f"DELETE FROM Scientist WHERE scientistid = {scientist_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}."
        
    elif table == 'Software_Development_Companies':
        sdc_id = data['company_id']
        try:
            query = f"DELETE FROM SoftwareDevelopmentCompanies WHERE sdc_id = {sdc_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Software_House':
        sh_id = data['house_id']
        try:
            query = f"DELETE FROM SoftwareHouse WHERE softwarehouse_id = {sh_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Software_Project':
        sh_id = data['software_house']
        sdc_id = data['softwareDevelopment']
        try:
            query = f"DELETE FROM SoftwareProject WHERE softwarehouse_id = {sh_id} AND sdc_id = {sdc_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Tech_Indicator':
        ti_id = data['indicator_id']
        try:
            query = f"DELETE FROM Tech_Indicator WHERE techid = {ti_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Telecommunication':
        t_id = data['telecom_id']
        try:
            query = f"DELETE FROM Telecommunication WHERE telecommunication_id = {t_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
    elif table == 'Telecommunication_Stats':
        ts_id = data['stat_id']
        try:
            query = f"DELETE FROM Telecommunication_Stats WHERE tsid = {ts_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}. "
        
    elif table == 'Freelancers':
        freelancer_id = data['freelancer_id']
        try:
            query = f"DELETE FROM Freelancers WHERE freelancer_id = {freelancer_id};"
            cursor.execute(query)
            dataBase.commit()
            result = "Data Deleted Successfully."
        except Error as e:
            result = f"Error occurred: {e}"
            result = f"Error occured, {e}."
        
    else:
        result = "Table not found"

    flash(result)
    return render_template(f'delete_forms/{table.lower()}.html')
    # return redirect(url_for('delete_form', table=table))

# ____________________________________________________________________________________________________________________________________
#                                             UPDATING IN TABLES
# ____________________________________________________________________________________________________________________________________
@app.route('/update/<table>', methods=['POST'])
def process_update(table):
    data = request.form
    # Process insertion based on table
    if table == 'Clients':
        id = data["company_client_id"]
        sdc_id = data['sdc_id']
        client_name = data['client_name']
        
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE Clients SET SDC_ID = {sdc_id}, Client_Name = '{client_name}'  WHERE CompanyClient_ID  = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'FreelancerCompanyAssignment':
        id = data['fc_assignment_id']
        company_id = data['company_id']
        freelancer_id = data['freelancer_id']
        payment = data['payment']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE freelancercompanyassignment SET Company_ID  = {company_id}, Freelancer_ID = {freelancer_id}, payment= {payment}  WHERE FreelancerCompany_ID  = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Indicator_Value':
        indicator_code = data['indicator_code']
        indicator_name = data['indicator_name']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE Indicator_value SET Indicator_Name = '{indicator_name}'  WHERE Indicator_Code  = '{indicator_code}';"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Scientist':
        id = data['scientist_id']
        name = data['name']
        discipline = data['discipline']
        qualification = data['qualification']
        affiliation = data['affiliation']
        tech_id = data['tech_id']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE Scientist SET Name = '{name}', Discipline = '{discipline}', Qualification = '{qualification}', Affiliation = '{affiliation}',TechID  = {tech_id}   WHERE ScientistID  = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Software_Development_Companies':
        id = data['softwaredevelopmentcompany_id']
        company_name = data['company_name']
        rating = data['rating']
        location = data['location']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE SoftwareDevelopmentCompanies SET Rating  = {rating}, Company_Name  = '{company_name}', Location = '{location}'  WHERE SDC_ID   = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Software_House':
        id = data['softwarehouse_id']
        name = data['name']
        about = data['about']
        software_company = data['software_company']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE softwareHouse SET Name = '{name}', About = '{about}', SoftwareCompany = {software_company}  WHERE SoftwareHouse_ID   = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Software_Project':
        softwarehouse_id = data['softwarehouse_id']
        sdc_id = data['sdc_id']
        project = data['project']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE softwareproject SET Project = '{project}' WHERE SoftwareHouse_ID  = {softwarehouse_id} AND SDC_ID={sdc_id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Tech_Indicator':
        id = data['tech_id']
        year = data['year']
        value = data['value']
        indicator_code = data['indicator_code']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE tech_Indicator SET year = {year}, value = {value}, Indicator_Code  = '{indicator_code}'  WHERE TechID   = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}. "

    elif table == 'Telecommunication':
        id = data['telecommunication_id']
        tsid = data['tsid']
        softwarehouse_id = data['softwarehouse_id']
        month = data['month']
        jazz = data['jazz']
        ufone = data['ufone']
        telenor = data['telenor']
        warid = data['warid']
        zong = data['zong']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE Telecommunication SET TSID = {tsid}, SoftwareHouse_ID = {softwarehouse_id}, month = '{month}', jazz = {jazz}, ufone = {ufone}, telenor = {telenor}, warid = {warid}, zong = {zong}  WHERE Telecommunication_id    = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}. "

    elif table == 'Telecommunication_Stats':
        id = data['telecommunication_stats_id']
        cellular_mobile = data['cellular_mobile']
        wireless = data['wireless']
        year = data['year']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE telecommunication_stats SET Cellular_Mobile  = {cellular_mobile}, wireless = {wireless}, year = {year}  WHERE TSID  = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    elif table == 'Freelancers':
        id = data['freelancer_id']
        name = data['name']
        profession = data['profession']
        earning = data['earning']
        reviews = data['reviews']
        hourrate = data['hourrate']
        # Perform Updation logic (database operations)
        try:
            query = f"UPDATE freelancers SET Name = '{name}',  Profession = '{profession}', Earning = {earning}, Reviews = {reviews}, Hour_Rate = {hourrate}  WHERE freelancer_id  = {id};"
            # Execute the SQL query
            cursor.execute(query)

            dataBase.commit()
            print("Data Updated Successfully.")
            result = "Data Updates Successfully."

        except Error as e:
            print("Error Occured ", e)
            result = f"Error occured, {e}."

    else:
        result = "Table not found"

    flash(result)
    # return render_template('success.html', result=result)
    return render_template(f'update_forms/{table.lower()}.html')

# ____________________________________________________________________________________________________________________________________
#                                             Displaying The TABLES On Search
# ____________________________________________________________________________________________________________________________________
@app.route('/process_search/<table>', methods=['POST'])
def process_search(table):
    data = request.form
    id = data["client_id"]
    if table == 'Clients':
        query = f"SELECT * FROM clients Where CompanyClient_ID = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]

    elif table == 'FreelancerCompanyAssignment':
        query = f"SELECT * FROM FreelancerCompanyAssignment Where FreelancerCompany_ID  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Indicator_Value':
        query = f"SELECT * FROM Indicator_Value Where Indicator_Code  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Scientist':
        query = f"SELECT * FROM Scientist Where ScientistID  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Software_Development_Companies':
        query = f"SELECT * FROM SoftwareDevelopmentCompanies Where Sdc_id  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Software_House':
        query = f"SELECT * FROM SoftwareHouse Where SoftwareHouse_ID  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Software_Project':
        id2 = data['softwareDevelopment']
        query = f"SELECT * FROM SoftwareProject Where Sdc_id  = {id2} and SoftwareHouse_ID={id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Tech_Indicator':
        query = f"SELECT * FROM Tech_Indicator Where TechID  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Telecommunication':
        query = f"SELECT * FROM Telecommunication Where Telecommunication_id  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]

    elif table == 'Telecommunication_Stats':
        query = f"SELECT * FROM Telecommunication_Stats Where TSID  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    elif table == 'Freelancers':
        query = f"SELECT * FROM Freelancers Where Freelancer_ID  = {id};"
        cursor.execute(query)
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        
    else:
        result = "Table not found"
        return jsonify({'Result': result})

    return render_template(f'search/AllTables.html', table = table, rows=rows, col_names=col_names)
    
    

if __name__ == '__main__':
    app.run(debug=True)
    if dataBase.is_connected():
        cursor.close() # Close the cursor object
        dataBase.close() # Close the database connection
        print("My SQL Connection is Closed.")
