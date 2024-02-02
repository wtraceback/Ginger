from flask import request, jsonify

from app.libs.redprint import Redprint
from app.libs.enums import ClientTypeEnum
from app.validators.forms import ClientForm, UserEmailForm
from app.models import User


api = Redprint('client')


@api.route('/register', methods=['POST'])
def register():
    data =request.json
    form = ClientForm(data=data)
    # TODO account 的位数不够，然后验证不通过该如何处理？
    # TODO 如果验证不通过，raise 了报错后，如何处理？
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }
        func = promise.get(form.type.data, None)
        if func:
            func()
        else:
            print("未定义指定类型的处理函数")
    else:
        errors = form.errors
        print(f"ClientForm errors = {errors}")

    return "register"


def __register_user_by_email():
    print("__register_user_by_email")
    form = UserEmailForm(data=request.json)
    # TODO 如果验证的 account 是已存在的邮箱，报错不准确

    if form.validate():
        User.register_by_email(
                form.account.data,
                form.secret.data,
                form.nickname.data
            )
    else:
        errors = form.errors
        print(f"UserEmailForm errors = {errors}")
