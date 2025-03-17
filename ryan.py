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
st.title("Ryan Tchato - 20 (FR)")
# Button linking to Transfermarkt profile
st.link_button("Transfermarkt Profile", "https://www.transfermarkt.fr/ryan-tchato/profil/spieler/743516")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Key Insights
st.header("🔍 Key Insights")
    # Physical Profile Analysis
st.markdown(
    """
    #### **Powerful & defensive Full-Back**
    
    **🌟 Overview**
    - A **dynamic, physically strong right-back** with impressive speed and defensive qualities.
    - Capable of playing both **right-back (RB) and right wing-back (RWB)**, providing tactical flexibility.
    - **Fast, aggressive, and hard to beat in 1v1 duels**, making him a strong defensive asset.

    ##### **🧠 Personality & Mentality**
    - **Highly competitive & aggressive**, thrives in defensive duels.
    - **Hardworking & physically resilient**, covering large distances per game.
    - **Tactical discipline**, making him reliable in defensive setups.
    - **Room for leadership growth**, could develop into a vocal presence in the backline.

    ##### **🎯 Football Profile**
    - **Defensive Strengths:**
      - **Strong in duels**, aggressive in 1v1 situations.
      - **Excellent tackling & interceptions**, often wins the ball high up the pitch.
      - **Aerially solid**, rare for a full-back.
    
    - **Physical & Athletic Qualities:**
      - **Top speed of 31.2 km/h**, making him one of the fastest full-backs.
      - **High-intensity sprints & endurance**, allowing him to cover ground effectively.
      - **Explosive acceleration & deceleration**, ideal for both pressing and recovery runs.

    - **Attacking Contributions (Needs Improvement):**
      - **Limited in deep progressions & crossing accuracy**.
      - **Can improve ball carrying under pressure**.
      - **Potential to develop as a modern attacking full-back with better offensive output**.

    ##### **🔄 Areas for Development**
    - **Increase attacking impact** with better crossing and decision-making in the final third.
    - **Improve ball retention under pressure** to limit turnovers.
    - **Work on attacking positioning** to contribute more in wide areas.

    ##### **🚀 Future Potential**
    - **Currently a solid defensive full-back**, with room to evolve into a **complete modern right-back**.
    - **Ideal for a high-intensity pressing team**, where his defensive work rate and speed are valuable.
    - **A move to Ligue 2 or an international club** could be the next logical step if he improves his attacking impact.

    ✅ **Ryan is a strong, aggressive full-back with elite defensive qualities and physical attributes. If he refines his attacking play, he could become a top-level modern full-back.**
    """
)

# Define the WhatsApp number (include country code, no '+' sign)
whatsapp_number = "33771730001"  # Example: +33 for France

# Message to send
message = "Hello, I am interested in Ryan Tchato. Can we discuss further?"

# Encode message for URL
encoded_message = urllib.parse.quote(message)

# WhatsApp URL
whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Button to open WhatsApp chat
if st.button("📲 Contact Sport Director"):
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">Send a whatsapp</a>', unsafe_allow_html=True)


st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Special young player "):
    image = load_image_from_github("fiche.png")
    if image:
        st.image(image, use_container_width=True)
    # Career Analysis
    st.write("""
    ### 🛤 **Career Path Analysis:**
    - **Early Development:** Trained at Montpellier’s academy, progressing from the U19s to the B team.
    - **Professional Transition:** Moved to **FC Versailles** in August 2024, a crucial step to gain first-team experience in National (3rd division).
    - **Versatility:** Primarily a **right-back**, but also capable of playing **left-back and right midfield**, adding tactical flexibility.
    
    ### 🚀 **Next Step:**
    - **Key Strengths:**
      - Strong **mentality and work ethic**, essential for high-level progression.
      - **Good defensive fundamentals** combined with offensive contributions.
      - **Adaptable**, making him an asset in various systems.
    
    - **Future Progression:**
      - If he **performs consistently in National**, he could attract **Ligue 2 clubs** looking for a modern full-back.
      - Should focus on **developing tactical awareness** and refining technical aspects like crossing and ball progression.
      - **Long-term potential:** With continued growth, could become an asset for **top-tier leagues or international competitions**.
    
    ✅ **Ryan possesses the right mentality and work rate for the top level. His next challenge is proving consistency at Versailles to earn a move to a higher division.**
    """)

with st.expander("📍 Position Played | Defensive right back"):
    image = load_image_from_github("position.png")
    if image:
        st.image(image, use_container_width=True)
    # Positional Analysis
    st.write("""
    ### **Ryan Tchato | Versatile Right-Back**
    - **Main Position:** Right-Back (RB) 
    - **Alternative Role:** Right Wing-Back (RWB) in more attacking setups.
    
    **🔍 Tactical Profile:**
    - Primarily a **defensive full-back**, solid in 1v1 situations.
    - Comfortable pushing forward as a **right wing-back** when needed.

    ✅ **Ryan is a solid, defensively reliable full-back with room for growth in offensive contributions.**
    """)

