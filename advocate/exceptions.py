class AdvocateException(Exception):
    pass


class UnacceptableAddressException(AdvocateException):
    pass


class NameserverException(AdvocateException):
    pass
