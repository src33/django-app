import json
from deep_translator import GoogleTranslator
import langcodes

def trans(filename,lang):
    flpth=[]
    # Open the file in read mode
    with open(filename, 'r',encoding='utf-8') as f:
        # Read all lines and store them in a list
        lines = f.readlines()

    # Strip the newline character from each line and store them in a new list
    my_list = [line.strip() for line in lines]
    #my_list = ['+ (353) 85 199 5043', 'info@taxgoglobal.com', 'HOME', 'SERVICES', 'PRICING', 'NEWS', 'COMPANY', 'SIGN IN', 'REGISTER', '#2022 for Free', 'Accounting Software for Small Business in Ireland', 'We provide all in one solution to Help Your Businesses Innovate and Grow', 'Get Started for Free', 'Our Services', 'Get Started', 'Setup and Manage Account Easily', 'Save upto 2 hours everyday, 40 hrs a month', 'Inventory Management', 'Adding products and services in your inventory made easy, entering and scanning products, easier, faster and much more efficient.', 'Contact Management', 'Do you want to keep track of your customers or suppliers on the GO? Tax GO can facilitate this by allowing you to track every inch of your business no matter where you are in the world.', 'Sale Management', 'Organises your customer invoices, quotGO 24/7 Support?', "Telephone support is available 24 hours a day, seven days a week, Freshchat available 24/7, FAQ's availabe for Important Questions.", '04', 'How will this help my business?', 'Tax GO Global was designed to help small & medium businesses management and service to Create/Send Invoices, Manage Inventory, Pay anywhere, Prepare Reports.', 'PRODUCT', 'Tax Calculator', 'Accounting', 'Retail', 'Consulting', 'Payroll', 'ABOUT', 'Company', 'Sign Up', 'Login', 'Plans', 'REACH US', 'Terms', 'Privacy', 'Policy', 'www.taxgoglobal.com', 'Privacy.', 'Terms and Conditions.']

    # Create a dictionary to store the translations
    translations = {}
    target_language = 'ml'
    # Initialize the Google Translate API client
    # lang=[input("lang : ") for i in range(3)]

    for language in lang: 

        code = langcodes.find(language).language
        for string in my_list:
            if not string:
                my_list.remove(string)
        # print(my_list)
        for string in my_list:
            try:
                # Translate the string
                if '@' not in string and not string.isnumeric() :
                    translation =  GoogleTranslator(source='auto', target=code).translate(string)
                    # decoded_translation = bytes(translation, "utf-8").decode("unicode_escape")
                    # Add the translation to the dictionary
                    string=string.replace(" ", "_")
                    translations[string] = translation
            except Exception as e:
                # Handle any errors here
                print(f"Error translating string {string}: {str(e)}")

        # Save the translations to a JSON file
        path=f'{filename}-{langcodes.Language.get(code).language_name()}.json'
        with open(path, 'w',encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=4)
        flpth.append(path) 
    return flpth       
