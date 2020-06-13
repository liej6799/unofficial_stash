class creds_model(object):
    BearerToken = ""
    UserId = ""
    OtpToken = ""

    def __init__(self, BearerToken, UserId, OtpToken):
        self.BearerToken = BearerToken
        self.UserId = UserId
        self.OtpToken = OtpToken
