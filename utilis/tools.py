#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/23 17:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :

from enum import StrEnum, unique
from re import fullmatch
from spacy import cli, load
from stqdm import stqdm
from streamlit import markdown
from string import punctuation


def is_english(text: str) -> bool:
    """ Check if the text is in English """
    pattern: str = r"[A-Za-z0-9\s\W]+"
    return bool(fullmatch(pattern, text))


@unique
class Color(StrEnum):
    """ Color Enum """
    RED: str = "#FFAAAA"
    YELLOW: str = "#FFEEAA"
    BLUE: str = "#88EEFE"
    GREEN: str = "#AAFFAA"
    GRAY: str = "#525352"


class EnglishAnnotator(object):
    """ This class is used to annotate text with different colors """

    def __init__(self, text: str) -> None:
        self._input = text
        cli.download("en_core_web_sm")
        self._nlp = load("en_core_web_sm")
        self._doc = self._nlp(self._input)
        self._tokens = [(token.text, token.pos_) for token in self._doc]

    def annotate(self, size_main: int = 20, padding: int = 5, margin: int = 3, border_radius: int = 10) -> None:
        """ Annotate the text """
        _annotated: list = []
        _adjust: float = 0.6

        for token, pos in stqdm(self._tokens, desc="Annotating the text...", unit="token", total=len(self._tokens)):
            if token in punctuation:
                token = (f"<span style='font-size:{size_main}px;"
                         f"display:inline-block;"
                         f"margin-bottom:{margin}px;'>{token}</span>")
                _annotated.append(token)
                continue

            match pos:
                case "NOUN":
                    token = token.replace(token,
                                          f"<span style='background-color:{Color.YELLOW};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{Color.GRAY};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case "VERB":
                    token = token.replace(token,
                                          f"<span style='background-color:{Color.RED};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{Color.GRAY};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case "ADJ":
                    token = token.replace(token,
                                          f"<span style='background-color:{Color.BLUE};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{Color.GRAY};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case "ADV":
                    token = token.replace(token,
                                          f"<span style='background-color:{Color.GREEN};"
                                          f"font-size:{size_main}px;"
                                          f"padding:{padding}px;"
                                          f"display:inline-block;"
                                          f"margin-bottom:{margin}px;"
                                          f"border-radius:{border_radius}px;'>{token} "
                                          f"<span style='color:{Color.GRAY};"
                                          f"font-size:{size_main * _adjust}px;'>{pos}</span></span>")
                    _annotated.append(token)
                case _:
                    token = (f"<span style='font-size:{size_main}px;"
                             f"padding:{padding}px;"
                             f"display:inline-block;"
                             f"margin-bottom:{margin}px;'>{token}</span>")
                    _annotated.append(token)

        string = " ".join(_annotated)
        markdown(string, unsafe_allow_html=True)


VALUES: str = """
Beneath the silver glow of a crescent moon, Elara wandered through the ancient forest, \
her footsteps light against the moss-covered ground. The trees, \
towering and twisted, murmured in a gentle, \
rhythmic whisper as if sharing the secrets of centuries past. \
A calm, fragrant breeze drifted through the leaves, sending a shiver down her spine. \
She paused, her heart racing, as a shadow emerged from the mist—a wolf, \
its amber eyes gleaming with unspoken knowledge. Silently, it approached, \
its graceful, fluid movements mirroring the mystery of the night. \
Yet, Elara felt no fear. Instead, a strange, warm calm filled her, \
like the forest had woven an ancient spell around her. \
The wolf watched her for a moment longer, then vanished, leaving only its presence's soft, \
lingering echoes. Elara smiled—she understood now. \
The forest was alive, and she had become part of its eternal, whispered tale.
"""
