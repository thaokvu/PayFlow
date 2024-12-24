# PayFlow

## Overview
PayFlow is designed to provide a secure, efficient, and user-friendly payroll management system for
organizations. It enables employees, HR, and admins to manage payroll activities seamlessly,
including salary calculations, tax deductions, and paycheck generation.


## Features
- **User Authentication (Employee, HR, Admin)**
Secure login for employees, HR personnel, and admins with role-based access control to ensure that each user only access their relevant data
- **Salary Calculation and Tax Deductions**
Automatically calculate employee salaries, including tax deductions, bonuses, and overtime, ensuring accurate payroll processing
- **Paycheck PDF Generation**
Generate downloadable PDF paychecks for employees, complete with salary breakdown, taxes, and deductions, providing a professional, paperless solution
- **Role-Based Access Control**
Restrict access to sensitive payroll data based on user roles (employee, HR, admin), ensuring data security and proper authorization for each action


## Technologies Used
### Backend
- **Python (Flask)**
    - **Flask** - Lightweight Python web framework for building the API and managing server-side logic
    - **Routing** - Manages URL routing to different endpoints for user login, payroll management, and paycheck generation
    - **User Authentication** - Implements secure login and registration processes, handling multiple roles (employee, HR, admin)
    - **Session Management** - Uses Flask's session management to maintain logged-in status and ensure secure access to protected routes
    - **Salary Calculation Logic** - Contains Python functions for salary computation, tax calculations, and deductions, streamlining payroll processing

- **SQLite**
    - **Database** - Stores user data (employee, HR, admin roles) and payroll information (salary details, tax calculations, pay periods)
    - **Lightweight** - SQLite is a file-based database that offers a simple and portable solution for the project's database needs
    - **Data Integrity** - Handles transactinal data, ensuring accurate payroll records with rollback capabilities for error handling
    - **Query Operations** - Manages all CRUD operations (Create, Read, Update, Delete) related to user and payroll data

- **ReportLab**
    - **PDF Generation** - Generates downloadable paycheck PDFs with detailed breakdowns of the salary, deductions, and taxes
    - **Dynamic Content** - Customizes paycheck layout based on user data, ensuring a professional and clear format for employees
    - **Integration** - Integrates seamlessly with the backend to generate and serve the PDFs directly to users upon request

### Frontend
- **HTML**
    - **Structure** - Provides the fundamental structure for the website's page, including the login page, payroll dashboard, and paycheck detail page
    - **Forms** - Facilitates user input through forms (login, registration, salary requests) for efficient data capture
    - **Dynamic Content** - Displays user-specific payroll data using placeholders that are dynamically filled by the backend

- **CSS**
    - **Styling** - Provides a clean and modern visual design for the user interface, ensuring an intuitive experience for users
    - **Responsive Design** - Ensures the application looks great on all devices, from desktops to mobile phones, using responsive grid layouts and media queries
    - **Notifications** - Styles notification messages (e.g. success, warning, error) for user feedback, ensuring clarity and ease of understanding

- **JavaScript**
    - **Interactivity** - Adds interactive elements, such as handling the "Download Paycheck (PDF)" button, confirmation prompts, and error handling on the frontend
    - **AJAX Requests** - Makes asynchronous requests to the backend for dynamic updates without requiring page reloads
    - **Client-Side Validation** - Validates form inputs (e.g., login credentials) to provide immediate feedback to users before submitting the data to the backend
    - **User Notification** - Implements notifications to inform users of successful or failed actions (e.g. paycheck generation) for better UX


## Prerequisites
- Python 3.x
- Flask
- ReportLab (for PDF generation)

## Setup
1. **Clone the Repository**
```bash
git clone https://github.com/thaokvu/PayFlow.git
```

2. **Create and activate a virtual environment** (optional but recommended)
```bash
python3 -m venv venv
# For Unix-based platforms (Linux and macOS)
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt

# If you don't have a requirements.txt, manually install the dependencies
pip install flask reportlab
```

4. **Run the Flask Application**
```bash
python app.py

# By default, the app will be running at http://127.0.0.1:5000/
```

