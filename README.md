# Emergence-Music-Distribution
Admin Panel -Emergence Music Distribution
Introduction - This project uses the Python-Flask Framework to create an admin dashboard for Emergence Music Distribution. It includes features like displaying company services, enabling file downloads (PDF and CSV), and visualizing client earnings with Chart.js. The dashboard is designed to work seamlessly on both desktop and mobile devices.  Before starting, please ensure you have the following installed on your system: 
1. Python: Version 3.4 or higher.
2. 2. Git: For cloning the project repository.
3. Flask: Basic understanding of Flask for web development.
4. HTML, CSS, JavaScript: Basics for frontend integration.
5. Chart.js: Basic knowledge of dynamic graph visualization.
6. Responsive Design: Understanding of making web applications responsive.
7. File Handling: Familiarity with handling file downloads in Flask.
8. Database Connection: Knowledge of connecting Flask to MySQL databases managed via PhpMyAdmin (XAMPP).
9. Optional Authentication: Basic understanding of implementing authentication in Flask.
   
Getting Started Install Python Programming Language to the system from: 
https://www.python.org/downloads/
(Python 3.5 or higher versions are preferred)

Follow these steps to set up and run the project: 
1. Clone the Repository:    ``   git clone <repository_url>    ```
   Replace `<repository_url>` with the URL of your GitHub repository.
3. Navigate to the Project Directory:    ```    cd <project_directory>    ```
4. Set Up Virtual Environment (Optional but Recommended):    - Create a virtual environment:      ```      python -m venv venv      ```    - Activate the virtual environment:      - On Windows:        ```        venv\Scripts\activate        ```      - On macOS/Linux:        ```        source venv/bin/activate        ```
5.  Install Dependencies:    ```    pip install Flask
   pip install mysql-connector     ```  5. Run the Application: 
   - Start the Flask application:      ```      python main.py      ```    Ensure you are in the project directory (cmd)  with the “main.py”
6. Access the Application:
Click the following web browser link shown in cmd.
For example,`http://127.0.0.1:5000/` is used to view the dashboard.  
 	
Additional Information Setting up Database: - 
Install XAMPP (Windows) or MAMP (macOS). - Start MySQL and access PHPMyAdmin. - Import the `emergence_music_distribution.sql` file from the project's ‘database’ folder into PHPMyAdmin.  

Admin Credentials: Use the following credentials on the sign-in page: 

Username: admin 

Password: admin@EMG 

For more information:
https://flask.palletsprojects.com/en/3.0.x/
https://flask.palletsprojects.com/en/3.0.x/quickstart/
https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
https://flask-dev.readthedocs.io/en/stable/

NB: You can see the recorded presentation video in the folder ‘Recorded Presentation Video’ and screenshots of every page in the ‘Screenshots’ folder in the Project file.
