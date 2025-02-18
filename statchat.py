import streamlit as st
import random
from PIL import Image

#  C:/Users/Other/.venv/Scripts/python.exe -m streamlit run c:/Users/Other/Desktop/eagles-bot/statchat.py

# List of random responses
# List of random responses
responses = [
    "Eagles are better than the Lions, Vikings, and Packers combined!",
    "Cooper Dejean is the best cornerback in the league! He recorded his first interception in the Super Bowl against the baby goat.",
    "The Eagles won 4 games in the 2024-2025 playoffs, which was 4 more than the Lions, Packers, and Vikings combined.",
    "Jalen Hurts has more playoff wins in the last three years than the Lions, Packers, and Vikings combined!",
    "The Eagles' defense allowed fewer points per game than any NFC North team in 2024!",
    "Philadelphia has won 16 playoff games since 2000—more than the Lions, Packers, Vikings, and Bears combined!",
    "A.J. Brown had more receiving yards in 2024 than any NFC North receiver!",
    "The Eagles have been to three NFC Championships since 2017. The entire NFC North? Just one.",
    "Detroit won their first playoff game in 30 years in 2024. Philly won a Super Bowl six years ago.",
    "Eagles fans argue about Super Bowls. NFC North fans argue about who lost to Philly worse.",
    "The Eagles have a top-5 offensive line every year. NFC North teams are still searching for one.",
    "Philadelphia had a higher team PFF grade than every NFC North team in 2024!",
    "Philly's run game dominated the NFC North last year—more rushing yards than all four teams in head-to-head matchups!",
    "Tails never fails!",
    "The Eagles had more Pro Bowl selections in 2024 than the entire NFC North combined!",
    "Jalen Carter had more sacks in 2024 than any interior lineman in the NFC North!",
    "The Eagles had a better third-down conversion rate than every NFC North team last season!",
    "Since 2017, the Eagles have played in more Super Bowls than the entire NFC North combined!",
    "The last time the Vikings won a championship, gas was 36 cents a gallon.",
    "Jordan Davis and Jalen Carter are nightmares for NFC North offensive lines!",
    "DeVonta Smith has more career playoff receiving yards than any active NFC North WR.",
    "The Eagles have finished with a winning record five straight seasons. No NFC North team has done that since the 1990s.",
    "Philadelphia’s defense forced more turnovers than any NFC North team in 2024.",
    "Dallas Goedert has more playoff receptions than any starting NFC North tight end.",
    "The Eagles’ pass rush had more sacks than any NFC North team in 2024!",
    "Since 2017, the Eagles have won more playoff games at home than the Lions, Packers, Bears, and Vikings combined.",
    "Nick Sirianni has more NFC Championship appearances than any NFC North coach.",
    "The Eagles led the league in QB sneaks again in 2024, while NFC North teams still can’t figure out how to stop it!",
]



import streamlit as st
import random
from PIL import Image

# Load the avatar image
avatar = Image.open("dan.jpg")

# Set the title and caption
st.title("StatChat")
st.caption("\U0001F3C8 An NFL Statistical Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I am StatChat. Ask me anything about the NFL 2024-2025 season!"}]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        with st.chat_message("assistant", avatar=avatar):
            st.write(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Select a random response
    response = random.choice(responses)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar=avatar):
        st.write(response)
