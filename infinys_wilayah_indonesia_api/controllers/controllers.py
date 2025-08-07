# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from .api_key_helper import api_key_required


class WilayahAPIController(http.Controller):

    def _json_response(self, data, error=None, status=200):
        if error:
            return request.make_response(
                json.dumps({"error": error}),
                headers={"Content-Type": "application/json"},
                status=status,
            )
        return request.make_response(
            json.dumps(data, indent=4), headers={"Content-Type": "application/json"}
        )

    @http.route(
        "/api/provinsi",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_provinsi_all(self, name=None, **kw):
        try:
            domain = []
            if name:
                domain.append(("name", "ilike", name))
            provinsi_records = request.env["wilayah.provinsi"].search(domain)
            data = [{"code": p.code, "name": p.name} for p in provinsi_records]
            return self._json_response(data)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/provinsi/<string:kode_provinsi>",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_provinsi_by_code(self, kode_provinsi, **kw):
        try:
            provinsi = request.env["wilayah.provinsi"].search(
                [("code", "=", kode_provinsi)], limit=1
            )
            if not provinsi:
                return self._json_response(
                    None, error="Provinsi tidak ditemukan.", status=404
                )
            return self._json_response({"code": provinsi.code, "name": provinsi.name})
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kota", type="http", auth="public", methods=["GET"], csrf=False, cors="*"
    )
    @api_key_required
    def get_kota_all(self, kode_provinsi=None, name=None, **kw):
        try:
            domain = []
            if kode_provinsi:
                domain.append(("provinsi_id.code", "=", kode_provinsi))
            if name:
                domain.append(("name", "ilike", name))

            kota_records = request.env["wilayah.kota"].search(domain)
            data = [
                {"code": k.code, "name": k.name, "province_code": k.provinsi_id.code}
                for k in kota_records
            ]
            return self._json_response(data)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kota/<string:kode_kota>",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_kota_by_code(self, kode_kota, **kw):
        try:
            kota = request.env["wilayah.kota"].search(
                [("code", "=", kode_kota)], limit=1
            )
            if not kota:
                return self._json_response(
                    None, error="Kota tidak ditemukan.", status=404
                )

            response = {
                "code": kota.code,
                "name": kota.name,
                "province": {
                    "code": kota.provinsi_id.code,
                    "name": kota.provinsi_id.name,
                },
            }
            return self._json_response(response)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kecamatan",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_kecamatan_all(self, kode_kota=None, name=None, **kw):
        try:
            domain = []
            if kode_kota:
                domain.append(("kota_id.code", "=", kode_kota))
            if name:
                domain.append(("name", "ilike", name))

            kecamatan_records = request.env["wilayah.kecamatan"].search(domain)
            data = [
                {"code": kec.code, "name": kec.name, "city_code": kec.kota_id.code}
                for kec in kecamatan_records
            ]
            return self._json_response(data)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kecamatan/<string:kode_kecamatan>",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_kecamatan_by_code(self, kode_kecamatan, **kw):
        try:
            kecamatan = request.env["wilayah.kecamatan"].search(
                [("code", "=", kode_kecamatan)], limit=1
            )
            if not kecamatan:
                return self._json_response(
                    None, error="Kecamatan tidak ditemukan.", status=404
                )

            response = {
                "code": kecamatan.code,
                "name": kecamatan.name,
                "city": {
                    "code": kecamatan.kota_id.code,
                    "name": kecamatan.kota_id.name,
                },
                "province": {
                    "code": kecamatan.kota_id.provinsi_id.code,
                    "name": kecamatan.kota_id.provinsi_id.name,
                },
            }
            return self._json_response(response)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kelurahan",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_kelurahan_all(self, kode_kecamatan=None, name=None, **kw):
        try:
            domain = []
            if kode_kecamatan:
                domain.append(("kecamatan_id.code", "=", kode_kecamatan))
            if name:
                domain.append(("name", "ilike", name))

            kelurahan_records = request.env["wilayah.kelurahan"].search(domain)
            data = [
                {
                    "code": kel.code,
                    "name": kel.name,
                    "postal_code": kel.postal_code,
                    "district_code": kel.kecamatan_id.code,
                }
                for kel in kelurahan_records
            ]
            return self._json_response(data)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kelurahan/<string:kode_kelurahan>",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_kelurahan_by_code(self, kode_kelurahan, **kw):
        try:
            kelurahan = request.env["wilayah.kelurahan"].search(
                [("code", "=", kode_kelurahan)], limit=1
            )
            if not kelurahan:
                return self._json_response(
                    None, error="Kelurahan tidak ditemukan.", status=404
                )

            response = {
                "code": kelurahan.code,
                "name": kelurahan.name,
                "postal_code": kelurahan.postal_code,
                "sub_district": {
                    "code": kelurahan.kecamatan_id.code,
                    "name": kelurahan.kecamatan_id.name,
                },
                "city": {
                    "code": kelurahan.kecamatan_id.kota_id.code,
                    "name": kelurahan.kecamatan_id.kota_id.name,
                },
                "province": {
                    "code": kelurahan.kecamatan_id.kota_id.provinsi_id.code,
                    "name": kelurahan.kecamatan_id.kota_id.provinsi_id.name,
                },
            }
            return self._json_response(response)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/search", type="http", auth="public", methods=["GET"], csrf=False, cors="*"
    )
    @api_key_required
    def search_all(self, q=None, **kw):
        if not q or len(q) < 3:
            return self._json_response(
                None,
                error="Query parameter 'q' is required and must be at least 3 characters long.",
                status=400,
            )

        try:
            domain = [("name", "ilike", q)]
            results = {
                "provinsi": [
                    {"code": p.code, "name": p.name}
                    for p in request.env["wilayah.provinsi"].search(domain)
                ],
                "kota": [
                    {
                        "code": k.code,
                        "name": k.name,
                        "province_code": k.provinsi_id.code,
                    }
                    for k in request.env["wilayah.kota"].search(domain)
                ],
                "kecamatan": [
                    {"code": kec.code, "name": kec.name, "city_code": kec.kota_id.code}
                    for kec in request.env["wilayah.kecamatan"].search(domain)
                ],
                "kelurahan": [
                    {
                        "code": kel.code,
                        "name": kel.name,
                        "postal_code": kel.postal_code,
                        "district_code": kel.kecamatan_id.code,
                    }
                    for kel in request.env["wilayah.kelurahan"].search(domain)
                ],
            }
            return self._json_response(results)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)

    @http.route(
        "/api/kodepos/<string:kode_pos>",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
        cors="*",
    )
    @api_key_required
    def get_by_postal_code(self, kode_pos, **kw):
        try:
            kelurahan_records = request.env["wilayah.kelurahan"].search(
                [("postal_code", "=", kode_pos)]
            )
            if not kelurahan_records:
                return self._json_response(
                    None,
                    error=f"No area found with postal code '{kode_pos}'.",
                    status=404,
                )

            data = [
                {
                    "code": kel.code,
                    "name": kel.name,
                    "postal_code": kel.postal_code,
                    "kecamatan": {
                        "code": kel.kecamatan_id.code,
                        "name": kel.kecamatan_id.name,
                    },
                    "kota": {
                        "code": kel.kecamatan_id.kota_id.code,
                        "name": kel.kecamatan_id.kota_id.name,
                    },
                    "provinsi": {
                        "code": kel.kecamatan_id.kota_id.provinsi_id.code,
                        "name": kel.kecamatan_id.kota_id.provinsi_id.name,
                    },
                }
                for kel in kelurahan_records
            ]
            return self._json_response(data)
        except Exception as e:
            return self._json_response(None, error=str(e), status=500)
