"""
This module contains the VendorInfo class, which stores reference info in the form a few python dictionary's.
This info used to determine which division the vendor is in, who its POST contact is, and what their risk tier is.

It my last few days at vulcan I changed how this work. previously the other classes would read from the below dictionaries,
however i changed this to instead save the dictionaries to a pkl file, and the other classes instead read from that. The reason for this
was because a pkl file can be updated at runtime, so the user can change the contact name or division name without needing to access the code.
"""


class VendorInfo:

    def __init__(self):

        # dict containing all states as the Keys, and a tuple as the Values. The tuple identifies
        # the states' abbreviation, company division, and POST contact. Some states are unused
        # currently.
        self.post_info = {
                          'Alabama': ['AL', 'Southern Gulf Coast', 'Renee Snipes'],
                          'Alaska': ['AK', 'West', 'Renee Snipes'],
                          'Arizona': ['AZ', 'Mountain West', 'Renee Snipes'],
                          'Arkansas': ['AR', 'Southern Gulf Coast', 'Renee Snipes'],
                          'California': ['CA', 'West', 'Renee Snipes'],
                          'Colorado': ['CO', 'Mountain West', 'Renee Snipes'],
                          'Connecticut': ['CT', 'Mideast', 'Cindy Keller'],
                          'Delaware': ['DE', 'Mideast', 'Cindy Keller'],
                          'District of Columbia': ['DC', 'Mideast', 'Cindy Keller'],
                          'Florida': ['FL', 'Southeast', 'Cindy Keller'],
                          'Georgia': ['GA', 'Southeast', 'Cindy Keller'],
                          'Hawaii': ['HI', 'West', 'Renee Snipes'],
                          'Idaho': ['ID', 'West', 'Renee Snipes'],
                          'Illinois': ['IL', 'Central', 'Renee Snipes'],
                          'Indiana': ['ID', ' Central', 'Renee Snipes'],
                          'Iowa': ['IA', 'Central', 'Renee Snipes'],
                          'Kansas': ['KS', 'Mountain West', 'Renee Snipes'],
                          'Kentucky': ['KT', 'Southern Gulf Coast', 'Renee Snipes'],
                          'Louisiana': ['LA', 'Southern Gulf Coast', 'Renee Snipes'],
                          'Maine': ['ME', ' Mideast', 'Cindy Keller'],
                          'Maryland': ['MD', 'Mideast', 'Cindy Keller'],
                          'Massachusetts': ['MA', 'Mideast', 'Cindy Keller'],
                          'Michigan': ['MI', 'Central', 'Renee Snipes'],
                          'Minnesota': ['MN', 'Central', 'Renee Snipes'],
                          'Mississippi': ['MS', 'Southern Gulf Coast', 'Renee Snipes'],
                          'Missouri': ['MS', 'Central', 'Renee Snipes'],
                          'Montana': ['MT', 'Mountain West', 'Renee Snipes'],
                          'Nebraska': ['NE', 'Mountain West', 'Renee Snipes'],
                          'Nevada': ['NV', 'West', 'Renee Snipes'],
                          'New Hampshire': ['NH', 'Mideast', 'Cindy Keller'],
                          'New Jersey': ["NJ", 'Mideast', 'Cindy Keller'],
                          'New Mexico': ['NM', 'Mountain West', 'Renee Snipes'],
                          'New York': ['NY', 'Mideast', 'Cindy Keller'],
                          'North Carolina': ['NC', 'Mideast', 'Cindy Keller'],
                          'North Dakota': ['ND', 'Mountain West', 'Renee Snipes'],
                          'Ohio': ['OH', 'Central', 'Renee Snipes'],
                          'Oklahoma': ['OK', 'Mountain West', 'Cindy Keller'],
                          'Oregon': ['OR', 'West', 'Renee Snipes'],
                          'Pennsylvania': ['PA', 'Mideast', 'Cindy Keller'],
                          'Rhode Island': ['RI', 'Mideast', 'Cindy keller'],
                          'South Carolina': ['SC', 'Southeast', 'Cindy Keller'],
                          'South Dakota': ['SD', 'Mountain West', 'Renee Snipes'],
                          'Tennessee': ['TN', 'Southern Gulf Coast', 'Renee Snipes'],
                          'Texas': ['TX', 'Southwest', 'Cindy Keller'],
                          'Utah': ['UT', 'Mountain West', 'Renee Snipes'],
                          'Vermont': ['VT', 'Central', 'Renee Snipes'],
                          'Virginia': ['VA', 'Mideast', 'Cindy Keller'],
                          'Washington': ['WA', 'West', 'Renee Snipes'],
                          'West Virginia': ['WV', 'Mideast', 'Cindy Keller'],
                          'Wisconsin': ['WI', 'Central', 'Renee Snipes'],
                          'Wyoming': ['WY', 'Mountain West', 'Renee Snipes'],
                          'U.S. Virgin Islands': ['VI', 'Southern', 'Cindy Keller'],
                         }

        # Dict containing all vendor service types as the Keys, and the associated risk category as the Values.
        # int 1 is Tier 1, int 2 is Tier 2, int 3 is Tier 3, and int 4 is Marine
        # Note that this is not a full list, as there are some service types that exist but are very rarly seen,
        # and have not come up since I began using this.
        self.service_type_info = {
                                  'Building Construction/Repair': 1,
                                  'Cleaning and Janitorial': 3,
                                  'Contract Crushing': 1,
                                  'Contract Drilling': 1,
                                  'Cranes With Operator': 1,
                                  'Electrical': 1,
                                  'Engineering': 2,
                                  'Environmental': 1,
                                  'Equipment Rental': 1,
                                  'Excavation': 2,
                                  'Fixed Eqt On Site Repair': 1,
                                  'Fire Extinguisher Recharge': 2,
                                  'Fuel': 1,
                                  'HVAC Repair': 2,
                                  'Landscaping': 2,
                                  'Mapping and Surveying': 2,
                                  'Marine - Not Using a Vessel': 1,
                                  'Marine - Using a Vessel': 4,
                                  'Mobile Eqt On Site Repair': 1,
                                  'Other Facilities Services On Site': 2,
                                  'Other Production Services On Site': 1,
                                  'Parts, Products or Equipment Only': 3,
                                  'Pest Control': 2,
                                  'Plumbing': 2,
                                  'Professional Services On Site': 2,
                                  'Professional Services Not On Site': 3,
                                  'Rail Eqt Install/Repair': 1,
                                  'Scale Repair': 1,
                                  'Security - Company': 1,
                                  'Staffing - Office': 2,
                                  'Stripping and Site Prep': 1,
                                  'Training': 2,
                                  'Waste Removal': 2,
                                  'Welding': 1
                                 }
