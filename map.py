"""
This module contains the Map class, which itself stores all the HTML XPATH's that are needed for the webdriver to
navigate the Vcommerce site. All XPATH's are stored as the values of a python dictionary contained
within a class member.
"""


class Map:

    def __init__(self):

        # dict containing website element descriptions as the Keys, and their HTML XPATH's as the values.
        self.full_xpath = {
                           'login_pw': '/html/body/div/div/div[2]/div[1]/div[2]/form/div/div[2]/input',

                           'login_button': '/html/body/div/div/div[2]/div[1]/div[2]/form/div/div[3]/div/button',

                           'apps_list': '/html/body/div/main/div/div[2]/div/div/div',

                           'vc_search_bar': '/html/body/div[5]/table/tbody/tr/td/form[1]/div/div/table/tbody/tr/td/div'
                                            '/table/tbody/tr[1]/td[2]/input',

                           'vc_link': '/html/body/div[5]/form[1]/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr'
                                      '/td/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/b/a',

                           'vc_general_button': '/html/body/div[5]/div[2]/div/div/div[1]/div[1]/ul/li[1]/ul/li[3]/a',

                           'vc_summary_button': '/html/body/div[5]/div[2]/div/div/div[1]/div[1]/ul/li[1]/ul/li[2]/a',

                           'vc_general_page_full': '/html/body',

                           'vc_summary_page': '/html/body/div[5]/div[2]/div/div/div[2]/div',

                           'vc_summary_page_full': '/html/body',

                           'vc_service_locator': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table/tbody/tr/td'
                                                 '/table/tbody[7]/tr[1]/td/h2',

                           'vc_link_locator': '/html/body/div[5]/div[2]/div/div/div[1]/form/div/div[1]/div[1]/h2',

                           'vc_single_service': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table/tbody/tr'
                                                '/td/table/tbody[3]/tr[34]/td[2]/div/table/tbody/tr/td[1]/div/div'
                                                '/div/div/div',

                           'vc_single_contact': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]'
                                                '/td/table/tbody/tr[11]/td[2]/button',

                           'vc_multi_contact': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]'
                                               '/td/table/tbody/tr[10]/td[2]/button',

                           'vc_contact_popup': '/html/body/div[14]/div/div[2]/div/div',

                           'legal_and_compliance_link': '/html/body/div[5]/div[2]/div/div/div[1]/div[1]/ul/li[6]/a',

                           'insurance_custom_link': '/html/body/div[5]/div[2]/div/div/div[1]/div[1]/ul/li[6]/ul'
                                                    '/li[2]/a',

                           'cert_download': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table/tbody/tr[7]/td[2]'
                                            '/div/table/tbody/tr/td[1]/div/a/span'
                           }