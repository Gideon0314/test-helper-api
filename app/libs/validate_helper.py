# -*- coding: UTF-8 -*-
from wtforms import ValidationError
from back_end.app.models.project import Project


class Validata_helper:


    def validate_swagger_url(self, field):
        if Project.query.filter_by(swagger_url=field.data).first():
            raise ValidationError('')
