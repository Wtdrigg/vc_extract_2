# vc_extract_2

The purpose of this program is to assist in automating the daily task of extracting vendor information from one of our vendor tracking systems.

The program has a GUI with a few entry boxes, which prompt the user for their password and the vendor’s ID number. Once this information is entered the user may then
click the submit button to begin the extraction process. This process uses Selenium to have an automated web browser log in using the provided password, then search for the vendor using the provided ID number.

Once the vendor is found, the page is copied, and all required information is found via algorithm and saved to memory. This extracted data is then saved into an excel spreadsheet created in the users downloads folder.

The algorithm will locate and extract the following from the vendor page:
1. The vendors name,
2. The vendors DBA name (if one exists),
3. The vendors new ID number (if one exists),
4. The vendor’s full address.
5. The vendors contact information which includes the contacts name, email, and phone.
6. The vendors Service Type
7. The vendors risk tier (determined based on the service type).
8. The company division that this vendor falls under.
9. The support contact for that division.

Furthermore, this algorithm will format this information appropriately, as the vendor system often lists information in all caps. It will also download any saved PDF certificates of insurance that may be stored on the vendor page.

Note that for this program to work the user must have the OneLogin chrome extension setup with valid company credentials and must also have a valid login password. The user must also have a copy of chrome’s "User Data" folder saved in the working directory, otherwise they would need to close all browser windows for selenium to work. Finally, the user must have a copy of chromedriver.exe saved to the programs working directory. This .exe file is developed by Google and must match the version of Chrome being used. It may be downloaded for free from selenium's website.
