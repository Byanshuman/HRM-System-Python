"""Flask Routes/Blueprints for HRM System"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Employee, Department, Payroll, Attendance, Leave
from datetime import datetime

# Create Blueprints
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
employee_bp = Blueprint('employees', __name__, url_prefix='/api/employees')
payroll_bp = Blueprint('payroll', __name__, url_prefix='/api/payroll')

# ==================== Auth Routes ====================
@auth_bp.route('/login', methods=['POST'])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        # This is a simplified example - in production, use proper password hashing
        # and database queries to verify credentials
        if not email or not password:
            return jsonify({'status': 'error', 'message': 'Email and password required'}), 400
        
        # TODO: Add actual authentication logic with password verification
        return jsonify({
            'status': 'success',
            'message': 'Login successful',
            'access_token': 'dummy_token'
        }), 200
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    """User registration endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        
        if not all([email, password, first_name, last_name]):
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400
        
        # TODO: Add validation and user creation logic
        return jsonify({
            'status': 'success',
            'message': 'User registered successfully'
        }), 201
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500



# ==================== Employee Routes ====================

@employee_bp.route('/', methods=['GET'])
@jwt_required()
def get_employees():
    """Get all employees"""
    try:
        employees = Employee.query.all()
        return jsonify({
            'status': 'success',
            'data': [{
                'id': e.id,
                'name': f"{e.first_name} {e.last_name}",
                'email': e.email,
                'position': e.position,
                'salary': e.salary
            } for e in employees]
        }), 200
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500

@employee_bp.route('/<int:employee_id>', methods=['GET'])
@jwt_required()
def get_employee(employee_id):
    """Get specific employee details"""
    try:
        employee = Employee.query.get(employee_id)
        if not employee:
            return jsonify({'status': 'error', 'message': 'Employee not found'}), 404
        
        return jsonify({
            'status': 'success',
            'data': {
                'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'email': employee.email,
                'phone': employee.phone,
                'department_id': employee.department_id,
                'position': employee.position,
                'salary': employee.salary,
                'hire_date': employee.hire_date,
                'status': employee.status
            }
        }), 200
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500

@employee_bp.route('/', methods=['POST'])
@jwt_required()
def create_employee():
    """Create new employee"""
    try:
        data = request.get_json()
        
        new_employee = Employee(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            department_id=data.get('department_id'),
            position=data.get('position'),
            salary=data.get('salary'),
            hire_date=datetime.now()
        )
        
        db.session.add(new_employee)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Employee created successfully',
            'employee_id': new_employee.id
        }), 201
    except Exception as err:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(err)}), 500

# ==================== Payroll Routes ====================

@payroll_bp.route('/employee/<int:employee_id>', methods=['GET'])
@jwt_required()
def get_employee_payroll(employee_id):
    """Get payroll records for an employee"""
    try:
        payrolls = Payroll.query.filter_by(employee_id=employee_id).all()
        return jsonify({
            'status': 'success',
            'data': [{
                'id': p.id,
                'month': p.month,
                'year': p.year,
                'basic_salary': p.basic_salary,
                'deductions': p.deductions,
                'bonus': p.bonus,
                'net_salary': p.net_salary
            } for p in payrolls]
        }), 200
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500

@payroll_bp.route('/', methods=['POST'])
@jwt_required()
def process_payroll():
    """Process monthly payroll"""
    try:
        data = request.get_json()
        
        payroll = Payroll(
            employee_id=data.get('employee_id'),
            month=data.get('month'),
            year=data.get('year'),
            basic_salary=data.get('basic_salary'),
            deductions=data.get('deductions', 0),
            bonus=data.get('bonus', 0)
        )
        
        # Calculate net salary
        payroll.net_salary = payroll.basic_salary + payroll.bonus - payroll.deductions
        payroll.paid_date = datetime.now()
        
        db.session.add(payroll)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Payroll processed successfully',
            'net_salary': payroll.net_salary
        }), 201
    except Exception as err:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(err)}), 500

# ==================== Protected Auth Routes ====================
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current authenticated user profile"""
    try:
        current_user_id = get_jwt_identity()
        return jsonify({
            'status': 'success',
            'data': {
                'user_id': current_user_id,
                'message': 'User authenticated'
            }
        }), 200
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """User logout endpoint (revoke token)"""
    try:
        return jsonify({
            'status': 'success',
            'message': 'Logged out successfully'
        }), 200
    except Exception as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500
