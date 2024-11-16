#!/usr/bin/env python3
"""
Basic Authentication class
"""
from api.v1.auth.auth import Auth


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
