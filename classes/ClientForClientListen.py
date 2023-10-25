class ClientForClientListen:
    _instance = None
    @staticmethod
    def instance():
        if not ClientForClientListen._instance:
            ClientForClientListen._instance = ClientForClientListen()
        return ClientForClientListen._instance