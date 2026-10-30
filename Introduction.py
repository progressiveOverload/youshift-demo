import streamlit as st

if "show_video" not in st.session_state:
    st.session_state.show_video = False


def toggle_video():
    st.session_state.show_video = not st.session_state.show_video


st.button("hello world", on_click=toggle_video)

if st.session_state.show_video:
    st.iframe(
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        width=763,
        height=429,
        alt="Rick Astley - Never Gonna Give You Up",
    )

st.badge(
    icon="👋",
    width="stretch",
    label="You can navigate via arrow on the upper left section",
)
st.divider()
st.header("Hey, Jota, Adolfo and Lucia, welcome to the demo!")
st.text("Demo includes 2 sections, data and business.")
st.text(
    "Respectively, they are focused on areas Jota and Adolfo described in their EYE posts."
)

st.text("Data: Approach to solve market intel and data engineering problem")
st.text(
    "Business: Combining data with pipeline tools to create meaningful business outputs"
)

st.header("Okay, let's build someting Youshift wants")
st.image(
    image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fih1.redbubble.net%2Fimage.5448843221.7506%2Fbg%2Cf8f8f8-flat%2C750x%2C075%2Cf-pad%2C750x1000%2Cf8f8f8.u1.jpg&f=1&nofb=1&ipt=3cee81f7203a9bcd06f61cbe2e073783e097b0c292e0e1d3d3b934d5a5d4ee32&ipo=images"
)
