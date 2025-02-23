#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/23 17:25
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("English Text Annotation")
divider()
with expander("Instructions", expanded=True):
    caption("1. Enter the text in the text box.")
    caption("2. Push the button annotate annotating the entered English text.")

empty_message: empty = empty()

empty_message.info("You can enter the English text in the Manipulation page.")
