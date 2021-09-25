# Small Lab API enpoints README
------------------------------

### Small Lab API
This Small Lab API is based on FastAPI is a modern,fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.Following scenerios have
been covered in this script:-
1. A REST API endpoint: GET Enndpoint: To fetch the lab associated with the lab_id.
2. Running POST or PUT to this endpoint runs an asynchronous task. 
   POST End Point: To add/create patient details.


### I. Steps to reporduce-
1. Ensure the folder strucure is created similar to the one here in github.
2. Create virtual env  using cmd - python -m venv wipro_fastapi_venv
3. Actiavte virtual env - wipro_fastapi_venv\Scripts\activate
4. Ensure python version is above 3.7 or later (Python version - 3.8)
5. pip install -r requirements.txt

### II. Run command-
uvicorn main:app --reload


### III. Validating end points -

GET End Point -  http://127.0.0.1:8000/lab/A1001
   
POST End Point - Use this URL: http://127.0.0.1:8000/docs

#### Unit Testing uising PyTest -

pytest RestApi_test.py
   

   
