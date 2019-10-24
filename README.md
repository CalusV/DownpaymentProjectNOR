# DownpaymentProjectNOR
This project utilizes Python and Django to take in user loan information through a form, before utilizing an API to generate downpayments.
The project focuses around persistent data through storing the downpayments in a database, and making them available to the user on request.
Form security and database independence are two of the main factors for choosing Django and Python for this project.

Bootstrap is also used to prettify things.

## How to run this project
1. Install python ([Download Python](https://www.python.org/downloads/)) *Only required if not already installed*
2. Install django ('python -m pip install django' in terminal) *Django is the web server environment*
3. Install requests ('python -m pip install django' in terminal) *requests is our API connection package*
4. Navigate to your folder with manage.py in a terminal
5. Run the server (type 'python manage.py runserver' to run test server environment)
6. Navigate to the URL in your web browser (127.0.0.1:8000)

## Possible future milestones
* User authentication linking loans+downpayments to individual users
* API independence through writing our own algorithms
* Graph display of interest versus loan downpayment ratios
* Let user choose between consistent loan downpayment sum or determined loan end date
