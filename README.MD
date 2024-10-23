# PROGRA102 - Flask REST API

## Description

This project is a REST API developed with Flask that allows managing users and their roles, as well as performing video analysis to detect specific objects.

## Requirements

- Python 3.9
- Flask 3.0.3

## Installation

1.  Clone the repository:

    ```
    git clone https://github.com/tu_usuario/tu_repositorio.git cd tu_repositorio
    ```

2.  Create and activate a virtual environment:

    ```
    conda create --name my_flask_project python=3.9
    conda activate my_flask_project
    ```

3.  Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

## Project Structure

```
flaskapi/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models/
│   │   ├── user.py
│       └── data_handler.py
├── run.py
├── requirements.txt
```

## Use

### Endpoints

#### Create a User

- URL: /api/send_name
- Method: POST
- Body:

    ```
      {
        "name": "Juan",
        "last_name": "Pérez"
      }
    ```

#### Get Greetings

- URL: /api/get_greetings
- Method: GET
- Description: Returns a list of greetings for all users.

#### Actualizar un Usuario

- URL: /api/update_user/<user_id>
- Method: PUT o PATCH
- Body:

    ```
        {
            "name": "Carlos"
        }
    ```
o

    ```
        {
            "last_name": "Ramírez"
        }
    ```

#### Get All Users

- URL: /api/users
- Method: GET
- Description: Returns a list of all users.

#### Eliminar un Usuario

- URL: /api/delete_user/<user_id>
- Method: DELETE
- Description: Delete a specific user based on their ID.
