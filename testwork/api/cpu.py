from flask import jsonify, request, url_for
from testwork.api import bp
from testwork import db
from testwork.models import Cpu


@bp.route('/cpu', methods=['POST'])
def create_cpu():
    data = request.get_json() or {}
    if 'usage' not in data:
        response = jsonify({'message': 'must include usage field'})
        response.status_code = 400
        return response
    cpu = Cpu()
    cpu.from_dict(data)
    db.session.add(cpu)
    db.session.commit()
    response = jsonify(cpu.to_dict())
    response.status_code = 201
#    response.headers['Location'] = url_for('api.get_user', id=cpu.id)
    return response
