from dash import Dash, dcc, dash_table, html, Input, Output, State, Patch, clientside_callback, exceptions
from app import app
import plotly.graph_objects as go
import plotly.express as px
import data
from data import final_data
import json
from datetime import datetime

# Clientside callback for mobile menu toggle (runs in browser for better performance)
app.clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            const sidebar = document.querySelector('.sidebar');
            const overlay = document.querySelector('.sidebar-overlay');
            
            if (sidebar && overlay) {
                sidebar.classList.toggle('show');
                overlay.classList.toggle('show');
                
                // Close menu when overlay is clicked
                overlay.onclick = function() {
                    sidebar.classList.remove('show');
                    overlay.classList.remove('show');
                };
                
                // Close menu when any nav link is clicked
                const navLinks = document.querySelectorAll('.nav-link');
                navLinks.forEach(link => {
                    link.onclick = function() {
                        sidebar.classList.remove('show');
                        overlay.classList.remove('show');
                    };
                });
            }
        }
        return '';
    }
    """,
    Output('sidebar-overlay', 'children'),
    Input('mobile-menu-toggle', 'n_clicks')
)


# Toggle between sign in and sign up
@app.callback(
    [
        Output('auth-title', 'children'),
        Output('auth-subtitle', 'children'),
        Output('confirm-password-section', 'style'),
        Output('auth-submit-btn', 'children'),
        Output('toggle-signup-btn', 'children'),
        Output('auth-email', 'value'),
        Output('auth-password', 'value'),
        Output('auth-confirm-password', 'value'),
    ],
    Input('toggle-signup-btn', 'n_clicks'),
    State('toggle-signup-btn', 'children'),
    prevent_initial_call=True
)
def toggle_auth_mode(n_clicks, current_text):
    is_signup = current_text == "Sign In"
    
    if is_signup:
        # Switch to sign up
        return (
            "Create Account",
            "Sign up to get started",
            {"display": "block"},
            "Create Account",
            "Sign In",
            "",  # Clear email
            "",  # Clear password
            "",  # Clear confirm password
        )
    else:
        # Switch to sign in
        return (
            "Welcome Back",
            "Sign in to your account to continue",
            {"display": "none"},
            "Sign In",
            "Sign Up",
            "",  # Clear email
            "",  # Clear password
            "",  # Clear confirm password
        )

# Handle authentication
@app.callback(
    [
        Output('user-session-store', 'data'),
        Output('auth-error', 'children'),
        Output('auth-error', 'style'),
    ],
    Input('auth-submit-btn', 'n_clicks'),
    [
        State('auth-email', 'value'),
        State('auth-password', 'value'),
        State('auth-confirm-password', 'value'),
        State('auth-submit-btn', 'children'),
        State('user-session-store', 'data'),
    ],
    prevent_initial_call=False
)
def authenticate_user(n_clicks, email, password, confirm_password, submit_text, session_data):
    # Check if button was never clicked
    if not n_clicks or n_clicks == 0:
        raise exceptions.PreventUpdate
    
    if not email or not password:
        return (
            session_data,
            "Please fill in all fields",
            {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
        )
    
    # Sign up validation
    if submit_text == "Create Account":
        if not confirm_password:
            return (
                session_data,
                "Please confirm your password",
                {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
            )
        if password != confirm_password:
            return (
                session_data,
                "Passwords do not match",
                {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
            )
        if len(password) < 6:
            return (
                session_data,
                "Password must be at least 6 characters",
                {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
            )
    
    # For demo: accept any valid input (in production, validate against database)
    if len(password) < 3:
        return (
            session_data,
            "Password too short",
            {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
        )
    
    # Create session
    user_data = {
        "email": email,
        "login_time": datetime.now().isoformat(),
        "authenticated": True
    }
    
    return (
        user_data,
        "",
        {"display": "none"},
    )


