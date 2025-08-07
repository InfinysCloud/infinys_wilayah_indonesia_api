# -*- coding: utf-8 -*-
from odoo import models, fields


class WilayahProvinsi(models.Model):
    _name = "wilayah.provinsi"
    _description = "Provinsi di Indonesia"

    name = fields.Char(string="Nama Provinsi")
    code = fields.Char(string="Kode Provinsi", index=True)
    kota_ids = fields.One2many("wilayah.kota", "provinsi_id", string="Daftar Kota")


class WilayahKota(models.Model):
    _name = "wilayah.kota"
    _description = "Kota di Indonesia"

    name = fields.Char(string="Nama Kota")
    code = fields.Char(string="Kode Kota", index=True)
    provinsi_id = fields.Many2one("wilayah.provinsi", string="Provinsi")
    kecamatan_ids = fields.One2many(
        "wilayah.kecamatan", "kota_id", string="Daftar Kecamatan"
    )


class WilayahKecamatan(models.Model):
    _name = "wilayah.kecamatan"
    _description = "Kecamatan di Indonesia"

    name = fields.Char(string="Nama Kecamatan")
    code = fields.Char(string="Kode Kecamatan", index=True)
    kota_id = fields.Many2one("wilayah.kota", string="Kota")
    kelurahan_ids = fields.One2many(
        "wilayah.kelurahan", "kecamatan_id", string="Daftar Kelurahan"
    )


class WilayahKelurahan(models.Model):
    _name = "wilayah.kelurahan"
    _description = "Kelurahan di Indonesia"

    name = fields.Char(string="Nama Kelurahan")
    code = fields.Char(string="Kode Kelurahan", index=True)
    kecamatan_id = fields.Many2one("wilayah.kecamatan", string="Kecamatan")
    postal_code = fields.Char(string="Kode Pos")
