from dash import Dash, dcc, dash_table, html, Input, Output, State, Patch, clientside_callback
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

# Clientside callback for loading screen on page navigation
app.clientside_callback(
    """
    function(pathname) {
        const loadingScreen = document.querySelector('.loading-screen');
        if (loadingScreen) {
            // Show loading screen
            loadingScreen.classList.add('show');
            
            // Hide after 400ms (page transition time)
            setTimeout(function() {
                loadingScreen.classList.remove('show');
            }, 400);
        }
        return window.location.pathname;
    }
    """,
    Output('_js_output', 'children'),
    Input('url', 'pathname'),
    prevent_initial_call=True
)

# Toggle between sign in and sign up
@app.callback(
    [
        Output('auth-title', 'children'),
        Output('auth-subtitle', 'children'),
        Output('confirm-password-section', 'style'),
        Output('auth-submit-btn', 'children'),
        Output('toggle-signup-btn', 'children'),
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
            "Sign In"
        )
    else:
        # Switch to sign in
        return (
            "Welcome Back",
            "Sign in to your account to continue",
            {"display": "none"},
            "Sign In",
            "Sign Up"
        )

# Handle authentication
@app.callback(
    [
        Output('user-session-store', 'data'),
        Output('auth-error', 'children'),
        Output('auth-error', 'style'),
        Output('url', 'pathname'),
    ],
    Input('auth-submit-btn', 'n_clicks'),
    [
        State('auth-email', 'value'),
        State('auth-password', 'value'),
        State('auth-confirm-password', 'value'),
        State('auth-submit-btn', 'children'),
        State('user-session-store', 'data'),
    ],
    prevent_initial_call=True
)
def authenticate_user(n_clicks, email, password, confirm_password, submit_text, session_data):
    if not email or not password:
        return (
            session_data,
            "Please fill in all fields",
            {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
            None
        )
    
    # Sign up validation
    if submit_text == "Create Account":
        if not confirm_password:
            return (
                session_data,
                "Please confirm your password",
                {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
                None
            )
        if password != confirm_password:
            return (
                session_data,
                "Passwords do not match",
                {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
                None
            )
        if len(password) < 6:
            return (
                session_data,
                "Password must be at least 6 characters",
                {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
                None
            )
    
    # For demo: accept any valid input (in production, validate against database)
    if len(password) < 3:
        return (
            session_data,
            "Password too short",
            {"color": "#dc2626", "fontSize": "0.875rem", "marginBottom": "1rem", "display": "block"},
            None
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
        "/"  # Redirect to home
    )

