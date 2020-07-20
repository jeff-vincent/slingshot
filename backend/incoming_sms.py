from app import mongo


class HandleIncomingSMS:
    def __init__(self, sms_object):
        self.sms_object = sms_object

    def parse_sms_callback(self):
        pass

    def write_to_db(self):
        pass

    