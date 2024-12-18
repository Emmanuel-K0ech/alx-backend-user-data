#!/usr/bin/env python3
"""
Basic Authentication class
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication Inheriting from Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        auth_length = len(authorization_header)
        result = authorization_header[6:auth_length]
        return result

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ Returns the decoded value of Base64 string """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            base64.b64decode(base64_authorization_header, validate=True)
        except Exception:
            return None
        result = base64.b64decode(base64_authorization_header)
        utf_result = result.decode('utf-8')
        return utf_result

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value
        """
        delim = ":"
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if delim not in decoded_base64_authorization_header:
            return (None, None)

        result = decoded_base64_authorization_header.split(":", 1)
        # converting via unpacking
        email, password = result
        return (email, password)
