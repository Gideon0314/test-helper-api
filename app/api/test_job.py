# -*- coding: UTF-8 -*-
from flask import jsonify
from app.libs.run_case import web_test, api_cases_test
from . import bp
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor(2)


@bp.route('/web_jobs', methods=['GET'])
def web_jobs():
    """test"""
    # executor.submit(api_test)
    executor.submit(web_test)
    return jsonify(
        {
            "status": 200,
            'msg': 'Two jobs was launched in background!'
        }
        )


@bp.route('/api_jobs', methods=['GET'])
def api_jobs():
    """test"""
    executor.submit(api_cases_test)
    return jsonify(
        {
            "status": 200,
            'msg': 'Two jobs was launched in background!'
        }
        )


# @bp.route('/api_jobs', methods=['GET'])
# def api_job():
#     executor.submit(api_test)
#     return jsonify(
#         {
#             "status": 200,
#             'msg': 'Two jobs was launched in background!'
#         }
#         )
