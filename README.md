# Marketplace | Django

## Description

This is a simple Django project that allows users to create, read, update, and delete items from a marketplace. The project is built using Django, ~~Django REST framework~~ _(planned in next version)_, and SQLite.

## Features

- User authentication
- CRUD operations on items
- User profile page
- User can only edit/delete items they created
- _TODO_ other features

## Installation

1. Clone the repository
2. Create a virtual environment

    ```bash
    python -m venv .venv
    ```
3. Activate the virtual environment
   
    - Windows

        ```bash
        .venv\Scripts\activate
        ```

    - Linux

        ```bash
        source .venv/bin/activate
        ```

        > **Note** : for fish shell, use `source .venv/bin/activate.fish`

        > **Note** : You can deactivate the virtual environment by running `deactivate` in the terminal later

4. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

5. Run the server

    ```bash
    python manage.py runserver
    ```

6. Open the browser and go to `http://localhost:8000`
7. _TODO_ finalize

## Screenshots

> **TODO:** Update screenshots

![Home Page](screenshots/home.png)

![Item Detail Page](screenshots/item_detail.png)

![Profile Page](screenshots/profile.png)
