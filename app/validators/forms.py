from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length

from app.libs.enums import ClientTypeEnum


class ClientRegisterForm(Form):
    account = StringField(validators=[DataRequired(), Length(
        min=5, max=32
    )])
    secret = StringField()
    client_type = IntegerField(validators=[DataRequired()])

    def validate_client_type(self, value):
        # 自定义 type 的验证器函数
        try:
            client = ClientTypeEnum(value)
        except ValueError as e:
            raise e
