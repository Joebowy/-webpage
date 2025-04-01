import streamlit as st

import streamlit as st

# Title
st.header("My Documents")

# List of PDFs
pdfs = {
    "Curriculum Vitae": "image/curriculum_vitae.pdf",
    "Bachelor Certificate": "image/Bachelor.pdf"

}

# Displaying pdfs document in my webpage
for name, path in pdfs.items():
    st.write(f"**{name}**")
    with open(path, "rb") as file:
        st.download_button(label="Download", data=file, file_name=path)







