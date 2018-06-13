from .Base import Base


class Msg(Base):
    """
    发送手机信息告警相关
    """
    def __init__(self):
        self.username = 'admin'
        self.pwd = 'admin'

    def send(self, msg):
        pass