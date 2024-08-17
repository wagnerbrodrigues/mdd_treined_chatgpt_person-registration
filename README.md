Person Registration with Token
This project is a simple web application for registering people with an ID and name, generating an MD5 token for each person, and storing this information in a MongoDB database. The application is built using Flask and Docker, and it was generated with the assistance of ChatGPT using Model-Driven Development (MDD), with the models stored in the diagrams folder. The project was created using a custom-trained ChatGPT model, which you can find here.

Project Structure
arduino
Copiar código
person_registration/
├── app.py
├── Dockerfile
├── requirements.txt
├── static/
│   └── styles.css
├── templates/
│   └── index.html
└── docker-compose.yml
Getting Started
Prerequisites
Docker
Docker Compose
Running the Application
Clone the repository:
bash
Copiar código
git clone https://github.com/wagnerbrodrigues/mdd_chatgpt_person-registration
cd person-registration
Build and run the Docker containers:
bash
Copiar código
docker-compose up --build
Open your browser and go to http://localhost:8080 to access the application.
Endpoints
/: Main page to register a person and view the list of registered people.
/register: Endpoint to register a new person (via POST request).
/get_people: Endpoint to get the list of registered people (via GET request).
Files
app.py: The main Flask application that handles routing and interactions with MongoDB.
Dockerfile: Defines the Docker image for the Flask application.
requirements.txt: Lists the dependencies for the Flask application.
templates/index.html: The HTML template for the web page.
static/styles.css: The CSS file for styling the web page.
docker-compose.yml: Defines the services for the web application and MongoDB, and how they interact.
Example Usage
Enter an ID and name in the form.
Click "Register" to add the person.
The list of registered people will be updated automatically.
Acknowledgments
This project was generated with the assistance of ChatGPT using Model-Driven Development (MDD) and a custom-trained model, available here.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This version now includes the reference to the custom-trained ChatGPT model. Let me know if there's anything else you'd like to add!
