# -*- coding: UTF-8 -*-
import os
import subprocess
from time import sleep
from datetime import datetime
from flask import render_template, jsonify
from app.libs.zip_file import zip_compress
from . import bp


@bp.route('/api_test', methods=['GET'])
def api_test():
    """ 测试 """
    project = 'httptest'
    hrp = 'httprunner'

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    allure_result, allure_report = f"result_{now}", f"report_{now}"

    project_path = os.path.abspath(os.path.dirname(os.getcwd()))
    cases_path = project_path + f'\\{hrp}\\{project}\\testcases'
    reports_path = project_path + f'\\{hrp}\\{project}\\reports'

    cmd = [
        # f"hrun {cases_path} --alluredir={reports_path}\\{allure_result}",
        f"hrun {cases_path} --alluredir={allure_result}",
        # f"allure serve {allure_result}",
        f"allure generate {allure_result} -o {allure_report}",
        # f"allure generate {reports_path}\\{allure_result}\ -o {reports_path}\\{allure_report}",
    ]

    for line in cmd:
        ret = subprocess.run(line, shell=True, cwd=reports_path, timeout=60)
        # if subp.returncode == 0:
        # subp.wait(20)
        if ret.returncode == 0:
            sleep(10)
            print("success:", ret)
        else:
            return jsonify(
                {
                    "status": 453,
                }
            )
    zip_compress(f'{reports_path}\\{allure_report}', f'{reports_path}\\{allure_report}.zip')
    return jsonify(
        {
            "status": 200,
        }
        )


@bp.route('/web_test', methods=['GET'])
def web_test():
    """ 测试 """

    hrp = 'web_test'
    # project = 'httptest'

    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    allure_result = f"allure_result_{now}"
    allure_report = f"allure_report_{now}"

    project_path = os.path.abspath(os.path.dirname(os.getcwd()))
    cases_path = project_path + f'\\{hrp}'
    reports_path = project_path + f'\\{hrp}\\report'

    cmd = [
        f'cd C:\Test_Helper\web_test',
        'run_test.bat',
        # f'pytest --rootdir={cases_path} --reruns 2 --alluredir={reports_path}\\{allure_result}',
        # f"allure generate {reports_path}/{allure_result} -c -o {reports_path}/{allure_report}",
    ]

    for line in cmd:
        ret = subprocess.run(line, shell=True, timeout=20, cwd="C:\Test_Helper\web_test")
        # if subp.returncode == 0:
        # subp.wait(20)
        sleep(10)
        if ret.returncode == 0:
            print("success:", ret)
        else:
            return jsonify(
                {
                    "status": 453,
                }
            )

    return jsonify(
        {
            "status": 200,
        }
        )

