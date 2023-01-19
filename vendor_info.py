"""
This module contains the VendorInfo class, which stores reference info in the form a few python dictionary's.
This info used to determine which division the vendor is in, who its POST contact is, and what their risk tier is.
"""


class VendorInfo:

    def __init__(self):

        # dict containing all states as the Keys, and a tuple as the Values. The tuple identifies
        # the states' abbreviation, company division, and POST contact. Some states are unused
        # currently.
        self.post_info = {
                          'Alabama': ('AL', 'Southern Gulf Coast', 'Renee Snipes'),
                          'Alaska': 'AK',
                          'Arizona': ('AZ', 'Mountain West', 'Renee Snipes'),
                          'Arkansas': ('AR', 'Southern Gulf Coast', 'Renee Snipes'),
                          'California': ('CA', 'West', 'Renee Snipes'),
                          'Colorado': ('CO', 'Mountain West', 'Renee Snipes'),
                          'Connecticut': 'CT',
                          'Delaware': ('DE', 'Mideast', 'Cindy Keller'),
                          'District of Columbia': 'DC',
                          'Florida': ('FL', 'Southeast', 'Cindy Keller'),
                          'Georgia': ('GA', 'Southeast', 'Cindy Keller'),
                          'Hawaii': 'HI',
                          'Idaho': 'ID',
                          'Illinois': ('IL', 'Central', 'Renee Snipes'),
                          'Indiana': 'ID',
                          'Iowa': ('IA', 'Central', 'Renee Snipes'),
                          'Kansas': ('KS', 'Mountain West', 'Renee Snipes'),
                          'Kentucky': ('KT', 'Southern Gulf Coast', 'Renee Snipes'),
                          'Louisiana': ('LA', 'Southern Gulf Coast', 'Renee Snipes'),
                          'Maine': 'ME',
                          'Maryland': ('MD', 'Mideast', 'Cindy Keller'),
                          'Massachusetts': 'MA',
                          'Michigan': ('MI', 'Central', 'Renee Snipes'),
                          'Minnesota': ('MN', 'Central', 'Renee Snipes'),
                          'Mississippi': ('MS', 'Southern Gulf Coast', 'Renee Snipes'),
                          'Missouri': ('MS', 'Central', 'Renee Snipes'),
                          'Montana': 'MT',
                          'Nebraska': 'NE',
                          'Nevada': ('NV', 'West', 'Renee Snipes'),
                          'New Hampshire': 'NH',
                          'New Jersey': ("NJ", 'Mideast', 'Cindy Keller'),
                          'New Mexico': ('NM', 'Mountain West', 'Renee Snipes'),
                          'New York': 'NY',
                          'North Carolina': ('NC', 'Mideast', 'Cindy Keller'),
                          'North Dakota': 'ND',
                          'Ohio': 'OH',
                          'Oklahoma': ('OK', 'Mountain West', 'Cindy Keller'),
                          'Oregon': 'OR',
                          'Pennsylvania': ('PA', 'Mideast', 'Cindy Keller'),
                          'Rhode Island': 'RI',
                          'South Carolina': ('SC', 'Southeast', 'Cindy Keller'),
                          'South Dakota': 'SD',
                          'Tennessee': ('TN', 'Southern Gulf Coast', 'Renee Snipes'),
                          'Texas': ('TX', 'Southwest', 'Cindy Keller'),
                          'Utah': 'UT',
                          'Vermont': 'VT',
                          'Virginia': ('VA', 'Mideast', 'Cindy Keller'),
                          'Washington': 'WA',
                          'West Virginia': ('WV', 'Mideast', 'Cindy Keller'),
                          'Wisconsin': ('WI', 'Central', 'Renee Snipes'),
                          'Wyoming': 'WY'
                         }

        # Dict containing all vendor service types as the Keys, and the associated risk category as the Values.
        # int 1 is Tier 1, int 2 is Tier 2, int 3 is Tier 3, and int 4 is Marine
        self.service_type_info = {
                                  'Building Construction/Repair': 1,
                                  'Cleaning and Janitorial': 3,
                                  'Contract Crushing': 1,
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
                                  'Welding': 1
                                 }
