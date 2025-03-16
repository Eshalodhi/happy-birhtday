import streamlit as st
import random

def birthday_wish():
    wishes = [
        "🎉 Happy Birthday! May your year ahead be filled with endless happiness, love, and success! 🎂✨",
        "🥳 Wishing you a birthday as bright and wonderful as your smile! Stay blessed and keep shining! 🌟🎈",
        "🎊 Happy Birthday! May this special day bring you countless reasons to laugh, unforgettable memories, and dreams coming true! 🎁🎂",
        "🎂 Today is all about you! May your day be filled with love, surprises, and moments that make you feel extra special! 🎉🎈",
        "🌟 Happy Birthday! May your heart be light, your dreams be big, and your journey ahead be full of magical moments! ✨🎂",
        "🎈 Cheers to another fantastic year! May you always find reasons to smile and celebrate life’s beautiful moments! 🥳🎊"
    ]
    return random.choice(wishes)

st.title("🎂 Happy Birthday Ammy! 🎉")

st.subheader(birthday_wish())
