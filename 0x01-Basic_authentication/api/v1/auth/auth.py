#!/usr/bin/env python3
"""
auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns True if path not in excluded_paths[] """
        if path is None or excluded_paths is None:
            return True
        # Deals with inconsistent paths
        if not path.endswith('/'):
            path += '/'
        # Final comparison
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
