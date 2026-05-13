# -*- coding: utf-8 -*-

from odoo import models


class AccountAssetReportHandler(models.AbstractModel):
    _inherit = "account.asset.report.handler"

    def _custom_options_initializer(self, report, options, previous_options):
        super()._custom_options_initializer(report, options, previous_options=previous_options)

        if any(col.get("expression_label") == "x_studio_asset_code" for col in options["columns"]):
            options["custom_columns_subheaders"][0]["colspan"] = 4

    def _query_lines(self, options, prefix_to_match=None, forced_account_id=None):
        lines = super()._query_lines(
            options,
            prefix_to_match=prefix_to_match,
            forced_account_id=forced_account_id,
        )

        asset_model = self.env["account.asset"]
        if "x_studio_asset_code" not in asset_model._fields:
            return [
                (account_id, asset_id, asset_group_id, {**columns, "x_studio_asset_code": ""})
                for account_id, asset_id, asset_group_id, columns in lines
            ]

        asset_ids = [asset_id for _account_id, asset_id, _asset_group_id, _columns in lines]
        asset_codes = {
            asset.id: asset.x_studio_asset_code or ""
            for asset in asset_model.browse(asset_ids)
        }

        return [
            (
                account_id,
                asset_id,
                asset_group_id,
                {**columns, "x_studio_asset_code": asset_codes.get(asset_id, "")},
            )
            for account_id, asset_id, asset_group_id, columns in lines
        ]
