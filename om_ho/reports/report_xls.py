from odoo import models


class PatientCardXLS(models.AbstractModel):
    _name = 'report.om_ho.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('Patient Card')
        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.patient_name, format1)
