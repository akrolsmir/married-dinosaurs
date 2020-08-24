import streamlit as st

CAT_IMG = "https://images.unsplash.com/photo-1552933529-e359b2477252?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=950&q=80"
DOG_IMG = "https://images.unsplash.com/photo-1534361960057-19889db9621e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
RABBIT_IMG = "https://images.unsplash.com/photo-1580762410711-aa47eb8872d7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"


with st.echo("below"):
    # Let's lay out our page!
    top = st.container()
    c1, c2, c3 = st.columns(3)

    # Now use a column like st.sidebar...
    c1.header("First column")
    c1.image(CAT_IMG, use_column_width=True)

    # Or use the fancy new `with` notation!
    with c2:
        "## Second column"
        st.image(DOG_IMG, use_column_width=True)
    with c3:
        st.header("Third column")
        st.image(RABBIT_IMG, use_column_width=True)

    # st.container() is like st.empty() but for *multiple* things
    with top:
        st.title("Horizontal Layout Playground")
        "*Press 'e' to edit this page!*"
        """
        Featuring:
        - `st.container`: Write elements to an out-of-order block
        - `st.columns`: Create multiple side-by-side containers
        - `with`: Syntax sugar
        """