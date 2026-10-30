import inspect

import pandas as pd
import requests
import streamlit as st

NPI_API = "https://npiregistry.cms.hhs.gov/api/"

st.header("Case: Anesthesiology firms, operated in multi-state")

# Thought process
st.markdown(
    """
Hey Jota. I was going through the NPPES NPI Registry while chatting with Claude. 
While I was going through the data, I've find out some orgs have multiple addresses, some even in multiple states.

I thought this could be a signal for a healthcare organization that is scaled beyond their geography. Although I'm an outsider to the industry and practice, not sure if that's the reality for all of the cases.
"""
)
st.divider()
st.header("Why this might be valuable for Youshift:")
st.markdown(
    """
I think this case simply shows scale. Operators, managers and 3rd ICP as healthcare execs,
(sometimes owner-operators) could benefit from what YouShift is offering; 

Workforce scheduling for managers, shift swaps between clinicians and financial high-level reports for execs.

"""
)


st.divider()

st.header("To-do list")
st.image(image="images/todo.png")

st.divider()

st.header("Basic API call")


def flatten(obj, prefix=""):
    """Nested dicts/lists -> flat columns like `addresses.1.state`."""
    if isinstance(obj, dict):
        items = obj.items()
    elif isinstance(obj, list):
        items = enumerate(obj)
    else:
        return {prefix: obj}
    out = {}
    for k, v in items:
        out.update(flatten(v, f"{prefix}.{k}" if prefix else str(k)))
    return out


def fetch_npi():
    r = requests.get(
        NPI_API,
        params={
            "version": "2.1",
            "enumeration_type": "NPI-2",
            "taxonomy_description": "Anesthesiology",
            "state": "TX",
            "limit": 2,
        },
        timeout=30,
    )
    r.raise_for_status()
    st.session_state.npi_data = r.json()


st.code(
    f'NPI_API = "{NPI_API}"\n\n' + inspect.getsource(fetch_npi),
    language="python",
)

st.button("Call NPI API", on_click=fetch_npi)

if "npi_data" in st.session_state:
    st.json(st.session_state.npi_data)
    results = st.session_state.npi_data["results"]
    st.dataframe(pd.DataFrame([flatten(x) for x in results]))

st.divider()

st.header("Data Structure")
st.image(image="images/data-structure-api.png")

st.divider()
st.header("Case")

st.text(
    "Organizations in TX, has Anesthesia in their taxonomy, has multiple locations and states are different."
)


def fetch_case():
    results = []
    for skip in [0, 200, 400, 600, 800, 1000]:
        r = requests.get(
            NPI_API,
            params={
                "version": "2.1",
                "enumeration_type": "NPI-2",
                "taxonomy_description": "Anesthesiology",
                "state": "TX",
                "limit": 200,
                "skip": skip,
            },
            timeout=30,
        )
        r.raise_for_status()
        results += r.json()["results"]

    rows = []
    for x in results:
        b = x["basic"]
        primary = next(a for a in x["addresses"] if a["address_purpose"] == "LOCATION")
        taxonomy = next(t for t in x["taxonomies"] if t["primary"])
        if "Anesthesiology" not in (taxonomy.get("desc") or ""):
            continue
        for secondary in x["practiceLocations"]:
            if secondary["state"] != primary["state"]:
                rows.append(
                    {
                        "org": b.get("organization_name"),
                        "status": b.get("status"),
                        "taxonomy": taxonomy.get("desc"),
                        "official": f"{b.get('authorized_official_first_name')} {b.get('authorized_official_last_name')}",
                        "official_title": b.get(
                            "authorized_official_title_or_position"
                        ),
                        "official_phone": b.get("authorized_official_telephone_number"),
                        "primary_address": f"{primary['address_1']}, {primary['city']}, {primary['state']}",
                        "secondary_address": f"{secondary['address_1']}, {secondary['city']}, {secondary['state']}",
                    }
                )
    st.session_state.case_rows = rows


st.code(inspect.getsource(fetch_case), language="python")

st.button("Run case", on_click=fetch_case)

if "case_rows" in st.session_state:
    st.dataframe(pd.DataFrame(st.session_state.case_rows))

    st.subheader("Deduplicated")
    df = pd.DataFrame(st.session_state.case_rows)
    dedup = df.drop(columns="secondary_address").drop_duplicates()
    st.dataframe(dedup)

    st.download_button("Export CSV", dedup.to_csv(index=False), "case.csv", "text/csv")
    st.download_button(
        "Export TXT", dedup.to_csv(index=False, sep="\t"), "case.txt", "text/plain"
    )

st.divider()

st.text(
    "Based on this data we can structure a go-to-market approach in the business section.",
)
st.text(
    "Also Claude did the heavy lifting mostly with few changes. Can't say I could replicate the program line by line with hand."
)
st.text("Not the most cracked programmer out there.")

st.image(
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.zenfs.com%2Fen%2Fmiami_herald_mcclatchy_975%2F88041bec3eb4d7c57c7af6a7fa392a6c&f=1&nofb=1&ipt=1cd7a3d7dfe7a7521941a51a74a86c4f90c7602daef8846ddeda573cfa8cf635&ipo=images"
)
