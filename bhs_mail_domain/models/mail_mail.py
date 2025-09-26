from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    sever_email_replace = fields.Char(string="Set Email From", help='Set default one email from to send mail from server', readonly=False)
    email_domains = fields.Char(string="Domain Email", help='If email domain is set, emails have domain similar to email domain are keep stable', readonly=False)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        sever_email_replace = self.env['ir.config_parameter'].sudo().get_param('sever_email_replace') or False
        email_domains = self.env['ir.config_parameter'].sudo().get_param('email_domains') or False
        res.update({
            'sever_email_replace': sever_email_replace,
            'email_domains': email_domains,
        })

        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("sever_email_replace", self.sever_email_replace)
        self.env['ir.config_parameter'].sudo().set_param("email_domains", self.email_domains)

class MailMail(models.Model):
    _inherit = 'mail.mail'

    def send(self, auto_commit=False, raise_exception=False, post_send_callback=None):
        sever_email_replace = self.env['ir.config_parameter'].sudo().get_param('sever_email_replace')
        email_domains = self.env['ir.config_parameter'].sudo().get_param('email_domains')
        for rec in self:
            if rec.email_from and email_domains:
                if ',' in email_domains:
                    email_domain_lst = email_domains.split(',')
                else:
                    email_domain_lst = email_domains.split()
                # email_domain_from = rec.email_from.split('@')[1]
                domain_is_in_email = any([domain.strip() in rec.email_from for domain in email_domain_lst])
                if not domain_is_in_email:
                    if not rec.reply_to:
                        rec.reply_to = rec.email_from
                    rec.email_from = sever_email_replace
        return super(MailMail, self).send(auto_commit, raise_exception, post_send_callback)