# -*- coding: utf-8 -*-
import json
import hmac
from functools import wraps
from odoo.http import request


def api_key_required(f):

    @wraps(f)
    def decorated(self, *args, **kwargs):
        api_key = request.httprequest.headers.get("X-API-Key", "")
        valid_key = (
            request.env["ir.config_parameter"].sudo().get_param("wilayah.api.key", "")
        )

        if not hmac.compare_digest(api_key, valid_key):
            error_response = {
                "error": "Unauthorized",
                "message": "Invalid or missing API Key. Please provide a valid key in the X-API-Key header.",
            }
            return request.make_response(
                json.dumps(error_response),
                headers={"Content-Type": "application/json"},
                status=401,
            )

        return f(self, *args, **kwargs)

    return decorated
