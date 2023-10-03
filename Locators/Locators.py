class Locators():
    # Website URL'S
    baseURL = "https://www.saucedemo.com/"
    aboutURL = "https://saucelabs.com/"
    all_items_URL = "https://www.saucedemo.com/inventory.html"
    cart_URL = "https://www.saucedemo.com/cart.html"

    # Login objects
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_logout_id = "logout_sidebar_link"
    username = "standard_user"
    password = "secret_sauce"

    # Sidebar Objects
    sidebar_menu_button_id = "react-burger-menu-btn"
    sidebar_cross_button_id = "react-burger-cross-btn"
    sidebar_block_class_name = "bm-menu-wrap"
    sidebar_link1_all_items = "inventory_sidebar_link"
    sidebar_link2_about = "about_sidebar_link"
    sidebar_link3_logout = "logout_sidebar_link"
    sidebar_link4_reset_app_states = "reset_sidebar_link"

    # Cart page Objects
    shopping_cart_continue_shopping_btn = "continue-shopping"
    sort_filter_class_name = "product_sort_container"
    product_item_name_class_name = "inventory_item_name"
    product_item_description_class_name = "inventory_item_desc"
    product_item_price_class_name = "inventory_item_price"
    product_details_name_class_name = "inventory_details_name"
    product_details_description_class_name = "inventory_details_desc"
    product_details_price_class_name = "inventory_details_price"
    cart_item_name_class_name = "inventory_item_name"
    cart_item_description_class_name = "inventory_item_desc"
    cart_item_price_class_name = "inventory_item_price"
    shopping_cart_btn_class_name = "shopping_cart_link"
    add_to_cart_btn = "btn_inventory"
    app_logo_class_name = "app_logo"
    inventory_item_class_name = "inventory_item"


    #  XL data file locators
    login_data_file_path = "XL data/LoginData.xlsx"
    product_name_data_file_path = "XL data/product_names.xlsx"
