#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:25:39 2025

@author: fcvmathieu
"""

import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.parse


# GitHub repository where images are stored (raw URL format)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/FC-Versailles/ryan/main/"

# Function to fetch images from GitHub
def load_image_from_github(filename):
    url = GITHUB_BASE_URL + filename
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"⚠️ Could not load image: {filename}")
        return None

image = load_image_from_github("pic.png")
if image:
    st.image(image, width=100)
# Title & Player Overview
st.title("Freddy Mbemba - 22 (RDC)")
# Button linking to Transfermarkt profile
st.link_button("Transfermarkt Profile", "https://www.transfermarkt.fr/ryan-tchato/profil/spieler/743516")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Key Insights
st.header("🔍 Key Insights")
st.markdown(
    """
    **xxx is an talented forward player with lot of potential. His football profile and personality are two strong indicators that suggest Freddy will reach the highest level.**
    
    **Personality & mentality** 🏃‍♂️💨
    - Strong determination to reach high level 
    - H

    
    **Football Profile**  🎯
    - Dribbling & Carrying: Excellent (P86) 
    - Shot Efficiency: Post-shot xG and touch in the box 
    - Speed & explosiveness : Strong physical habilities

    **Best suited for:** Freddy can help teams that play the offensive transition or direct play (speed, run behind) and also in positonnal attack (1v1 as winger or second striker) 🏹⚡
    """
)

# Define the WhatsApp number (include country code, no '+' sign)
whatsapp_number = "33771730001"  # Example: +33 for France

# Message to send
message = "Hello, I am interested in Freddy Mbemba. Can we discuss further?"

# Encode message for URL
encoded_message = urllib.parse.quote(message)

# WhatsApp URL
whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Button to open WhatsApp chat
if st.button("📲 Contact Sport Director"):
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">Send a whatsapp</a>', unsafe_allow_html=True)


st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Young player ready for a new step"):
    image = load_image_from_github("fiche.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy has progressed rapidly through divisions, demonstrating strong development potential.Freddy is a young talented forward player, right footed. His career path illustrate the potential and the development of Freddy. In 21/22 he played in 6th division, 22/23 he was transfered in USL Dunkerque in the 3rd Division. 23/24 USL Dunkerque jump in 2nd division and Freddy was in loan to Nimes in 3rd division. Freddy is ready to take a new step in his career")

with st.expander("📍 Position Played | Left Winger & Versatile Forward"):
    image = load_image_from_github("position.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy primarily plays as a left winger but is also comfortable as a second striker or right winger. Freddy is a complete forward player.")

with st.expander("⏳ Minutes played | A key player - 23/24 starting lineups"):
    image = load_image_from_github("minutes_played.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("This season Freddy is a key player for the team. Freddy took 22/23 lineups and more than 90% of the available minutes. For the first time of his career he took 2 yellows cards that bring to a missing match.")

with st.expander("🛡 Player Profile | Wide Threat - Explosive & Dribbler"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy excels in high-intensity attacking scenarios, with great dribbling skills and goal instincts. Freddy Mbemba is a high-intensity, direct winger with strong dribbling and goal-scoring instincts. His ability to take on defenders and progress the ball makes him an exciting attacking asset, but improving his crossing precision and playmaking could make him a more complete forward. 🚀")


with st.expander("📈 Performance Progression | Individual Development"):
    image = load_image_from_github("progression.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy Mbemba has transitioned into a more effective goal-scorer and playmaker (xG assisted), as seen by his higher xG assisted and goal contribution stats. However, there is a slight trade-off in his dribbling and ball progression, suggesting either a tactical shift (e.g., playing higher up the pitch) or defensive adaptation from opponents.")

with st.expander("👥 Player Comparison | Ernest Nuamah (Ligue 1)"):
    image = load_image_from_github("radar.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Advanced radar stats highlighting Freddy's capabilities to reach top level.")


with st.expander("🏋️ Physical Performance | High Intensity & Explosiveness"):
    image = load_image_from_github("physique.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Endurance: Covers significant distance per game (10,845m), showcasing strong stamina. Speed: Reaches a top speed of 32.5 km/h, indicating strong sprint capabilities. In term of intensity: High acceleration/deceleration numbers (35 accelerations, 38 decelerations per game), proving his ability to make explosive movements and quick changes of direction. Sprint Efforts: 27 sprints per game, maintaining a good balance between high-intensity bursts and recovery.")

with st.expander("🤕 Injury History | Robust Player"):
    image = load_image_from_github("injuries.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy has maintained excellent availability with no major injuries this season. Freddy is a robust player. He did not get any injury this year that bring 100% of availabity for training and match. He takes care about his body with some session with physio (massage & cares).")

with st.expander("⚖️ Weight Evolution"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Monitoring body composition is key to performance optimization. He is currently working with a nutritionist")

with st.expander("🔥 Personnality & Motivation | high self determination"):
    image = load_image_from_github("Happiness.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Freddy is highly motivated and dedicated to his football journey. His motivation runs deep, rooted in his childhood passion, with a constant desire to progress and reach the highest levels of football.")

with st.expander("📊 Game Report"):
    image = load_image_from_github("game_report.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Example of Game report, please contact Mathieu Feigean for more explanation or request.")






st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p><strong>M.Feigean</strong> - Football Development</p>
    </div>
    """, unsafe_allow_html=True)

