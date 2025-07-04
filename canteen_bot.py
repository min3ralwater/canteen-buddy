import streamlit as st
import random
import datetime

canteen_menu = {
    "noodles": ["Chicken Noodles", "Laksa", "Fried Bee Hoon", "Mee Rebus"],
    "rice": ["Chicken Rice", "Nasi Lemak", "Curry Rice", "Fried Rice"],
    "snacks": ["Spring Roll", "Fishball Stick", "Chicken Nuggets", "Fries"],
    "drinks": ["Milo", "Iced Lemon Tea", "Soy Milk", "Apple Juice"]
}

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
            st.success(f"✅ Added **{new_food}** to **{new_category}**!")
        else:
            st.warning("Please type a food name before adding.")