5. **Access the Application**
    - **Login Page**
    `http://127.0.0.1:5000/`
        - **Admin**
            - Username - admin
            - Password - adminpassword
        - **Employee**
            - Username - employee
            - Password - employeepassword
        - **Manager**
            - Username - manager
            - Password - managerpassword
   <img width="956" alt="PayFlow Login Page (index html)" src="https://github.com/user-attachments/assets/05a02618-184f-4d18-ad13-e7a9b527a80f" />
   
    - **Dashboard Page**
    `http://127.0.0.1:5000/dashboard/<username>`
        - **Admin**
        `http://127.0.0.1:5000/dashboard/admin`
        - **Employee**
        `http://127.0.0.1:5000/dashboard/employee`
        - **Manager**
        `http://127.0.0.1:5000/dashboard/manager`
   <img width="959" alt="PayFlow Dashboard (Admin)" src="https://github.com/user-attachments/assets/cc1a9389-f541-4d41-978f-d05f7c143ec9" />
   <img width="959" alt="PayFlow Dashboard (Employee)" src="https://github.com/user-attachments/assets/782bc02b-a9cf-4840-9eb2-e4de22b108b4" />
   <img width="959" alt="PayFlow Dashboard (Manager)" src="https://github.com/user-attachments/assets/483dc338-ef7e-4c90-8208-0b5a6efa5295" />

    - **Paycheck Details Page**
    `http://127.0.0.1:5000/paycheck_details/<username>`
        - **Admin**
        `http://127.0.0.1:5000/paycheck_details/admin`
        - **Employee**
        `http://127.0.0.1:5000/paycheck_details/employee`
        - **Manager**
        `http://127.0.0.1:5000/paycheck_details/manager`
  <img width="959" alt="PayFlow Paycheck Details (Admin)" src="https://github.com/user-attachments/assets/0e1b3a75-b51d-446e-8682-b20b45f29fed" />
  <img width="305" alt="PayFlow Paycheck Details PDF (Admin)" src="https://github.com/user-attachments/assets/6b1f42e1-4e88-4ade-bb24-69e3d9eaff43" />
  <img width="959" alt="PayFlow Paycheck Details (Employee)" src="https://github.com/user-attachments/assets/401b9835-600e-4f8d-a398-11e4f2aba21c" />
  <img width="305" alt="PayFlow Paycheck Details PDF (Employee)" src="https://github.com/user-attachments/assets/f55d7575-3425-46b5-be96-5117ba9db315" />
  <img width="959" alt="PayFlow Paycheck Details (Manager)" src="https://github.com/user-attachments/assets/c2b5399c-2531-48ad-82e0-af63b91e71a5" />
  <img width="304" alt="PayFlow Paycheck Details PDF (Manager)" src="https://github.com/user-attachments/assets/33a2511b-922b-4e3e-9551-67ea167daafa" />


## Application Structure
- **`app.py`** - Contains the main Flask application logic, including the routes for login, dashboard, and paycheck PDF generation
- **`templates/`** - Contains the HTML files (e.g., `index.html`, `dashboard.html`, `paycheck_details.html`) used for rendering the web pages
- **`static/`** - Contains the static files such as images or stylesheets
- **`requirements.txt`** - Lists the Python dependencies for the application

## Routes
1. **Homepage** (`/`)
- **Method** - `GET`
- Displays the login form for users

2. **Login** (`/login`)
- **Method** - `POST`
- Handles user login
    - Upon success, redirects the user to their dashboard

3. **Dashboard** (`/dashboard/<username>`)
- **Method** - `GET`
- Displays the user-specific dashboard based on the username
    - It shows details like role and provides a link to generate a paycheck

4. **Generate Paycheck PDF** (`/generate_paycheck/<username>`)
- **Method** - `GET`
- Generates and downloads the paycheck PDF for the user, including the payroll details like salary, tax deductions, and net pay

5. **Paycheck Details** (`/paycheck_details/<username>`)
- **Method** - `GET`
- Displays detailed paycheck information (salary, deductions, etc.) in a clean, readable format on the web page

## PayFlow Demo
https://github.com/user-attachments/assets/ed090934-f522-4776-b9ea-26bb487de8de

## Customization
1. **Add More Roles** - You can add additional roles (e.g., "HR", "Contractor", etc) by adding corresponding payroll data in the `payroll_data` dictionary in `app.py`.
2. **Modify the PDF Style** - The PDF generation logic can be customized to match your company's branding (e.g., colors, fonts, layout).
3. **Authentication Logic** - Right now, the app uses a simple username check, but you can replace this with proper authentication (e.g., using Flask-Login for session management).

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push orgin feature-xyz`).
5. Create a new pull request.
