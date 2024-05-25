# User CURD

This project is a web application for managing user data, providing CRUD (Create, Read, Update, Delete) operations. The frontend is hosted at `http://127.0.0.1:5500/html/dashboard.html`, and the backend is powered by FastAPI, running on `http://127.0.0.1:8888`.

![image](https://github.com/Hamza-Ghaffar/CURD_FASTAPI/assets/73717242/7503cb68-9734-4236-bd1a-7b2f5eb5c7ac)





## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Thanks](#thanks)

## Overview

The User Management System is designed to simplify the process of managing user data for web applications. It allows administrators to perform CRUD operations on user records, facilitating user registration, updating user information, and managing user accounts efficiently.

## Features

- Create, Read, Update, and Delete user data
- Frontend interface for managing users
- Backend API endpoints for user CRUD operations
- Seamless integration between frontend and backend

## Technologies Used

- Frontend:
  - HTML5
  - CSS3
  - JavaScript

- Backend:
  - FastAPI
  - Python

## Installation

To install and run the User Management System on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd your-repo
    ```

3. Start the frontend server:
    ```bash
    cd frontend
    python3 -m http.server 5500
    ```

4. Start the backend server:
    ```bash
    cd ../backend
    uvicorn main:app --reload --port 8888
    ```

5. Access the application:
   Open your web browser and visit `http://127.0.0.1:5500/html/dashboard.html` to access the user management system.

## Usage

The User Management System provides a user-friendly interface for managing user data. Administrators can perform CRUD operations on user records using the frontend interface. Additionally, the backend API endpoints can be utilized for programmatic access to user data.

## Contributing

Contributions to the User Management System are welcome! If you have suggestions for improvement or want to report issues, please open an issue or submit a pull request.


## Thanks

Special thanks to ChatGPT for providing assistance during the development of this project!
