class creds_model(object):
    BearerToken = ''
    UserId = ''
    OtpToken = ''
    Email = ''
    Password = ''

    def __init__(self, BearerToken='', UserId='', OtpToken='', Email='', Password=''):
        self.BearerToken = BearerToken
        self.UserId = UserId
        self.OtpToken = OtpToken
        self.Email = Email
        self.Password = Password