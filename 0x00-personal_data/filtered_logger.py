#!/usr/bin/env python3
""" Module filtered_logger.py """
from typing import List, Tuple
import logging
import re

logging.basicConfig(filename="record.log", level=logging.INFO)
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated
    Args:
        fields list[str]: representin all fields to obfuscate
        redaction (str): representing by what the field will obfuscate
        message (str): string representing the log line
        separator (str): string representing by which character is
                        seperating all fields in the log line
    Uses regex to replace occurrences of certain field values
    use re.sub to perform the substitutuion with a single regex
    # Text is seperated by ;, hence regex will start from '=' to ';'
    """
    for field in fields:
        pattern = r"({}=)([^{}]+)".format(field, separator)
        message = re.sub(pattern, r"\1" + redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    logging.basicConfig(filename="record.log", level=logging.INFO,
                        format=f"FORMAT")

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ uses filter_datum() to redact fields specified"""
        redacted_msg = filter_datum(self.fields, self.REDACTION,
                                    record.msg, self.SEPARATOR)
        record.msg = redacted_msg
        return super().format(record)


def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    log_formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)
    return logger
