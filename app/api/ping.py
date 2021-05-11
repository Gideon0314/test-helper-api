from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify({
            "data": {
                'a': 200000,
                'b': 200000,
                'c': 200000,
                'd': 200000,
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
                    "2022-02",
                    "2022-03",
                    "2022-04",
                    "2022-05",
                    "2022-06",
                    "2022-07"
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
                "nameAndValueList": [{
                    "name": "Java",
                    "value": 10000
                },
                    {
                        "name": "人工智能",
                        "value": 10000
                    },
                    {
                        "name": "前端",
                        "value": 10000
                    },
                    {
                        "name": "区块链",
                        "value": 10000
                    },
                    {
                        "name": "大数据",
                        "value": 10000
                    },
                    {
                        "name": "游戏",
                        "value": 10000
                    },
                    {
                        "name": "移动端",
                        "value": 10000
                    }
                    ],
                    "nameList": [
                        "Java",
                        "人工智能",
                        "前端",
                        "区块链",
                        "大数据",
                        "游戏",
                        "移动端"
                    ]
                }
            }
        )
