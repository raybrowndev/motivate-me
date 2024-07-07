import streamlit as st
from hydralit import HydraApp, HydraHeadApp
import random

# Define the themes
themes = [
    "PLASTIC BOTTLES", ## blue #CCF2FF
    "STEPS", ## yellow #FFFFB2
    "RECYCLING", ## green #D6FFC2
    "SCREEN TIME", ## orange #ffdfd3
    "TRANSPORT" ## purple #E8D1FF
]

# Function to pick a random theme
def pick_theme():
    return random.choice(themes)

# Define a new HydraHeadApp for theme selection
class ThemeSelectionApp(HydraHeadApp):
    def run(self):
        # Custom CSS to align the title and center the text
        st.markdown(
            """
            <style>
            .title {
                text-align: center;
            }
            .centered-box {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background-color: #0A215A;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 50%;
                margin: 0 auto;
                text-align: center;
                color: white;
                font-size: 24px;
                font-family: Arial, sans-serif;
                font-weight: bold;
            }
            .centered-text {
                text-align: center;
                font-size: 24px;
                font-family: Arial, sans-serif;
                font-weight: bold;
                margin-top: 20px;
            }
            .blue-box {
                background-color: #CCF2FF; /* Blue background color */
                color: black; /* Text color */
                padding: 30px; /* Adjust padding for blue box */
                border-radius: 15px; /* Adjust border radius for blue box */
                width: 17%;
            }
            .purple-box {
                background-color: #E8D1FF; /* Purple background color */
                color: black; /* Text color */
                padding: 25px; /* Adjust padding for pink box */
                border-radius: 12px; /* Adjust border radius for pink box */
                width: 11%;
            }
            .green-box {
                background-color: #D6FFC2; /* Green background color */
                color: black; /* Text color */
                padding: 20px; /* Adjust padding for green box */
                border-radius: 10px; /* Adjust border radius for green box */
                width: 11%;
            }
            .yellow-box {
                background-color: #FFFFB2; /* Yellow background color */
                color: black; /* Text color */
                padding: 20px; /* Adjust padding for green box */
                border-radius: 10px; /* Adjust border radius for green box */
                width: 7%;
            }
            .orange-box {
                background-color: #ffdfd3; /* Orange background color */
                color: black; /* Text color */
                padding: 20px; /* Adjust padding for green box */
                border-radius: 10px; /* Adjust border radius for green box */
                width: 13%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Streamlit app with custom CSS class for the title
        st.markdown('<h1 class="title">MotivateMe🧠</h1>', unsafe_allow_html=True)
        st.text(" ")
        st.text(" ")
        st.text(" ")

        # Centered box with blue background and text
        st.markdown("""
        <div class="centered-box">
            ⬇️ PICK YOUR THEME FOR THE WEEK  ⬇️
        </div>
        """, unsafe_allow_html=True)

        st.text(" ")
        st.text(" ")
        st.text(" ")
        picked = False
        # Use st.beta_columns to create layout columns
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15 = st.columns(15)

        # Use col8 to center the button
        with col8:
            if st.button("Pick Theme", key="pick_button", type="secondary"):
                # st.text(" ")
                picked = True

        if picked:
            selected_theme = pick_theme()
            # Centered text for the theme announcement
            st.write('<div class="centered-text">This week\'s theme is... </div>', unsafe_allow_html=True)
            st.text(" ")

            # Display the selected theme in a centered box with a different color
            if selected_theme == "PLASTIC BOTTLES":
                box_color_class = "blue-box"
            elif selected_theme == "STEPS":
                box_color_class = "yellow-box"
            elif selected_theme == "RECYCLING":
                box_color_class = "green-box"
            elif selected_theme == "SCREEN TIME":
                box_color_class = "orange-box"
            elif selected_theme == "TRANSPORT":
                box_color_class = "purple-box"

            st.markdown(f"""
                        <div class="centered-box {box_color_class}">
                            <b>{selected_theme}</b>
                        </div>
                        """, unsafe_allow_html=True)


# Define a basic Streamlit app

class LogDetails(HydraHeadApp):
    def run(self):
        # Custom CSS to align the title in the center and style the action required line and form
        st.markdown(
            """
            <style>
            .log-details-title {
                text-align: center;
                margin-bottom: 20px; /* Add margin to the bottom of the title */
            }
            .action-required {
                text-align: center;
                color: red;
                font-size: 20px;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 20px; /* Add margin to the bottom of the action required line */
            }
            .form-container {
                max-width: 600px; /* Set a maximum width for the form container */
                margin: 0 auto; /* Center align the form horizontally */
            }
            .form-label {
                display: inline-block;
                width: 120px; /* Set a fixed width for the labels */
                text-align: center; /* Center align text within labels */
                font-size: 18px;
                font-weight: bold;
                margin-right: 10px;
            }
            .form-input {
                width: 200px; /* Adjust this value to make the input box smaller */
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                text-align: center; /* Center align text within input boxes */
            }
            .form-row {
                display: flex;
                align-items: center;
                justify-content: center; /* Center align items horizontally */
                margin-bottom: 10px; /* Add margin to the bottom of each form row */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Use the custom CSS class in the title
        st.markdown('<h1 class="log-details-title">Log Details✨</h1>', unsafe_allow_html=True)

        # Use the custom CSS class for the action required line
        st.markdown('<div class="action-required">Action Required: Please log details from yesterday</div>', unsafe_allow_html=True)

        # Form for TEAM, NAME, THEME, and DAILY COUNT
        form_fields = [
            ("TEAM:", "Enter your team"),
            ("NAME:", "Enter your name"),
            ("THEME:", "Enter the theme"),
            ("DAILY COUNT:", "Enter daily count")
        ]

        # Wrap the form in a container div for centering and alignment
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        for label, placeholder in form_fields:
            st.markdown(
                f"""
                <div class="form-row">
                    <label class="form-label">{label}</label>
                    <input class="form-input" type="text" placeholder="{placeholder}">
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)




if __name__ == "__main__":
    over_theme = {
        'txc_inactive': 'black',
        'menu_background': 'white',
        'txc_active': 'white',
        'option_active': '#0A215A'
    }

    # Initialize the HydraApp with navbar theme
    app = HydraApp(
        title='MotivateMe',
        favicon="🧠",
        hide_streamlit_markers=True,
        use_navbar=True,
        navbar_sticky=True,
        navbar_animation=False,
        navbar_theme=over_theme  # Pass the navbar theme here
    )
    app.enable_guest_access()

    # Add the apps to the HydraApp instance
    app.add_app("Home", ThemeSelectionApp(), is_home=True)  # Use ThemeSelectionApp for the home page
    app.add_app("Log Details", LogDetails())

    # Run the HydraApp
    app.run()
