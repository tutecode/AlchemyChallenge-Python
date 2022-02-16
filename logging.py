# importing module
import logging

def logger():
    # Create and configure logger
    logging.basicConfig(filename="logs.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to INFO
    logger.setLevel(logging.INFO)

    return logger

# Test messages
#logger.debug("Harmless debug Message")
#logger.info("Just an information")
#logger.warning("Its a Warning")
#logger.error("Did you try to divide by zero")
#logger.critical("Internet is down")