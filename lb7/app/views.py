from app import db
from flask_login import login_required, current_user
from flask import Blueprint, request, render_template
from app.models import Employee, Position, Division, Job, User

bp = Blueprint('bp', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/job_list', methods=['GET'])
@login_required
def job_list():
    job = Employee.query.join(Job).order_by(Job.date_of_employment)
    if request.args.get('division_id'):
        job = job.filter(Job.division_id == request.args.get('division_id'))
    elif request.args.get('after_date'):
        job = job.filter(Job.date_of_employment > request.args.get('after_date'))
    job = job.all()
    return render_template("job_list.html", job_list=job)

@bp.route('/job/put', methods=['PUT'])
def put_job():
    dismissal = Job.query.get(request.args.get('id'))
    dismissal.date_of_dismissal = request.args.get('date_of_dismissal')
    db.session.add(dismissal)
    db.session.commit()
    return dismissal.to_dict()

@bp.route('/employee/add', methods=['POST'])
def add_employee():
    employee = Employee(**request.args)
    db.session.add(employee)
    db.session.commit()
    return employee.to_dict()

@bp.route('/employee/get', methods=['GET'])
def get_employee():
    employee = Employee.query.get(request.args.get('id'))
    return employee.to_dict()

@bp.route('/employee/put', methods=['PUT'])
def edit_employee():
    edit_employee = Employee.query.get(request.args.get('id'))
    if request.args.get('second_name'):
        edit_employee.second_name = request.args.get('second_name')
    if request.args.get('first_name'):
        edit_employee.first_name = request.args.get('first_name')
    if request.args.get('surname'):
        edit_employee.surname = request.args.get('surname')
    if request.args.get('address'):
        edit_employee.address = request.args.get('address')
    if request.args.get('date_of_birth'):
        edit_employee.date_of_birth = request.args.get('date_of_birth')
    db.session.add(edit_employee)
    db.session.commit()
    return edit_employee.to_dict()

@bp.route('/employee/delete', methods=['DELETE'])
def del_employee():
    employee = Employee.query.get(request.args.get('id'))
    db.session.delete(employee)
    db.session.commit()
    return employee.to_dict()

@bp.route('/position/add', methods=['POST'])
def add_position():
    position = Position(**request.args)
    db.session.add(position)
    db.session.commit()
    return position.to_dict()

@bp.route('/position/get', methods=['GET'])
def get_position():
    position = Position.query.get(request.args.get('id'))
    return position.to_dict()

@bp.route('/position/delete', methods=['DELETE'])
def del_position():
    position = Position.query.get(request.args.get('id'))
    db.session.delete(position)
    db.session.commit()
    return position.to_dict()

@bp.route('/division/add', methods=['POST'])
def add_division():
    division = Division(**request.args)
    db.session.add(division)
    db.session.commit()
    return division.to_dict()

@bp.route('/division/get', methods=['GET'])
def get_division():
    division = Division.query.get(request.args.get('id'))
    return division.to_dict()

@bp.route('/division/delete', methods=['DELETE'])
def del_division():
    division = Division.query.get(request.args.get('id'))
    db.session.delete(division)
    db.session.commit()
    return division.to_dict()

@bp.route('/job/add', methods=['POST'])
def add_job():
    employee = Employee.query.get(request.args.get('employee_id'))
    position = Employee.query.get(request.args.get('position_id'))
    division = Employee.query.get(request.args.get('division_id'))
    new_employee = {
        "date_of_employment": request.args.get('date_of_employment'),
        "employee_id": employee.id,
        "position_id": position.id,
        "division_id": division.id,
    }
    add_job = Job(**new_employee)
    db.session.add(add_job)
    db.session.commit()
    return add_job.to_dict()

























