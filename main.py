from classes.SessionBase import SessionBase
from classes.ClientForServerListen import ClientForServerListen
from classes.ClientForClientListen import ClientForClientListen
from classes.BNF import BNF

from config.logger import get_logger

def init():

    LISTEN_PORT_FOR_SERVER = 3000
    LISTEN_PORT_FOR_CLIENT = 3001

    if BNF.instance().create_listen("0.0.0.0", LISTEN_PORT_FOR_SERVER, 10, ClientForServerListen.instance()) == SessionBase.INVALID_SESSION_HANDLE:
        get_logger().info(
            {
                "service": "Authentication",
                "event": "create_listen (server)",
                "status": "Failed",
            }
        )
        return False
    
    if BNF.instance().create_listen("0.0.0.0", LISTEN_PORT_FOR_CLIENT, 10, ClientForClientListen.instance()) == SessionBase.INVALID_SESSION_HANDLE:
        get_logger().info(
            {
                "service": "Authentication",
                "event": "create_listen (client)",
                "status": "Failed",
            }
        )
        return False
    
    BNF.instance().start()

if __name__ == "__main__":
    init()