import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Retro Chat",
    page_icon="🕹️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Enhanced styling with inline CSS - no external files needed
st.markdown("""
<style>
/* Base Styling */
body {
    background-color: #120458;
    background-image: linear-gradient(180deg, #120458 0%, #000000 100%);
    color: #fff;
    font-family: monospace;
}

/* CRT Screen Effect */
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
    background-size: 100% 2px, 3px 100%;
    pointer-events: none;
    z-index: 999;
}

/* Neon Text */
.neon-text {
    color: #fff;
    text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #0073e6, 0 0 20px #0073e6, 0 0 25px #0073e6, 0 0 30px #0073e6, 0 0 35px #0073e6;
}

.hot-pink-text {
    color: #ff00c1;
    text-shadow: 0 0 5px #ff00c1, 0 0 10px #ff00c1, 0 0 15px #ff00c1, 0 0 20px #ff00c1;
}

.cyan-text {
    color: #00fff9;
    text-shadow: 0 0 5px #00fff9, 0 0 10px #00fff9, 0 0 15px #00fff9, 0 0 20px #00fff9;
}

.lime-text {
    color: #adff2f;
    text-shadow: 0 0 5px #adff2f, 0 0 10px #adff2f, 0 0 15px #adff2f, 0 0 20px #adff2f;
}

/* Retro Header */
h1 {
    font-size: 3rem;
    background: linear-gradient(90deg, #ff00c1, #00fff9, #adff2f);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 0.75rem #ff00c1);
    margin: 1rem 0;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 2px;
}

h2 {
    text-transform: uppercase;
    letter-spacing: 2px;
    text-align: center;
}

/* Button Styles */
.stButton button {
    background: black !important;
    color: #00fff9 !important;
    border: 3px solid #00fff9 !important;
    border-radius: 0 !important;
    box-shadow: 0 0 5px #00fff9, 0 0 10px #00fff9 !important;
    padding: 10px 24px !important;
    transition: all 0.3s !important;
    text-transform: uppercase !important;
    margin: 10px 0 !important;
}

.stButton button:hover {
    background: #00fff9 !important;
    color: black !important;
    box-shadow: 0 0 10px #00fff9, 0 0 20px #00fff9, 0 0 30px #00fff9 !important;
    transform: scale(1.05) !important;
}

/* Input Fields */
div[data-baseweb="input"] {
    background: #000 !important;
    border: 2px solid #ff00c1 !important;
    box-shadow: 0 0 5px #ff00c1 !important;
}

input[type="text"] {
    color: #adff2f !important;
    font-size: 18px !important;
}

/* Room Code Display */
.room-code {
    letter-spacing: 5px;
    font-size: 2rem;
    color: #adff2f;
    text-shadow: 0 0 5px #adff2f, 0 0 10px #adff2f;
    background-color: rgba(0, 0, 0, 0.8);
    padding: 15px;
    border: 3px solid #adff2f;
    text-align: center;
    margin: 20px 0;
}

/* Footer */
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgba(0,0,0,0.7);
    padding: 5px;
    border-top: 2px solid #ff00c1;
    text-align: center;
    font-size: 14px;
    color: #adff2f;
}
</style>
""", unsafe_allow_html=True)

# Create footer
st.markdown(
    """
    <div class="footer">
        RETRO-CHAT v1.0 | © 2025 | PRESS ESC TO EXIT
    </div>
    """,
    unsafe_allow_html=True
)

