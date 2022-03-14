from hiworker.user_data import UserData


class OqcUser(UserData):
    """
    不良品列表
    """
    def __init__(self, table):
        super(OqcUser, self).__init__(table)
