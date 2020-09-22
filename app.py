import streamlit as st
from execbox_side import execbox_side

st.beta_set_page_config(layout="wide")

execbox_side("""
import streamlit as st

CAT_IMAGE = "https://images.unsplash.com/photo-1552933529-e359b2477252?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=950&q=80"
DOG_IMAGE = "https://images.unsplash.com/photo-1534361960057-19889db9621e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
RABBIT_IMAGE = "https://images.unsplash.com/photo-1580762410711-aa47eb8872d7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"


# Let's lay out our page!
top = st.beta_container()
c1, c2, c3 = st.beta_columns(3)

# Now use a column, just like st.sidebar...
c1.header("First column")
c1.image(CAT_IMAGE, use_column_width=True)

# Or use the fancy new `with` notation!
with c2:
    st.header("Second column")
    st.image(DOG_IMAGE, use_column_width=True)
with c3:
    st.header("Third column")
    st.image(RABBIT_IMAGE, use_column_width=True)

# st.beta_container() is like st.empty() but for *multiple* things
with top:
    st.title("Layout Playground")
    st.write("*Edit my source code and I'll immediately update ========>*")
    
    # Finally, st.beta_expander() allows expanding and collapsing!
    with st.beta_expander("Featuring", expanded=True):
	    st.write(\"""
	    - `st.beta_container`: Write elements to an out-of-order block
	    - `st.beta_expander`: A container that users can expand/collapse
	    - `st.beta_columns`: Create multiple side-by-side containers
	    - `with container`: Syntax sugar!
	    \""")
""", autorun=True, line_numbers=True)