def home_page():
    """Home page with options to host or join"""
    # Title
    st.markdown("<h1>RETRO CHAT</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align: center; color: #00fff9; font-size: 1.5rem; letter-spacing: 2px;">
            A BLAST FROM THE PAST
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Description
    st.markdown(
        """
        <div style="text-align: center; margin: 30px 0;">
            <p style="font-size: 1.2rem; color: #adff2f;">
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
                <h2 style="color: #00fff9; text-shadow: 0 0 10px #00fff9;">CHOOSE YOUR PATH</h2>
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

def host_chatroom():
    """Host a new chatroom interface"""
    st.markdown("<h1>HOST A CHATROOM</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align: center; color: #00fff9; font-size: 1.2rem; letter-spacing: 1px;">
            Create your own retro chat space
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Input fields for chatroom name and host username
    st.markdown('<p class="cyan-text" style="margin-top: 30px;">ENTER CHATROOM INFO:</p>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            room_name = st.text_input("ROOM NAME", key="room_name", placeholder="MY RADICAL CHATROOM")
        with col2:
            host_name = st.text_input("YOUR NAME", key="host_name", placeholder="NEON_RIDER")
    
    # Create chatroom button
    if st.button("CREATE CHATROOM", key="create_room_btn"):
        if not room_name or not host_name:
            st.error("Please enter both room name and your name")
            return
        
        with st.spinner(""):
            # Show retro loading animation
            st.markdown(
                """
                <div style="text-align: center;">
                    <p class="hot-pink-text">INITIALIZING CHATROOM</p>
                    <div style="color: #00fff9;">
                        <span style="animation: glitch 1s infinite;">CONNECTING</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Generate a random 5-digit code
            room_code = str(random.randint(10000, 99999))
            
            # Store chatroom info in session state
            st.session_state.room_code = room_code
            st.session_state.username = host_name
            st.session_state.room_name = room_name
            st.session_state.is_host = True
            st.session_state.page = "chat"
            
            st.experimental_rerun()
    
    # Back button
    if st.button("BACK", key="back_btn"):
        st.session_state.page = "home"
        st.experimental_rerun()

def join_chatroom():
    """Interface for joining an existing chatroom"""
    st.markdown("<h1>JOIN A CHATROOM</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align: center; color: #00fff9; font-size: 1.2rem; letter-spacing: 1px;">
            Enter the access code
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Input fields for room code and username
    st.markdown('<p class="cyan-text" style="margin-top: 30px;">ENTER ACCESS CREDENTIALS:</p>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            room_code = st.text_input("ROOM CODE", key="join_room_code", placeholder="12345")
        with col2:
            username = st.text_input("YOUR NAME", key="join_username", placeholder="PIXEL_PUNK")
    
    # Join button
    if st.button("JOIN CHATROOM", key="join_room_btn"):
        if not room_code or not username:
            st.error("Please enter both room code and your name")
            return
        
        # For demonstration, we'll just simulate a successful join
        # In the full app, you'd validate the code with Supabase
        
        # Store info in session state
        st.session_state.room_code = room_code
        st.session_state.username = username
        st.session_state.room_name = "DEMO ROOM"  # This would come from DB lookup
        st.session_state.is_host = False
        st.session_state.page = "chat"
        
        st.experimental_rerun()
    
    # Back button
    if st.button("BACK", key="back_btn_join"):
        st.session_state.page = "home"
        st.experimental_rerun()

def chat_interface():
    """Basic chat interface mockup"""
    # Display chat header
    room_name = st.session_state.room_name
    username = st.session_state.username
    is_host = st.session_state.get("is_host", False)
    
    header_suffix = " (HOST)" if is_host else ""
    st.markdown(f"<h1>CHATROOM: {room_name}</h1>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <p style="text-align: center; color: #00fff9; font-size: 1.2rem;">
            Logged in as: <span class="hot-pink-text">{username}{header_suffix}</span>
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # If host, display the room code for sharing
    if is_host:
        st.markdown(
            f"""
            <div class="room-code">{st.session_state.room_code}</div>
            <p class="lime-text" style="text-align: center;">SHARE THIS CODE WITH OTHERS TO JOIN</p>
            """, 
            unsafe_allow_html=True
        )
    
    # Simple chat display
    st.markdown(
        """
        <div style="background-color: rgba(0, 0, 0, 0.7); border: 3px solid #ff00c1; border-radius: 0; 
                    box-shadow: 0 0 10px #ff00c1; padding: 20px; margin: 20px 0; height: 300px; overflow-y: auto;">
            <div style="color: #adff2f; margin-bottom: 10px; text-align: center;">
                Messages will appear here in the full version
            </div>
            <div style="color: #00fff9; margin-bottom: 10px; text-align: center;">
                This is a placeholder chat interface
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Message input
    message = st.text_input("", key="message_input", placeholder="TYPE YOUR MESSAGE HERE...")
    
    if message:
        st.success(f"Message sent! In the full version, this would be saved to the database.")
        st.session_state.message_input = ""
    
    # Exit button
    if st.button("EXIT CHATROOM", key="exit_btn"):
        # Clear chatroom data from session
        if "room_id" in st.session_state:
            del st.session_state.room_id
        if "room_name" in st.session_state:
            del st.session_state.room_name
        if "room_code" in st.session_state:
            del st.session_state.room_code
        if "username" in st.session_state:
            del st.session_state.username
        if "is_host" in st.session_state:
            del st.session_state.is_host
        
        st.session_state.page = "home"
        st.experimental_rerun()

# Main application logic
def main():
    # Handle different pages
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "host":
        host_chatroom()
    elif st.session_state.page == "join":
        join_chatroom()
    elif st.session_state.page == "chat":
        chat_interface()

# Run the main application
if __name__ == "__main__":
    main()
