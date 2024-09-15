
# Task Collector

## Test live
The app is live at: <br />
https://tasker-collector.onrender.com <br />
it uses the free tier, so if the server is not available, try in a minute again because it spins down due to inactivity 


## Tasker: Post Method:
```
POST https://tasker-collector.onrender.com/tasker
```
<b> Expected Json Structure: </b> <br />
```
{
    "task": "sum",
    "params": "[3,2]"
}
```
<b>-OR-</b>
```
{
    "task": "multiply",
    "params": "[3,2,3]"
}
```
### Postman query examples
![image](https://github.com/user-attachments/assets/abed2912-8eb8-4b72-ac12-846b1edd7df2)
![image](https://github.com/user-attachments/assets/f17f6e4e-72ca-4cf7-b75f-51ea50a3aff2)

## Tasker: Get Method:
To make testing easier and validate that the data is there
```
GET https://tasker-collector.onrender.com/tasker
```
### Postman query examples
![image](https://github.com/user-attachments/assets/b4692397-1f09-4d1b-951b-d6c6663ac45a)


## Test locally
1. The project was built in python 3.12.6
2. Clone the repository to your local ennviroment 
```
git clone https://github.com/JacobSobolev/tasker-collector.git
```
2. add Python virtual environment to the project and activate it 
```
python -m venv .venv
.venv\Scripts\activate (if you are on windows, you need to use PowerShell)
source venv/bin/activate (if you are on mac\linux)
```
3. install the packages
```
pip install -r requirements.txt
```
4.  in the app/__ init __.py file uncomment line 10 and comment line 11
5. run the flask app
```
flask --app run run --debug  
```
