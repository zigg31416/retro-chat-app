import streamlit as st
from components.host import host_chatroom
from components.join import join_chatroom, waiting_room
from components.chat import chat_interface
from utils.ui_elements import inject_custom_css, add_glitch_effect, create_retro_footer

# Set page config
st.set_page_config(
    page_title="Retro Chat",
    page_icon="🕹️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS
inject_custom_css()

# Add retro effects
add_glitch_effect()
create_retro_footer()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Main application
def main():
    # Handle different pages
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "host":
        host_chatroom()
    elif st.session_state.page == "join":
        join_chatroom()
    elif st.session_state.page == "waiting":
        waiting_room()
    elif st.session_state.page == "chat":
        chat_interface()

def home_page():
    """Home page with options to host or join"""
    # Title
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <h1 class="neon-text" style="font-size: 3rem;">RETRO CHAT</h1>
            <p class="cyan-text" style="font-family: 'VT323', monospace; font-size: 1.5rem;">
                A BLAST FROM THE PAST
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Description
    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <p style="font-family: 'VT323', monospace; font-size: 1.2rem; color: #adff2f;">
                Create or join a retro-styled temporary chatroom with your friends.
                <br>No accounts, no history, just pure nostalgic vibes.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Options
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(
            """
            <div style="background-color: rgba(0, 0, 0, 0.7); border: 3px solid #ff00c1; padding: 30px; margin: 20px 0; box-shadow: 0 0 15px #ff00c1;">
                <h2 style="font-family: 'Press Start 2P', cursive; color: #00fff9; text-align: center; margin-bottom: 30px; text-shadow: 0 0 10px #00fff9;">CHOOSE YOUR PATH</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("HOST CHATROOM", key="host_btn"):
                st.session_state.page = "host"
                st.experimental_rerun()
        
        with col_b:
            if st.button("JOIN CHATROOM", key="join_btn"):
                st.session_state.page = "join"
                st.experimental_rerun()
        
        # Credits
        st.markdown(
            """
            <div style="text-align: center; margin-top: 50px; font-family: 'VT323', monospace; font-size: 0.8rem; color: rgba(255,255,255,0.6);">
                Built with Streamlit and Supabase
            </div>
            """, 
            unsafe_allow_html=True
        )

# Run the main application
if __name__ == "__main__":
    main()
