# Project Overview

This project develops an API from the definition in https://gitlab.scratchpay.com/-/snippets/42/raw/main/swagger.yaml, stores the user data, validates the workflow and containerises the application.

## Workflow
user-management-REST/ is the WORKING DIRECTORY

The API has been developed with django rest framework following the swagger spec for the API definition. The endpoints were tested with the POSTMAN API client.


Measures have been take to ensure the setup is configured to generally work across platforms different platforms (test on ubuntu, debian and MacOS)

The application has been containerized as the project was implemented to be runnable by docker. The manifests were then deployed and validated on an kubernetes cluster (EKS).





---

## Technical Considerations

Application
- Schema was designed to meet the guidelines provided in the swagger docs
- The CSV seeder was built to communicate with the database with error handling measures

Infrastructure
- The application was containerized and pushed to a container registry(docker hub)
- Kubernetes manifests were built to orchestrate the application
- Application environmental variables were passed using secrets which was sealed (using sealed secrets) as default secrets aren't really secure (using base64)
- Using an independent db (like production) rather than running the database as a container


## How to setup

Application

Without docker
- Create a virtual environment (optional - https://realpython.com/python-virtual-environments-a-primer/ )
- Install dependencies (pip3 install -r requirements.txt )
- Create an env file following the format in .env.example file
- Make migrations (python3 manage.py makemigrations)
- Migrate (python3 manage.py migrate)

# start the seeder
- Run server (python3 manage.py stats)

# start the application server
- Run server (python3 manage.py runserver)


With docker (server)
- docker build . -t <tag-name>
- docker run -p 8000:8000 -e NAME="<name>" -e USER="<user>" -e PASSWORD="<password>" -e HOST="<host>" -e PORT="<port>" -e SECRET_KEY="<secret-key>" -e ALLOWED_HOSTS="localhost 127.0.0.1 0.0.0.0 [::1]" lexmill99/scratch-pay:v5



Infrastructure
- Create a secret with the envs or use a secret manager
- Run kubectl apply -f <local-path>/manifests 
N.B: If your host ip is not in allowed host env, probes may fail



## IMAGES 

<div align="center">
  <a href="/">
    <img src="https://res.cloudinary.com/dtvv1oyyj/image/upload/v1667501093/Screenshot_from_2022-11-03_19-39-06.png" width="240"/>
  </a>
</div>

<div align="center">
  <a href="/">
    <img src="https://res.cloudinary.com/dtvv1oyyj/image/upload/v1667501088/Screenshot_from_2022-11-03_19-39-33.png" width="240"/>
  </a>
</div>

<div align="center">
  <a href="/">
    <img src="https://res.cloudinary.com/dtvv1oyyj/image/upload/v1667501077/Screenshot_from_2022-11-03_19-40-01.png" width="240"/>
  </a>
</div>