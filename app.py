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
                background-color: #FFDEE3;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 50%;
                margin: 0 auto;
                text-align: center;
                color: black;
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

class OverviewApp(HydraHeadApp):
    def run(self):
        st.title("Month Overview")
        st.write("Month overview coming soon!")

class LeaderboardApp(HydraHeadApp):
    def run(self):
        st.title("Leaderboard")
        st.write("Leaderboard coming soon!")

class BlogApp(HydraHeadApp):
    def run(self):
        st.title("Blog")
        st.write("Blog coming soon!")

if __name__ == "__main__":
    over_theme = {
        'txc_inactive': 'black',
        'menu_background': 'white',
        'txc_active': 'black',
        'option_active': '#FFDEE3'
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
    app.add_app("Overview", OverviewApp())
    app.add_app("Leaderboard", LeaderboardApp())
    app.add_app("Blog", BlogApp())


    # Run the HydraApp
    app.run()

