from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models import User


class ClientForm(Form):
    account = StringField(validators=[
                DataRequired(message="账号不允许为空"),
                Length(min=5, max=32)
            ])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        # 自定义 type 的验证器函数
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise ValidationError('Invalid client type')

        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
                Email(message="无效的邮箱")
            ])
    secret = StringField(validators=[
                DataRequired(),
                Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
            ])
    nickname = StringField(validators=[
                DataRequired(),
                Length(min=2, max=22)
            ])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError("邮箱已存在，请更换另外的邮箱")
