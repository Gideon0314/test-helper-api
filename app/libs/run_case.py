# -*- coding: UTF-8 -*-
import os
import subprocess
from datetime import datetime
from time import sleep
from app.libs.zip_file import zip_compress


def api_case_test(case_name):
    """ 测试 """

    project = 'httptest'
    hrp = 'httprunner'

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    allure_result, allure_report = f"result_{now}", f"report_{now}"

    project_path = os.path.abspath(os.path.dirname(os.getcwd()))
    case_path = project_path + f'\\{hrp}\\{project}\\testcases\\{case_name}'
    reports_path = project_path + f'\\{hrp}\\{project}\\reports'

    cmd = [
        f"hrun {case_path} --alluredir={allure_result}",
        f"allure generate {allure_result} -o {allure_report}",
    ]

    for line in cmd:
        ret = subprocess.run(line, shell=True, cwd=reports_path, timeout=60)
        if ret.returncode == 0:
            sleep(10)
            print("success:", ret)
        else:
            print('ERROR')

    zip_compress(f'{reports_path}\\{allure_report}', f'{reports_path}\\{allure_report}.zip')

    print('success')


def api_cases_test():
    """ 测试 """

    project = 'httptest'
    hrp = 'httprunner'

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    allure_result, allure_report = f"result_{now}", f"report_{now}"

    project_path = os.path.abspath(os.path.dirname(os.getcwd()))
    cases_path = project_path + f'\\{hrp}\\{project}\\testcases'
    reports_path = project_path + f'\\{hrp}\\{project}\\reports'

    cmd = [
        # f"hrun {cases_path} --html=reports\pytest_report_{now}.html --self-contained-html",
        f"hrun {cases_path} --html={now}.html --self-contained-html --alluredir={allure_result}",
        f"allure generate {allure_result} -o {allure_report}",
    ]

    for line in cmd:
        ret = subprocess.run(line, shell=True, cwd=reports_path, timeout=60)
        if ret.returncode == 0:
            sleep(10)
            print("success:", ret)
        else:
            print('ERROR')

    zip_compress(f'{reports_path}\\{allure_report}', f'{reports_path}\\{allure_report}.zip')

    print('success')


def web_test():
    """ 测试 """
    hrp = 'web_test'
    # project = 'httptest'
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    allure_result, allure_report = f"result_{now}", f"report_{now}"
    project_path = os.path.abspath(os.path.dirname(os.getcwd()))

    cmd = [
        f'pytest --reruns 2 --html={now}.html --self-contained-html --alluredir=reports\\{allure_result} --clean-alluredir',
        f'allure generate reports\\{allure_result} -c -o reports\\{allure_report}',
        # r'allure open allure-report'
    ]
    for line in cmd:
        ret = subprocess.run(line, shell=True, timeout=20, cwd=f"{project_path}\web_test")
        sleep(10)
        if ret.returncode == 0:
            print("success:", ret)
            '''记录运行结果'''
        else:
            print('error')
    print('success')
