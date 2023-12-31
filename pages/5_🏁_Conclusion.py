import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from millify import millify
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="Uniswap On L2s",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Conclusion"}</h1>', unsafe_allow_html=True)
st.info("This page encapsulates the essential takeaways from our exploration, providing a holistic understanding of the state of Uniswap on L2s.", icon="ℹ️")


insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">As we conclude our examination of Uniswap\'s presence on Layer 2s, certain patterns come into focus. Token swap dynamics reveal a consistent preference for WETH and USDC, with variations on Avalanche and BSC. Arbitrum and Polygon emerge as key players, with Arbitrum particularly standing out in terms of user activity and swap volume, particularly among larger retail traders.</p>'
st.markdown(insight_1, unsafe_allow_html=True)


insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Optimism, while not commanding the highest volumes, showcases resilience and engagement, notably during airdrop events. Meanwhile, Avalanche and BSC grapple with retention challenges, prompting a closer look at how Uniswap can strengthen its foothold on these two L2s.</p>'
st.markdown(insight_2, unsafe_allow_html=True)
