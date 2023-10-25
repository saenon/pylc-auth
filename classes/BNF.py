from config.logger import get_logger

class BNF:
    _logger = get_logger()
    _instance = None
    _counter = 0
    
    @staticmethod
    def instance():
        if not BNF._instance:
            BNF._instance = BNF()
        return BNF._instance
    
    def create_listen(self, ip_address, port, max_connections, client):
        # TBD
        pass
    
    def start(self):
        # TBD
       BNF._logger.info(
            {
                "service": "Authentication",
                "event": "start",
                "status": "Success",
            }
        )