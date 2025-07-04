import streamlit as st
import random

# ---------- Initialize menu in session state ----------
default_menu = {
    "noodles": ["Chicken Noodles", "Laksa", "Fried Bee Hoon", "Mee Rebus"],
    "rice": ["Chicken Rice", "Nasi Lemak", "Curry Rice", "Fried Rice"],
    "snacks": ["Spring Roll", "Fishball Stick", "Chicken Nuggets", "Fries"],
    "drinks": ["Milo", "Iced Lemon Tea", "Soy Milk", "Apple Juice"]
}

if "canteen_menu" not in st.session_state:
    st.session_state.canteen_menu = default_menu.copy()

canteen_menu = st.session_state.canteen_menu

# ---------- App UI ----------
st.title("🍱 Canteen Buddy Chatbot")

option = st.radio("Choose an option:", ["What to eat today?", "What new food I found?"])

# ---------- Option 1: Suggest food ----------
if option == "What to eat today?":
    category = st.selectbox("Pick a food category:", list(canteen_menu.keys()))
    if st.button("Give me a suggestion!"):
        suggestion = random.choice(canteen_menu[category])
        st.success(f"Here’s an idea from the **{category}** stall: **{suggestion}** 😋")

# ---------- Option 2: Add new food ----------
elif option == "What new food I found?":
    new_category = st.selectbox("Pick a category to add to:", list(canteen_menu.keys()))
    new_food = st.text_input("Enter the name of the new food:")

    if st.button("Add to list"):
        if new_food.strip() != "":
            if new_food not in canteen_menu[new_category]:
                canteen_menu[new_category].append(new_food)
                st.success(f"✅ Added **{new_food}** to **{new_category}**!")
            else:
                st.warning("⚠️ This food is already in the list.")
        else:
            st.warning("❗Please type a food name before adding.")
