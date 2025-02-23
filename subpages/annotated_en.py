#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/23 17:26
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   annotated_en.py
# @Desc     :

from streamlit import text_area, sidebar, header, button, caption, spinner

from utilis.tools import is_english, EnglishAnnotator, VALUES

text = text_area(
    "ENTER THE ENGLISH TEXT:", max_chars=300, placeholder="Enter the English text here.",
    height=300, value=VALUES, help="Please enter the English text in the text box."
)
if is_english(text):
    caption("The entered text **IS** in English.")
else:
    caption("The entered text is **NOT** in English. Please enter the English text.")

with sidebar:
    header("Actions")
    action = button("Annotate", type="primary", help="Click to annotate the entered English text.")

if action:
    with spinner("Annotating the text...", show_time=True):
        EnglishAnnotator(text).annotate()
