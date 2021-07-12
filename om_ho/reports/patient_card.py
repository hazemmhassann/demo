from odoo import api, models


class ParticularReport(models.AbstractModel):
    _name = 'report.om_ho.report_patient'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        print("Yest Entered")
        # get the records selected for this rendering of the report
        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list = []
        for app in appointments:
            vals = {
                'notes': app.notes,
                'appdate': app.appointment_date

            }
            appointment_list.append(vals)
        print("appointment", appointments)
        print("appointment_list", appointment_list)


        print("docids", docids)
        print("data", data)

        # return a custom rendering context
        return {
            'docs': docs,
            'data': data,
            'doc_model': 'hospital.patient',
            'docids': docids
        }
