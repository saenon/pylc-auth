import logging

def get_logger():
    """
    Get logger with default settings.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    logging.Logger
        Logger with default settings.
    """
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    file_handler = logging.FileHandler("./authentication.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
