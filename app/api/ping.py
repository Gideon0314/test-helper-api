from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify({
            "data": {
                'a': 5,
                'b': 223,
                'c': 23,
                'd': 23,
            },
            "status": 200
        })

@bp.route('/ping/bar', methods=['GET'])
def ping1():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify(
        {
            "status": 200,
            "message": "成功",
            "data": {
                "yearMonthList": [
                    "2022-05-12",
                    "2022-05-13",
                    "2022-05-14",
                    "2022-05-15",
                    "2022-05-16",
                ],
                "aritcleTotalList": [
                    {'data': [1, 2, 3, 4, 5, 5, 6], 'name': '全球赢'},
                    {'data': [1, 2, 3, 4, 5, 5, 6], 'name': 'Ework'},
                    {'data': [1, 2, 3, 4, 5, 5, 6], 'name': 'SkyCloud'},
                    {'data': [1, 2, 3, 4, 5, 5, 6], 'name': 'SkyTree'},
                    {'data': [1, 2, 3, 4, 5, 5, 6], 'name': '智能投放'}
                ]
                }
            }
        )

@bp.route('/ping/pie', methods=['GET'])
def ping2():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify(
        {
            "status": 200,
            "message": "成功",
            "data": {
                "nameAndValueList": [
                    {
                        "name": "全球赢",
                        "value": 32
                    },
                    {
                        "name": "Ework",
                        "value": 13
                    },
                    {
                        "name": "SkyCloud",
                        "value": 4
                    },
                    {
                        "name": "SkyTree",
                        "value": 3
                    },
                    {
                        "name": "智能投放",
                        "value": 32
                    },
                    ],
                    "nameList": [
                        "全球赢",
                        "Ework",
                        "SkyCloud",
                        "SkyTree",
                        "智能投放",
                    ]
                }
            }
        )


