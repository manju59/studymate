# backend/config.py

import os
import streamlit as st

class Settings:
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_API_URL = os.getenv("MISTRAL_API_URL")

    @classmethod
    def validate(cls):
        if not cls.MISTRAL_API_KEY or not cls.MISTRAL_API_URL:
            st.error(
                "Please set MISTRAL_API_KEY and MISTRAL_API_URL environment variables."
            )
            st.stop()

# Validate at import time
Settings.validate()