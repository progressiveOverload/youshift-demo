import pandas as pd
import streamlit as st

st.header("Go-to-market planning with our newly acquired data")

# Deduplicated case data from the Data page
CASE = [
    {
        "org": "AG SIMPLY MEDICINE",
        "status": "A",
        "taxonomy": "Anesthesiology, Pain Medicine",
        "official": "AMIT GUPTA",
        "official_title": "Trustee",
        "official_phone": "8054228131",
        "primary_address": "1687 ERRINGER RD STE 217, SIMI VALLEY, CA",
    },
    {
        "org": "ANCHOR ERUPTION ENTERPRISES LLC",
        "status": "A",
        "taxonomy": "Anesthesiology, Pain Medicine",
        "official": "SHAMSIDEEN MUSA",
        "official_title": "CMO/Owner",
        "official_phone": "9077718178",
        "primary_address": "9500 INDEPENDENCE DR STE 700, ANCHORAGE, AK",
    },
    {
        "org": "ARLINGTON ANESTHESIA GROUP, PLLC",
        "status": "A",
        "taxonomy": "Anesthesiology",
        "official": "BRETT EHRHARDT",
        "official_title": "CFO",
        "official_phone": "7203580218",
        "primary_address": "350 E INTERSTATE 20 STE 200, ARLINGTON, TX",
    },
    {
        "org": "AZURA ANESTHESIA PARTNERS LLC",
        "status": "A",
        "taxonomy": "Anesthesiology",
        "official": "GREGG MILLER",
        "official_title": "Authorized Official",
        "official_phone": "7175154048",
        "primary_address": "8140 CORPORATE DR STE 125, NOTTINGHAM, MD",
    },
    {
        "org": "BLUE CLOUD ANESTHESIA, LLC",
        "status": "A",
        "taxonomy": "Anesthesiology",
        "official": "DEVIN LARSEN",
        "official_title": "CEO",
        "official_phone": "2083401840",
        "primary_address": "1000 WOODCOCK RD STE 120, ORLANDO, FL",
    },
    {
        "org": "CAPITOL PAIN INSTITUTE, PA",
        "status": "A",
        "taxonomy": "Anesthesiology, Pain Medicine",
        "official": "SANDFORD SCHOCKET",
        "official_title": "Director",
        "official_phone": "5124677246",
        "primary_address": "8015 SHOAL CREEK BLVD STE 103, AUSTIN, TX",
    },
    {
        "org": "CCMMA CA PC",
        "status": "A",
        "taxonomy": "Anesthesiology, Critical Care Medicine",
        "official": "LAURIE LADUCA",
        "official_title": "CREDENTIALING MANAGER",
        "official_phone": "8457022711",
        "primary_address": "1100 BUTTE ST, REDDING, CA",
    },
    {
        "org": "CCMMA NJ LLC",
        "status": "A",
        "taxonomy": "Anesthesiology, Critical Care Medicine",
        "official": "LAURIE LADUCA",
        "official_title": "MANAGER",
        "official_phone": "8457022711",
        "primary_address": "350 BOULEVARD, PASSAIC, NJ",
    },
    {
        "org": "CCMMA TX PLLC",
        "status": "A",
        "taxonomy": "Anesthesiology",
        "official": "LAURIE LADUCA",
        "official_title": "MANAGER",
        "official_phone": "8457022711",
        "primary_address": "2 PARK AVE STE 2039, NEW YORK, NY",
    },
    {
        "org": "CRITICAL CARE MEDICAL MANAGEMENT ASSOCIATES PLLC",
        "status": "A",
        "taxonomy": "Anesthesiology, Critical Care Medicine",
        "official": "LAURIE LADUCA",
        "official_title": "CREDENTIALING MANAGER",
        "official_phone": "8457022711",
        "primary_address": "701 N BROADWAY, SLEEPY HOLLOW, NY",
    },
    {
        "org": "EPMED, PA",
        "status": "A",
        "taxonomy": "Anesthesiology, Pain Medicine",
        "official": "EDUARDO VAZQUEZ",
        "official_title": "President",
        "official_phone": "9155987246",
        "primary_address": "3215 GATEWAY BLVD W, EL PASO, TX",
    },
]

st.dataframe(pd.DataFrame(CASE))

st.divider()

st.header("Plan")
st.image("images/todo-business.png")

st.divider()
st.header("I was thinking I would make this section mostly in Clay.")
st.text(
    "Unfortunately I'm out of credits so here's an approach held together by duct tape and bubble gum. Aka doing things that don't scale."
)
st.image(
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.Mb7BJ426O1ndhYnic89oJAHaEj%3Fpid%3DApi&f=1&ipt=417cb1740f143d600f4cd9ad5121a78597dce1f4ee0fb5144586a74369d36405&ipo=images"
)
