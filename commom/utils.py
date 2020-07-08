# _*_ coding: utf-8 _*_
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Utilities:

    @staticmethod
    def check_username(first_name: str, last_name: str) -> str:
        if first_name is None or first_name == '' or \
                last_name is None or last_name == '':
            return ''
        i = 0
        res = un = first_name.lower()
        while un != '':
            username = None
            try:
                username = User.objects.get(username=un)
            except ObjectDoesNotExist:
                un = ''
            if username is not None:
                un = f'{first_name}_{last_name}' if i == 0 else \
                    f'{first_name}_{str(i).rjust(2, "0")}'
            res = un if un != '' else res
            i += 1
        return res

    @staticmethod
    def get_database_choices(db=None, description_fields: list = None):
        if db is None or description_fields is None:
            return ()
        qs = db.objects.all()
        choices = []
        for data in qs:
            value = [f'{getattr(data, field)} ' for field in description_fields]
            choices.append((data.pk, ''.join(value)))
        return choices

    @staticmethod
    def get_result_status(
            code: int = 200, message: str = '', data: dict = None
    ) -> dict:
        return {
            'status': {
                'sttCode': code,
                'sttMsgs': message
            },
            'data': data,
            'date': datetime.datetime.now(),
            'app': data['app'] if data is not None else None,
        }
