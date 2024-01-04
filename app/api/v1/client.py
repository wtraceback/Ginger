from flask import request, jsonify

from app.libs.redprint import Redprint
from app.libs.enums import ClientTypeEnum
from app.validators.forms import ClientRegisterForm


api = Redprint('client')


@api.route('/register', methods=['POST'])
def register():
    # data = request.json
    print("====================")
    # print(f"request.form = {request.form}")
    print(f"request.json = {request.json}")
    # form = ClientRegisterForm(data=data)
    # if form.validate():
    #     promise = {
    #         ClientTypeEnum.USER_EMAIL: __register_user_by_email,
    #     }

    return "register"

def __register_user_by_email():
    pass
