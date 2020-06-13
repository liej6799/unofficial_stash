class login_model(object):
    email = ""
    password = ""

    def __init__(self, email, password):
        self.email = email
        self.password = password


class login_2fa_send_model(object):
    email = ""
    token = ""

    def __init__(self, email, token):
        self.email = email
        self.token = token


class validate_2fa_model(object):
    token = ""
    secret = ""

    def __init__(self, token, secret):
        self.token = token
        self.secret = secret
