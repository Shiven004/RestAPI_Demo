# Small Lab REST API README
----------------------------

***Small Lab API-***</br>

This Small Lab API is based on FastAPI is a modern,fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.Following scenerios have
been covered in this script:-
1. A REST API endpoint: GET Enndpoint: To fetch the lab details associated with a particular lab_id.
2. Running POST or PUT to this endpoint runs an asynchronous task. 
   POST End Point: To add/create patient details for a particular test request.
   
***Running the Rest API on Docker***</br>

***Pre-requisites***</br>

1. Ensure the folder strucure is created similar to the one in github.</br>
2. Create virtual env using cmd - python -m venv wipro_fastapi_venv </br>
3. Actiavte virtual env - wipro_fastapi_venv\Scripts\activate. </br>
4. Ensure python version is above 3.7 or later (Python version - 3.8). </br>

***I. Build the images mentioned in the docker-compose. yml file using the below command:***</br>

docker-compose build

***II. Start the docker container using the below command:***</br>

docker-compose up -d

***III. Validating end points -***</br>

FASTAPI provides Interactive API docs to validate the endpoints.Please enter lab related data to get the correct details.

GET End Point -  http://127.0.0.1:8000/docs </br>

***Example:*** Enter lab_id = "A1001" to fetch the lab centre data.
   
POST End Point - http://127.0.0.1:8000/docs </br>

***Example:*** Enter lab_id = "A1001" and test_requested = "RT-PCR Test" to add/create patient details.

***IV. Unit Testing using PyTest -***</br>

***Run the below command in Docker CLI associated with the image:***</br>

pytest rest_api_test.py

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Running the Rest API locally***</br>

***I. Steps to reporduce-***
1. Ensure the folder strucure is created similar to the one in github.
2. Create virtual env  using cmd - python -m venv wipro_fastapi_venv.
3. Actiavte virtual env - wipro_fastapi_venv\Scripts\activate.
4. Ensure python version is above 3.7 or later (Python version - 3.7 or above).
5. Run the cmd : ***pip install -r requirements.txt*** (Navigate to the root directory where requirements.txt file is located and execute the mentioned command) </br>

***II. Run command-***</br>
***Important: Navigate to the app directory where main.py file is located and execute the below command:***</br>
python main.py

***III. Validating end points -***

FASTAPI provides Interactive API docs to validate the endpoints.Please enter lab related data to get the correct details.

GET End Point -  http://127.0.0.1:8000/lab/A1001    OR  http://127.0.0.1:8000/docs </br>

***Example:*** Enter lab_id = "A1001" to fetch the lab centre data.
   
POST End Point - Use this URL: http://127.0.0.1:8000/docs </br>

***Example:*** Enter lab_id = "A1001" and test_requested = "RT-PCR Test" to add/create patient details.

***IV. Unit Testing using PyTest -***

pytest rest_api_test.py
   

   
