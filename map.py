"""
This module contains the Map class, which itself stores all the HTML PATH addresses that are needed for the webdriver to
navigate the Vcommerce site. All PATH's are stored as the values of a python dictionary contained within a class member.
If you ever need to find the HTML path, this can be done by right clicking on an element in the web browser and clicking inspect,
then right clicking the same element on the list and selecting either copy Xpath (for the short version), or copy Full Xpath (for the long
version).

The short version relies on some kind of HTML attribute being the same across all vendor files, so I often use the long version instead.

I had to quickly make several changes to this in my last few days at Vulcan so this is a little bit messier than I would like.
"""


class Map:

    def __init__(self):

        # dict containing website element descriptions as the Keys, and their HTML PATH's as the values.
        self.full_xpath = {
                           'login_pw': '/html/body/div/div/div[2]/div[1]/div[2]/form/div/div[2]/input',

                           'login_button': '/html/body/div/div/div[2]/div[1]/div[2]/form/div/div[3]/div/button',

                           'continue_button': '//*[@id="root"]/div/div[2]/div[1]/div[2]/form/div/div[3]/div/button',

                           'apps_list': '/html/body/div/div/main/div/div[2]/div/div/div',

                           'vc_search_bar': '/html/body/div[5]/table/tbody/tr/td/form[1]/div/div/table/tbody/tr/td/div'
                                            '/table/tbody/tr[1]/td[2]/input',

                           'vc_link': '/html/body/div[5]/form[1]/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr'
                                      '/td/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/b/a',

                           'vc_general_button': '/html/body/div[5]/div[2]/div/div/div[1]/div[1]/ul/li[1]/ul/li[3]/a',

                           'vc_summary_button': '/html/body/div[5]/div[2]/div/div/div[1]/div[1]/ul/li[1]/ul/li[2]/a',

                           'vc_general_page_full': '/html/body',

                           'vc_summary_page': '//*[@id="SupplierSummary_body"]',

                           'vc_summary_page_full': '/html/body',

                           'vc_service_locator': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table/tbody/tr/td/table/tbody[5]/tr[3]/td/h2',

                           'vc_link_locator': '/html/body/div[5]/div[2]/div/div/div[1]/form/div/div[1]/div[1]/h2',

                           'vc_single_service': '//*[@id="CustElement_11297"]/div/div',
                                                                                                                                    
                           'vc_single_contact': '/html/body/div[5]/div/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/button',
                           'vc_single_contact2':'/html/body/div[5]/div/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]/button',
                           'vc_single_contact3':'/html/body/div[5]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/button',
                           'vc_single_contact4':'/html/body/div[5]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]/button',
                           'vc_single_contact5':'/html/body/div[6]/div/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/button',
                           'vc_single_contact6':'/html/body/div[6]/div/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]/button',
                           'vc_single_contact7':'/html/body/div[6]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/button',
                           'vc_single_contact8':'/html/body/div[6]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]/td/table/tbody/tr[11]/td[2]/button',

                           'vc_multi_contact': '/html/body/div[5]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]'
                                               '/td/table/tbody/tr[10]/td[2]/button',
                           'vc_multi_contact2': '/html/body/div[6]/div[2]/div/div/div[2]/div/form/table[2]/tbody/tr[2]'
                                               '/td/table/tbody/tr[10]/td[2]/button',

                           'vc_contact_popup': '/html/body/div[14]/div/div[2]/div/div',
                           'vc_contact_popup2': '/html/body/div[15]/div/div[2]/div/div',

                           'legal_and_compliance_link': '//*[@id="PHX_NAV_LegalAndCompliance"]',

                           'insurance_custom_link': '//*[@id="PhoenixNavLink_PHX_NAV_SupplierProfile_InsuranceAdditionalInfo"]',

                           'cert_download': '/html/body/div[5]/div/div/div/div[2]/div/form/table/tbody/tr[7]/td[2]/div/table/tbody/tr/td[1]/div/a/span',
                           'cert_download2': '/html/body/div[6]/div/div/div/div[2]/div/form/table/tbody/tr[7]/td[2]/div/table/tbody/tr/td[1]/div/a/span',

                           'approve_search_results': '//*[@id="ApprNotifications_body"]/div[5]/table/tbody/tr[2]/td/'
                                                     'div/form/table/tbody/tr[2]/td/table/tbody/tr/td/div[2]/table',

                           'approve_summary_button': '//*[@id="PhoenixNavLink_PHX_NAV_SupplierProfile_'
                                                     'SupplierSummary"]',

                           'approve_summary_page_body': '//*[@id="SupplierSummary_body"]',

                           'approve_first_item': '//*[@id="ApprNotifications_body"]/div[5]/table/tbody/tr[2]/td/div/'
                                                 'form/table/tbody/tr[2]/td/table/tbody/tr/td/div[2]/table/tbody/'
                                                 'tr[1]/td[1]/a',

                           'approve_remove_button': '/html/body/div[5]/table/tbody/tr[2]/td/div/form/table/tbody/'
                                                    'tr[2]/td/table/tbody/tr/td/div[2]/table/tbody/tr[1]/td[3]/input',

                           'approve_login_button': '/html/body/div/div/div[2]/div[1]/div[3]/form/div/div[3]/div/button',

                           'approve_vc_password': '/html/body/div/div/div[2]/div[1]/div[3]/form/div/div[2]/input'
                           }
