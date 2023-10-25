class ClientForServerListen:
    _instance = None
    @staticmethod
    def instance():
        if not ClientForServerListen._instance:
            ClientForServerListen._instance = ClientForServerListen()
        return ClientForServerListen._instance