from .Base import Base


class Email(Base):
    """
    发送邮件告警相关
    """
    def __init__(self):
        self.username = 'admin'
        self.pwd = 'admin'

    def send(self, msg):
        pass