# canteen-buddy
Chat with me if you don't know what to eat
import streamlit as st
import random
import datetime
import json
import os

# ---------- Load or create menu file ----------
menu_file = "canteen_menu.json"

# Default menu (if first time run)
default_menu = {
    "noodles": ["Chicken Noodles", "Laksa", "Fried Bee Hoon", "Mee Rebus"],
    "rice": ["Chicken Rice", "Nasi Lemak", "Curry Rice", "Fried Rice"],
    "snacks": ["Spring Roll", "Fishball Stick", "Chicken Nuggets", "Fries"],
    "drinks": ["Milo", "Iced Lemon Tea", "Soy Milk", "Apple Juice"]
}

# Load or create menu
if os.path.exists(menu_file):
    with open(menu_file, "r") as f:
        canteen_menu = json.load(f)
else:
    canteen_menu = default_menu.copy()
    with open(menu_file, "w") as f:
        json.dump(canteen_menu, f)

# ---------- Streamlit UI ----------
st.title("🍱 Canteen Buddy Chatbot")

option = st.radio("Choose an option:", ["What to eat today?", "What new food I found?"])

if option == "What to eat today?":
    category = st.selectbox("Pick a food category:", list(canteen_menu.keys()))
    if st.button("Give me a suggestion!"):
        random.seed(datetime.date.today().toordinal())
        suggestion = random.choice(canteen_menu[category])
        st.success(f"Today’s pick for {category}: **{suggestion}** 😋")

elif option == "What new food I found?":
    new_category = st.selectbox("Pick a category to add to:", list(canteen_menu.keys()))
    new_food = st.text_input("Enter the name of the new food:")
    if st.button("Add to list"):
        if new_food:
            canteen_menu[new_category].append(new_food)
            # Save to file
            with open(menu_file, "w") as f:
                json.dump(canteen_menu, f)
            st.success(f"✅ Added **{new_food}** to **{new_category}**!")
        else:
            st.warning("Please type a food name before adding.")
