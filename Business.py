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
st.image("images/todo-business2.png")

st.divider()
st.header("This was harder than I was thinking")
st.text(
    "Basic B2B cold email outreach is hard in YouShift's case and seeing you guys attend 3 events in a month kind of reinforces this case."
)
st.image(
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.Mb7BJ426O1ndhYnic89oJAHaEj%3Fpid%3DApi&f=1&ipt=417cb1740f143d600f4cd9ad5121a78597dce1f4ee0fb5144586a74369d36405&ipo=images"
)

st.divider()
st.header("First Problem, Data export structure on Hubspot")

st.image("images/hs-issue.png")
st.text(
    "Although import was looking alright, in practice contacts and company connections wasn't there."
)

st.image("images/hs-issue2.png")

st.header(
    "While that was waiting I've tried getting emails at scale with Firecrawl and Claude, but that was beyond usability"
)

st.image("images/claude-output.png")
st.text("https://claude.ai/share/9519fc81-7273-4556-80d7-127ecede42db")


st.header("Great demo so far Ali, not a single issue! What's next?")

case_df = pd.DataFrame(CASE)
case_df.insert(0, "company_id", [f"C{i:02d}" for i in range(1, len(case_df) + 1)])

# Company table: one row per organization, keyed by company_id
companies_df = case_df[["company_id", "org", "status", "taxonomy", "primary_address"]]

# Officials table: one row per official role, linked to its company via company_id
officials_df = case_df[["official", "official_title", "official_phone", "company_id"]]

companies_col, officials_col = st.columns(2)
with companies_col:
    st.subheader("Companies")
    st.dataframe(companies_df, hide_index=True)
with officials_col:
    st.subheader("Officials")
    st.dataframe(officials_df, hide_index=True)


st.text("")
st.image("images/import-export structure.png")


st.header(
    "Now we can import data to Hubspot correctly, and we should replicate this approach to ensure maximum usability of the data."
)

st.divider()

st.header("Final Thoughts")
st.text(
    "I was expecting more from myself in this business section because we already have a data and imaginary case about why they might be interested in YouShift's offering. "
)

st.text(
    "I think go-to-market is unique in it's way for every company, but tools, approach, handling data and generating a pipeline are the main tasks we handle around gtm."
)

st.text(
    "Whether it's events, cold calls or in-person/virtual meetings, with correct use case and right data, playbooks can scale. And hey, that's one of the task to getting to PMF"
)

st.text("Thank you for your time and good luck!")
