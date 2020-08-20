import streamlit as st

with st.echo("below"):
    with st.sidebar:
        st.write("Markdown")
        "# magic"
    "And now I'm free!"

    c1, c2, c3 = st.beta_columns(3)
    c1.title("First column")
    with c2:
        "## Second column"
    c3.slider("Third column")