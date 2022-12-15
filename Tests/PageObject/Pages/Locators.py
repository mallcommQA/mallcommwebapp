__author__ = 'Chidozie Amefule'


class Locator(object):

    # Landing page locator
    logo = "//div[@class='stuff']//img"
    signIn_register = "//div[@class='stuff']//span"
    email = "//div[@class='stuff']//input"
    next_button = "//div[@class='stuff']//button"
    change_language = "//div[@class='LangSwitch']"
    language_list = "//div[@class='pickert']"
    english_us = "//div[@class='LangSwitch']//a[1]"
    flag = "//div[@class='LangSwitch']//img"
    czech = "//div[@class='LangSwitch']//a[2]"
    danish = "//div[@class='LangSwitch']//a[3]"
    dutch = "//div[@class='LangSwitch']//a[4]"
    french = "//div[@class='LangSwitch']//a[5]"
    german = "//div[@class='LangSwitch']//a[6]"
    hungarian = "//div[@class='LangSwitch']//a[7]"
    italian = "//div[@class='LangSwitch']//a[8]"
    polish = "//div[@class='LangSwitch']//a[9]"
    polish_next_button = "//button"
    slovak = "//div[@class='LangSwitch']//a[10]"
    spanish = "//div[@class='LangSwitch']//a[11]"
    swedish = "//div[@class='LangSwitch']//a[12]"
    turkish = "//div[@class='LangSwitch']//a[13]"
    arabic = "//div[@class='LangSwitch']//a[14]"
    english_uk = "//div[@class='LangSwitch']//a[15]"

    # Register flow locator
    register_email = "//div[@class='stuff']//input"
    register_next_button = "//div[@class='stuff']//button"
    sign_in_password_page = "//div[@class='login_register_form']"
    change_email = "//div[@class='stuff']//a"
    register_first_name = "//div[@class='stuff']//input[@id='register_first_name']"
    register_last_name = "//div[@class='stuff']//input[@id='register_last_name']"
    country_code_dropdown = "//div[@class='stuff']//span[@class='dropdown-arrow']"
    country_code_list = "//div[@class='dropdown open']//ul//li"
    uk_country_code = "//li[@class='dropdown-item preferred']//strong[contains(text(),'United Kingdom')]"
    us_country_code = "//li[@class='dropdown-item preferred']//strong[contains(text(),'United States')]"
    france_country_code = "//li[@class='dropdown-item preferred']//strong[contains(text(),'France')]"
    phone_number = "//div[@class='stuff']//input[@name='telephone']"
    register_next_button_2 = "//div[@class='stuff']//button[@class='lr_btn step_button']"
    switch_to_sign_in = "//div[@class='stuff']//button[@class='lr_btn switch_type_button']"
    change_email_2 = "//div[@class='stuff']//p[1]//a"
    change_first_name = "//div[@class='stuff']//p[2]//a"
    change_last_name = "//div[@class='stuff']//p[3]//a"
    password = "//div[@class='stuff']//input[@id='password']"
    confirm_password = "//div[@class='stuff']//input[@id='password_confirm']"
    register_next_button_3 = "//div[@class='stuff']//button[@class='lr_btn step_button']"
    switch_to_sign_in_2 = "//div[@class='stuff']//small"
    change_password = "//div[@class='stuff']//p[4]//a"
    select_centre_dropdown = "//div[@class='centre_picker']//i"
    selected_centre = "//div[@class='menu visible']//div[1]"
    select_store_dropdown = "//div[@class='select_holder']//i"
    selected_store = "//div[@class='menu visible']//div[contains(text(),'Mallcomm Team')]"
    register_next_button_4 = "//button[@class='lr_btn step_button']"
    switch_to_sign_in_3 = "//button[@class='lr_btn switch_type_button']"
    terms_conditions_tick_box = "//div[@class='tacs']//input[@id='checkbox_7']"
    register_button = "//button[@class='lr_btn step_button']"
    switch_to_sign_in_4 = "//button[@class='lr_btn switch_type_button']"
    confirm_registration = "//div[@class='NotVerified']//button[1]"
    already_registered = "//div[@class='stuff']//span"
    first_name_empty_warning = "//div[@class='login_register_form']//div[2]//div[1]"
    last_name_empty_warning = "//div[@class='login_register_form']//div[2]//div[2]"
    resend_verification_email = "//div[@class='NotVerified']//button[2]"

    # Sign In flow locators
    sign_in_email = "//div[@class='stuff']//input"
    sign_in_next_button = "//div[@class='stuff']//button"
    sign_in_password = "//input[@id='password']"
    forgot_password = "//div[@class='main_view']//a[text()='Forgot Password']"
    sign_in_button = "//div[@class='main_view']//button[@class='lr_btn step_button']"
    switch_to_register_button = "//div[@class='main_view']//button[@class='lr_btn switch_type_button']"
    unregistered_email_sign_in = "//div[@class='login_register_form']"
    invalid_password_message = "//div[@class='login_register_form']//div[1]//div"
    locked_account_message = "//div[@class='login_register_form']//div[contains(text(),'Your account is locked')]"

    # Logout Locators
    logout_button = "//div[@id='app']//i[@class='fa fa-sign-out-alt']"

    # Password reset locators
    forgot_password_link = "//a[@class='forgot-psswd']"
    send_password_reset_email_button = "//div[@class='login_register_form']//button"
    confirm_reset_password_email_sent = "//button[@class='lr_btn switch_type_button']//small"

    # User Profile locators
    side_menu = "//div[@class='sidebar_controler']"
    avatar = "//div[@class='user_profile']//img"
    image = "//div[@class='Images']"
    change_avatar = "//div[@class='content']//div[@class='user_image']//img"
    input_image = "//div[@class='content']//input[@class='input-file']"
    image_input_text = "//p[contains(text(),'Drag new image here or click to browse')]"
    remove_image = "//button[@class='RemoveImage']"
    back_tab = "//div[@class='content']//button[@class='cancel']"
    save_profile = "//button[@class='save'][1]"
    register_for_another_store = "//button[@class='save'][2]"
    profile_select_centre_dropdown = "//i[@class='dropdown icon']"
    profile_selected_centre = "//div[@class='item'][1]"
    profile_selected_centre_next = "//button[1]"
    profile_select_store_dropdown = "//i[@class='dropdown icon']"
    profile_selected_store = "//div[@class='item'][2]"
    profile_selected_store_next = "//button[@class='save btn-info']"
    profile_terms_condition_tick_box = "//input[@id='checkbox_7']"
    profile_terms_condition_tick_box_next = "//button[@class='save btn-info']"
    register_for_another_store_password = "//input[@id='password']"
    register_for_another_store_confirm_password = "//input[@id='confirm_password']"
    register_for_another_store_register_button = "//button[contains(text(),'Register')]"
    registration_success_display = "//div[contains(text(),'Registration success')]"
    continue_tab = "//button[contains(text(),'Continue')]"
    cancel = "//button[@class='cancel']"
    profile_change_password = "//div[@class='content']//a[text()='Change Password']"
    old_password = "//div[@class='content']//input[@id='old_password']"
    new_password = "//div[@class='content']//input[@id='password']"
    confirm_new_password = "//div[@class='content']//input[@id='password_confirm']"

    # Header Tab Bar
    menu_button = "//div[@id='app']//i[@class='fa fa-bars']"
    centre_name = "//div[@id='app']//h1[@class='centre_Name']//a"
    notification_bell = "//i[@class='fa fa-bell']"
    search_button = "//div[@id='app']//i[@class='fa fa-search']"
    search_box = "//div[@class='inner']//input"
    help_button = "//div[@id='app']//i[@class='fa fa-question']"
    help_button_chatbot = "//div[@class='ChatBot']"
    help_button_chatbot_header = "//div[@class='ChatBot']//div[@class='head']"
    close_notification_button = "//i[@class='fa fa-times fa-3x']"
    logout = "//div[@id='app']//i[@class='fa fa-sign-out-alt']"
    switch_centre_button = "//h1[@class='centre_Name']//i[@class='material-icons']"
    switch_centre_search_button = "//div[@class='centre_switcher__search']"
    alt_centre = "//div[@class='centre_switcher__results']//li[2]"

    # Settings
    settings_button = "//div[@id='app']//i[@class='fa fa-cog']"
    choose_language_tab = "//label[text()='Choose your prefered Language']"
    settings_language_list = "//a[@class='cLng']"
    settings_english_us = "//a[@class='cLng'][1]"
    settings_czech = "//a[@class='cLng'][2]"
    settings_danish = "//a[@class='cLng'][3]"
    settings_dutch = "//a[@class='cLng'][4]"
    settings_french = "//a[@class='cLng'][5]"
    settings_german = "//a[@class='cLng'][6]"
    settings_hungarian = "//a[@class='cLng'][7]"
    settings_italian = "//a[@class='cLng'][8]"
    settings_polish = "//a[@class='cLng'][9]"
    settings_slovak = "//a[@class='cLng'][10]"
    settings_spanish = "//a[@class='cLng'][11]"
    settings_swedish = "//a[@class='cLng'][12]"
    settings_turkish = "//a[@class='cLng'][13]"
    settings_arabic = "//a[@class='cLng'][14]"
    settings_english_uk = "//a[@class='cLng'][15]"
    settings_terms_conditions = "//label[text()='Terms & Conditions']"
    settings_terms_conditions_content = "//div[contains(text(),'TERMS OF USE OR MOBILE')]"

