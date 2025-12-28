"""HRM System - Main Application Entry Point"""

import os
from app import create_app, db
from app.models import User, Employee, Department, Payroll, Attendance, Leave
from config import config

# Initialize Flask application
app = create_app(os.getenv('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Register shell context for flask shell"""
    return {
        'db': db,
        'User': User,
        'Employee': Employee,
        'Department': Department,
        'Payroll': Payroll,
        'Attendance': Attendance,
        'Leave': Leave
    }

@app.before_request
def create_tables():
    """Create database tables if they don't exist"""
    db.create_all()

@app.route('/')
def index():
    """Health check endpoint"""
    return {
        'status': 'success',
        'message': 'HRM System API is running',
        'version': '1.0.0'
    }, 200

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return {
        'status': 'healthy',
        'service': 'HRM-System'
    }, 200

if __name__ == '__main__':
    # Create application context
    with app.app_context():
        # Create database tables
        db.create_all()
        print('✓ Database tables created successfully')
    
    # Run the Flask development server
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', True)
    )
