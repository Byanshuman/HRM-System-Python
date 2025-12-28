# HRM System - Python

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive **Human Resource Management System** built with Python Flask. This system provides a complete solution for managing employees, payroll, attendance tracking, leave management, and performance evaluation.

## Features

✨ **Core Features:**
- 👤 **Employee Management** - Add, update, and manage employee records
- 💰 **Payroll Processing** - Calculate and process monthly payroll with deductions and bonuses
- 📋 **Attendance Tracking** - Track employee check-in/check-out and attendance records
- 📅 **Leave Management** - Handle leave requests with approval workflow
- ⭐ **Performance Evaluation** - Manage employee performance assessments
- 🏢 **Department Management** - Organize employees by departments

🔐 **Security & Authentication:**
- JWT-based API authentication
- Password hashing with Werkzeug
- Role-based access control
- Secure session management

🏗️ **Architecture:**
- RESTful API design
- Modular Flask application structure
- SQLAlchemy ORM for database operations
- Environment-based configuration

## Project Structure

```
HRM-System-Python/
├── app/
│   ├── __init__.py           # Application factory and extensions
│   ├── models.py             # Database models (User, Employee, Payroll, etc.)
│   └── routes.py             # API endpoints and blueprints
├── config.py                 # Configuration settings
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Byanshuman/HRM-System-Python.git
   cd HRM-System-Python
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your settings
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:5000`

## API Endpoints

### Employee Endpoints
- `GET /api/employees/` - Get all employees
- `GET /api/employees/<id>` - Get employee details
- `POST /api/employees/` - Create new employee
- `PUT /api/employees/<id>` - Update employee
- `DELETE /api/employees/<id>` - Delete employee

### Payroll Endpoints
- `GET /api/payroll/employee/<id>` - Get employee payroll history
- `POST /api/payroll/` - Process payroll
- `GET /api/payroll/<id>` - Get payroll details

### Attendance Endpoints
- `GET /api/attendance/employee/<id>` - Get attendance records
- `POST /api/attendance/` - Record attendance

### Leave Endpoints
- `GET /api/leaves/` - Get leave requests
- `POST /api/leaves/` - Submit leave request
- `PUT /api/leaves/<id>/approve` - Approve leave

## Database Models

### User Model
- User authentication and login credentials
- Password hashing support
- Admin role assignment

### Employee Model
- Employee personal information
- Department assignment
- Position and salary details
- Employment status

### Payroll Model
- Monthly payroll records
- Salary calculations with deductions and bonuses
- Payment tracking

### Attendance Model
- Daily attendance records
- Check-in and check-out timestamps
- Attendance status tracking

### Leave Model
- Leave request management
- Leave type specification
- Approval workflow

## Configuration

Edit `.env` file to configure:

```env
# Flask
FLASK_ENV=development
FLASK_DEBUG=True

# Database
DATABASE_URL=sqlite:///hrm_system.db

# Security
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key
```

## Testing

Run tests using pytest:

```bash
pytest
```

## Technologies Used

- **Backend:** Flask 2.3.2, Python 3.8+
- **Database:** SQLAlchemy, SQLite/PostgreSQL/MySQL
- **Authentication:** Flask-Login, Flask-JWT-Extended
- **Validation:** Email-Validator
- **Scheduling:** APScheduler
- **Testing:** Pytest

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Byanshuman** - MBA in HR/Organizational Behavior

## Support

For support, email your-email@example.com or open an issue in the repository.

## Acknowledgments

- Thanks to the Flask community for the excellent framework
- SQLAlchemy for the powerful ORM
- All contributors and supporters of this project
