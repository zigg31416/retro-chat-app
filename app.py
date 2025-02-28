import streamlit as st

# Set page config
st.set_page_config(
    page_title="Retro Chat",
    page_icon="🕹️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add basic inline styling instead of loading external CSS
st.markdown("""
<style>
body {
    background-color: #120458;
    color: #ffffff;
    font-family: monospace;
}
h1 {
    color: #ff00c1;
    text-shadow: 0 0 5px #ff00c1, 0 0 10px #ff00c1;
    font-size: 3rem;
    text-align: center;
}
.button {
    background-color: black;
    color: #00fff9;
    border: 3px solid #00fff9;
    padding: 10px 24px;
    text-align: center;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    box-shadow: 0 0 5px #00fff9;
}
</style>
""", unsafe_allow_html=True)

def main():
    # Title
    st.markdown("<h1>RETRO CHAT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00fff9; font-size: 1.5rem;'>A BLAST FROM THE PAST</p>", unsafe_allow_html=True)
    
    # Description
    st.markdown("<p style='text-align: center; color: #adff2f; font-size: 1.2rem;'>Create or join a retro-styled temporary chatroom.</p>", unsafe_allow_html=True)
    
    # Options
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div style='background-color: rgba(0, 0, 0, 0.7); border: 3px solid #ff00c1; padding: 30px; margin: 20px 0; box-shadow: 0 0 15px #ff00c1;'><h2 style='color: #00fff9; text-align: center;'>CHOOSE YOUR PATH</h2></div>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("HOST CHATROOM", key="host_btn"):
                st.session_state.page = "host"
                st.experimental_rerun()
        
        with col_b:
            if st.button("JOIN CHATROOM", key="join_btn"):
                st.session_state.page = "join"
                st.experimental_rerun()

# Run the main application
if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    # Simple page routing
    if st.session_state.page == "home":
        main()
    elif st.session_state.page == "host":
        st.title("Host Chatroom")
        st.write("This is the host page (simplified)")
        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.experimental_rerun()
    elif st.session_state.page == "join":
        st.title("Join Chatroom")
        st.write("This is the join page (simplified)")
        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.experimental_rerun()
