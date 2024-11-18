from streamlit_option_menu import option_menu
def home_page():
    homepage = option_menu(None,options = ["Home", "Root-Finding Methods", "Linear Algebraic Equations",'Numerical Differentiation','Numerical Integration','Non-Linear Optimization'],
        icons=['house','calculator', "braces",'list-ol','type-italic',"graph-up"],
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container":{"width":"100%"},
            "nav-link": {"font-size": "12px", "text-align": "center", "margin":"0px","color":"#eee"},
            "nav-link-selected": {
                "background-color": "#112A46",
            }
        }
        )
    return homepage