# This is a test proyect for crowdbotics

## Api Usage:

This project uses JWT for api authentication, as well as session and basic authentication for the browsable web api.

In order to obtain your JWT credentials you must send a post request to /login-api

`
curl -d '{"username":"wcolmenares", "password":"testtest"}' -H "Ccalhost:8000/login-api/
`

After obtain it, you can start creating/updating/deleting pets.

Examples using python requests library:

#### Get list of pets

`
requests.get('http://127.0.0.1:8000/api/v1/', headers = {'Authorization': 'JWT <yourtoken>'})
`

#### Update a pet

`
requests.put('http://127.0.0.1:8000/api/v1/<pet_id>/', data={'birthday': <new_birthday>},headers={'Authorization': 'JWT <yourtoken>'})
`

#### Delete a pet

`
requests.delete('http://127.0.0.1:8000/api/v1/<pet_id>/', headers={'Authorization': 'JWT <yourtoken>'})
`