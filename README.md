# VHG Depreciation Schedule Extension

![Odoo 19](https://img.shields.io/badge/Odoo-19.0-875A7B?style=flat-square)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=flat-square)
![Category](https://img.shields.io/badge/Category-Accounting-4ECDC4?style=flat-square)

Extend the native Depreciation Schedule report with an Asset Code column for Odoo 19.

This addon enhances the original `account_asset` depreciation schedule by introducing a dedicated **Asset Code** report column. It is intentionally small and safe: the original report remains the base, while this module enriches its output when the custom field `x_studio_asset_code` exists on `account.asset`.

## Highlights

- Adds an **Asset Code** column to the native depreciation schedule report.
- Reuses the original `account.asset.report.handler`.
- Gracefully falls back to blank values when `x_studio_asset_code` does not exist.
- Adjusts report subheader colspan so the extra column fits cleanly.
- Avoids cloning the full report definition.

## Technical Notes

- `data/assets_report.xml`
  Declares the new `account.report.column` on the existing depreciation schedule report.
- `models/account_assets_report.py`
  Extends the native report handler to populate `x_studio_asset_code` values line by line.

## Module Layout

```text
tha_vhg_ds_ext/
|-- data/
|-- models/
`-- __manifest__.py
```

## Dependencies

- `account_asset`

## Installation

1. Place the module in your custom addons path.
2. Update the Apps list in Odoo.
3. Install **VHG Depreciation Schedule Extension**.

## License

This module is licensed under `LGPL-3`.
