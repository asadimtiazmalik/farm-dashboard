from hydralit import HydraApp
import streamlit as st
import apps
if __name__ == '__main__':
    over_theme = {'txc_inactive': '#FFFFFF'}
    navbar_theme = {
        'txc_inactive': '#333333',  # Inactive Menu Item Text color (dark gray)
        'menu_background': '#F5F5F5',  # Menu Background Color (light gray)
        # 'txc_active': '#FFFFFF',     # Active Menu Item Text Color (white)
        # 'option_active': '#87CEFA'     # Active Menu Item Color (light blue)
    }
    #this is the host application, we add children to it and that's it!
    app = HydraApp(
        title='Wheat Health Monitoring Dashboard',
        favicon="🐙",
        hide_streamlit_markers=True,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_banner_images=["./resources/logo.png",None,{'header':"<h1 style='text-align:center;padding: 30px 0px 0px 0px ;color:black;font-size:200%;'>Wheat Health Monitoring Dashboard</h1><br>"},None,"./resources/nust.png"], 
        banner_spacing=[10,30,60,30,10],
        use_navbar=True, 
        navbar_sticky=False,
        navbar_theme=navbar_theme
    )

    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(),is_home=True)

    #add all your application classes here
    app.add_app("Raster Viz", icon="🛰️", app=apps.UploadApp())
    # app.add_app("Sequency Denoising",icon="🔊", app=apps.WalshApp(title="Sequency Denoising"))
    # app.add_app("Sequency (Secure)",icon="🔊🔒", app=apps.WalshAppSecure(title="Sequency (Secure)"))
    # app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title="Solar Mach"))
    # app.add_app("Spacy NLP", icon="⌨️", app=apps.SpacyNLP(title="Spacy NLP"))
    # app.add_app("Uber Pickups", icon="🚖", app=apps.UberNYC(title="Uber Pickups"))
    # app.add_app("Solar Mach", icon="🛰️", app=apps.SolarMach(title="Solar Mach"))

    complex_nav = {
    'Home': ['Home'],
    'View': ['Raster Viz']
    }
    app.run(complex_nav)
