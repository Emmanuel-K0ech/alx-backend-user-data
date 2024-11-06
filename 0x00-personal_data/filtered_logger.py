#!/usr/bin/env python3
""" Module filtered_logger.py """
from typing import List
import re


def filter_datum(fields: List[int], redaction: str, message: str,
                 separator: str) -> List[str]:
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
    """
    # Text is seperated by ;, hence regex will start from '=' to ';'
    new_fields: List[str] = []
    for field in fields:
        pattern: str = fr"{re.escape(field)}=.*?(?={re.escape(separator)}|$)"
        new_fields.append(re.sub(pattern, f"{field}={redaction}", message))
    return new_fields
