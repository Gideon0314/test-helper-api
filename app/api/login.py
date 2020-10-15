# -*- coding: UTF-8 -*-
from app.api.auth import basic_auth
from flask import jsonify, g
from app import db
from . import bp


@bp.route('/user/login', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_jwt()
    # g.user_id.ping()
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": {
                "token": token
            }
        }
        )