with st.expander("⏳ Minutes played | An asset player"):
    image = load_image_from_github("minutes_played.png")
    if image:
        st.image(image, use_container_width=True)
    # Performance Analysis
    st.write("""
    ### **📊 Match Involvement:**
    - **Appearances:** Featured in multiple matches but with inconsistent minutes.
    - **Starting Role:** Began some games but was often substituted out.
    - **Late-Season Trends:** Reduced game time in 2025, possibly due to competition, injury, or tactical changes.
    - **Unused Substitute & DNP Matches:** Several instances where he wasn’t used, indicating he may be in a rotational role.

    """)
with st.expander("🛡 Player Profile | Defensive right back"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
# Player profile analysis
    st.write("""
    ### **Ryan Tchato | Physical & Aggressive Full-Back**
    
    #### **🔍 Strengths:**
    - **Defensive Ability:** Excels in aggressive actions, tackles, and interceptions, ranking above the league average.
    - **Aerial Presence:** Strong in aerial duels, which is a rare quality for a full-back.
    - **High Defensive Actions:** His involvement in defensive duels and recoveries is higher than most full-backs in the league.
    - **Press Resistance:** Handles pressure well when passing, minimizing costly errors.

    #### **📉 Areas for Improvement:**
    - **Offensive Contribution:** Below league average in deep progressions, crosses, and passing impact.
    - **Ball Carrying & Creativity:** Needs to improve his ball progression and confidence in attacking phases.
    - **Turnovers:** A tendency to lose possession in build-up play, requiring better decision-making under pressure.

    #### **📊 Tactical Fit:**
    - Best suited for a **defensive-minded team** that prioritizes solidity over offensive overlapping runs.
    - Could be valuable in a **back three system as a right wing-back** if he improves crossing and attacking contributions.
    - Ideal for **a team that presses high**, as his aggressive duels and interceptions suit proactive defensive structures.

    ### **🚀 Next Steps in Development:**
    - Work on crossing accuracy and final third decision-making.
    - Improve technical ability in **1v1 offensive duels** to be more dangerous going forward.
    - Enhance passing range and confidence to initiate plays more effectively.

    ✅ **Ryan is an aggressive, defensively solid full-back with strong tackling and aerial ability. If he improves his offensive impact, he could develop into a high-level modern full-back.**
    """)

# with st.expander("📈 Performance Progression | Individual Development"):
#     image = load_image_from_github("progression.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("For the first season in 3rd french division, Ryan show a real interest in the individual development. Wer aim to develop his technical skills and also improve his offensive contribution")
             
             
# with st.expander("👥 Player Comparison | Ernest Nuamah (Ligue 1)"):
#     image = load_image_from_github("radar.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Advanced radar stats highlighting Freddy's capabilities to reach top level.")


with st.expander("🏋️ Physical Performance | High Intensity & Power"):
    image = load_image_from_github("physique.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("""
    ### **Ryan Tchato | Explosive & Enduring Full-Back**
    
    #### **📊 Key Physical Attributes:**
    - **Total Distance Covered:** High work rate, covering an average of **10,828m per game**.
    - **High-Speed Running (16-24 km/h):** **1,787 meters per game**, indicating strong mobility and ability to track back.
    - **Sprints (>24 km/h):** Reaches **255 meters per game**, showing his ability to accelerate quickly.
    - **Acceleration & Deceleration:**
      - **13 accelerations per game** (>4m/s²), meaning he can quickly reach top speed.
      - **36 decelerations per game**, crucial for defensive recoveries and transitions.
    - **Top Speed (VMAX):** Peaks at **31.2 km/h**, which is fast for a full-back.

    #### **🔍 Strengths:**
    - **Explosive in short bursts**, allowing him to recover defensively.
    - **High endurance**, making him effective in both defensive and offensive phases.
    - **Speed for tracking back and overlapping runs**.
    - **Aggressive deceleration**, allowing him to adjust his position quickly.

    #### **📉 Areas for Development:**
    - **Increase sprint frequency** to become more dangerous on overlaps.
    - **Improve acceleration efficiency** to be more reactive in tight spaces.
    - **Refine movement patterns** to optimize energy use and avoid fatigue.

    #### **📌 Tactical Fit:**
    - Suited for **high-intensity pressing teams** due to his speed and endurance.
    - Can excel in **attacking full-back roles**, provided he enhances his final-third impact.
    - **Well-adapted to modern football**, where full-backs need high physical output.

    ✅ **Ryan is a physically gifted full-back with explosive speed and endurance. With better offensive involvement, he could become a top-tier modern defender.**
    """)


with st.expander("🤕 Injury History | Robust Player"):
    image = load_image_from_github("injuries.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("He had no injuries this year. Djamal is very robust and take care of his body")

with st.expander("⚖️ Weight Evolution"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Mxxx")

# with st.expander("🔥 Personnality & Motivation | high self determination"):
#     image = load_image_from_github("Happiness.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("x")




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

