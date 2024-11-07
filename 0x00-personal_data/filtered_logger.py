#!/usr/bin/env python3
""" Module filtered_logger.py """
from typing import List
import re


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
