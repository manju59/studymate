import os
import streamlit as st

class Settings:
    @classmethod
    def get(cls):
        api_key = os.getenv("MISTRAL_API_KEY")
        api_url = os.getenv("MISTRAL_API_URL")

        if not api_key or not api_url:
            st.error("Please set MISTRAL_API_KEY and MISTRAL_API_URL environment variables.")
            st.stop()

        return {
            "api_key": api_key,
            "api_url": api_url
        }