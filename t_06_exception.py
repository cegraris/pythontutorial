# try ==================================
import logging

try:
    ...
except ZeroDivisionError as e:
    logging.exception(e)
except ValueError as e:
    logging.exception(e)
else:
    ...
finally:
    ...
