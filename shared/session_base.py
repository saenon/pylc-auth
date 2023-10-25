class SessionBase:
    INVALID_SESSION_HANDLE = 0

    SESSION = 0
    CONNECT_SESSION = 1
    TIMER_SESSION = 2
    LISTEN_SESSION = 3
    EVENT_SESSION = 4
    EXIT_SESSION = 5

    def __init__(self, io_service, session_type):
        self.type_ = session_type
        self.handle_ = self.INVALID_SESSION_HANDLE
        self.user_data_ = None
        self.error_message_ = ""
        self.io_service_ = io_service
        self.close_error_ = False

    def set_type(self, session_type):
        self.type_ = session_type

    def get_type(self):
        return self.type_

    def set_handle(self, session_handle):
        self.handle_ = session_handle

    def get_handle(self):
        return self.handle_

    def set_user_data(self, data):
        self.user_data_ = data

    def get_user_data(self):
        return self.user_data_

    def set_error_message(self, message):
        self.error_message_ = message

    def get_error_message(self):
        return self.error_message_

    def is_session(self):
        return self.type_ == self.SESSION

    def is_listen_session(self):
        return self.type_ == self.LISTEN_SESSION

    def is_timer_session(self):
        return self.type_ == self.TIMER_SESSION

    def is_connect_session(self):
        return self.type_ == self.CONNECT_SESSION

    def is_event_session(self):
        return self.type_ == self.EVENT_SESSION

    def is_valid(self):
        return self.handle_ != self.INVALID_SESSION_HANDLE

    def is_close_error(self):
        return self.close_error_
