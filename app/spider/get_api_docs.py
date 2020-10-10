# -*- coding: UTF-8 -*-
from datetime import datetime
import requests
from flask import flash
from sqlalchemy import and_
from back_end.app import db
from back_end.app.models.api_docs import ApiDocs
from back_end.app.models.definitions import Definitions
from back_end.app.models.project import Project
import re
import sys

Author = "Gideon"


class ApiDocsHelper:

    def __init__(self, swagger_url, pid):
        sys.setrecursionlimit(1000000)
        self.swagger_url = swagger_url
        self.pid = pid

    def api_docs_url(self):
        url = re.findall(r"(.*)/swagger-ui.html", self.swagger_url)[0] + "/v2/api-docs"
        return url

    def api_docs(self, return_json=True):
        api_docs_url = self.api_docs_url()
        response = requests.get(api_docs_url, {"Connection": "close"}, verify=False)
        if response.status_code != 200:
            return {} if return_json else response.text
        return response.json() if return_json else response.text

    def get_definitions(self):
        # 获取gdefinitions
        data = {}

        definitions = self.api_docs()['definitions']

        for k, v in definitions.items():

            data['title'] = str(k)

            if v.__contains__('properties'):
                data['properties'] = str(v['properties'])
            else:
                data['properties'] = None
                
            if v.__contains__('type'):
                data['type'] = str(v['type'])
            else:
                data['type'] = None

            self.definitions_db_tools(data)

    def definitions_db_tools(self, data):
        exist_data = Definitions.query.filter(Definitions.title == data["title"]).all()
        if exist_data:
            exist_data = exist_data[0]
            if str(data['title']) == str(exist_data.title):
                exist_data.id = exist_data.id
                exist_data.project_id = self.pid
                exist_data.title = str(data['title'])
                exist_data.properties = str(data['properties'])
                exist_data.type = data['type']
                db.session.add(exist_data)
                db.session.commit()
                db.session.close()
        else:
            data = Definitions(
                project_id=self.pid,
                title=str(data['title']),
                properties=str(data['properties']),
                type=str(data['type']),
            )
            db.session.add(data)
            db.session.commit()
            db.session.close()

    def api_info(self):

        api = {}

        api_docs = self.api_docs()

        paths = api_docs['paths']

        version = api_docs['info']['version']

        for path, api_info in paths.items():

            api['path'] = path

            for request_method, info in api_info.items():

                api['request_method'] = request_method

                if info.__contains__('tags'):
                    api['tags'] = info['tags']

                else:
                    api['tags'] = None

                if info.__contains__('summary'):
                    api['summary'] = info['summary']

                else:
                    api['summary'] = None

                if info.__contains__('parameters'):
                    parameters = info['parameters']
                    api['requests_definitions'] = parameters
                    # api['requests_definitions'] = self.re_ref(parameters)

                else:
                    api['requests_definitions'] = None

                if info.__contains__('responses'):
                    responses = info['responses']
                    # api['responses_definitions'] = self.re_ref(responses)
                    api['responses_definitions'] = responses

                else:
                    api['responses_definitions'] = None

                self.db_tools(api)

        self.docs_version_updated(version)
        self.get_definitions()

    def db_tools(self, api):
        # 更新
        exist_data = ApiDocs.query.filter(and_(ApiDocs.path == api["path"], ApiDocs.request_method == api["request_method"])).all()

        if exist_data:

            exist_data = exist_data[0]

            a = str(exist_data.requests_definitions) == str(api["requests_definitions"])
            b = str(exist_data.responses_definitions) == str(api["responses_definitions"])

            if a and b:

                flash(f'该接口未更新: {api["summary"]}  {api["path"]} ')

            else:
                # docs 状态
                state = 1
                exist_data.project_id = str(self.pid)
                exist_data.api_summary = api["summary"]
                exist_data.tags = api["tags"]
                exist_data.path = api["path"]
                exist_data.request_method = api["request_method"]
                exist_data.requests_definitions = str(api["requests_definitions"])
                exist_data.responses_definitions = str(api["responses_definitions"])
                exist_data.updated = datetime.now()
                db.session.add(exist_data)
                self.docs_state_change(state)
                db.session.commit()
                flash(f'{api["summary"]}该接口已更新')
                db.session.close()

        else:
            # docs 状态
            project_data = ApiDocs(
                project_id=str(self.pid),
                api_summary=api["summary"],
                tags=api["tags"],
                path=api["path"],
                request_method=api["request_method"],
                requests_definitions=str(api["requests_definitions"]),
                responses_definitions=str(api["responses_definitions"]),
                created_at=datetime.now()
            )
            flash(f'该接口不存在，新增数据: {api["summary"]}  {api["path"]}')
            db.session.add(project_data)
            db.session.commit()
            flash(f'{api["summary"]}该接口已更新')

    # def re_ref(self, data):
    #     rd = re.sub(r"(, |)'\$ref': '#/.*?'", '', str(data))
    #     rd = re.sub(r"\$", '', str(data))
    #     rd = ast.literal_eval(rd)
    #     return rd

    def docs_state_change(self, state):
        return Project.query.filter_by(id=self.pid).update({"docs_state": state})

    def docs_version_updated(self, version):
        return Project.query.filter_by(id=self.pid).update({"version": version})
