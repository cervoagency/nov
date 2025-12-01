from dash import Dash, dcc, dash_table, html, Input, Output, State, Patch, clientside_callback, exceptions
from app import app
import plotly.graph_objects as go
import plotly.express as px
import data
from data import final_data
import json
from datetime import datetime
from users import user_exists, register_user, verify_user

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


# ============================================
# AUTHENTICATION CALLBACKS - Clean & Functional
# ============================================

# Toggle between Sign In and Sign Up mode
@app.callback(
    [
        Output('auth-title', 'children'),
        Output('auth-subtitle', 'children'),
        Output('confirm-password-section', 'style'),
        Output('auth-submit-btn', 'children'),
        Output('toggle-text', 'children'),
        Output('toggle-signup-btn', 'children'),
    ],
    Input('toggle-signup-btn', 'n_clicks'),
    State('toggle-signup-btn', 'children'),
    prevent_initial_call=True
)
def toggle_auth_mode(n_clicks, current_text):
    """Switch between Sign In and Sign Up forms"""
    is_switching_to_signup = (current_text == "Sign Up")

    if is_switching_to_signup:
        return (
            "Create Account",
            "Sign up to get started with Clarity",
            {"marginBottom": "1.5rem", "display": "block"},  # Show confirm password
            "Create Account",
            "Already have an account? ",
            "Sign In",
        )
    else:
        return (
            "Welcome Back",
            "Login or Sign up to continue",
            {"marginBottom": "1.5rem", "display": "none"},  # Hide confirm password
            "Sign In",
            "Don't have an account? ",
            "Sign Up",
        )


# Main authentication handler (Sign In / Sign Up)
@app.callback(
    [
        Output('user-session-store', 'data'),
        Output('auth-error', 'children'),
        Output('auth-error', 'style'),
        Output('auth-email', 'value'),
        Output('auth-password', 'value'),
        Output('auth-confirm-password', 'value'),
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
def handle_authentication(n_clicks, email, password, confirm_password, button_text, session_data):
    """Handle both Sign In and Sign Up logic"""

    # Basic validation
    if not email or not password:
        return (
            session_data,
            "⚠️ Please fill in all required fields",
            {
                "color": "#dc2626",
                "fontSize": "0.875rem",
                "marginBottom": "1rem",
                "padding": "0.75rem",
                "backgroundColor": "#fee2e2",
                "borderRadius": "0.5rem",
                "display": "block"
            },
            email or "",
            password or "",
            confirm_password or "",
        )

    # Clean email input
    email = email.strip().lower()

    # Validate email format
    if "@" not in email or "." not in email.split("@")[-1]:
        return (
            session_data,
            "⚠️ Please enter a valid email address",
            {
                "color": "#dc2626",
                "fontSize": "0.875rem",
                "marginBottom": "1rem",
                "padding": "0.75rem",
                "backgroundColor": "#fee2e2",
                "borderRadius": "0.5rem",
                "display": "block"
            },
            email,
            password,
            confirm_password or "",
        )

    # Validate password length
    if len(password) < 6:
        return (
            session_data,
            "⚠️ Password must be at least 6 characters long",
            {
                "color": "#dc2626",
                "fontSize": "0.875rem",
                "marginBottom": "1rem",
                "padding": "0.75rem",
                "backgroundColor": "#fee2e2",
                "borderRadius": "0.5rem",
                "display": "block"
            },
            email,
            password,
            confirm_password or "",
        )

    # SIGN UP LOGIC
    if button_text == "Create Account":
        # Validate confirm password
        if not confirm_password:
            return (
                session_data,
                "⚠️ Please confirm your password",
                {
                    "color": "#dc2626",
                    "fontSize": "0.875rem",
                    "marginBottom": "1rem",
                    "padding": "0.75rem",
                    "backgroundColor": "#fee2e2",
                    "borderRadius": "0.5rem",
                    "display": "block"
                },
                email,
                password,
                confirm_password or "",
            )

        if password != confirm_password:
            return (
                session_data,
                "⚠️ Passwords do not match",
                {
                    "color": "#dc2626",
                    "fontSize": "0.875rem",
                    "marginBottom": "1rem",
                    "padding": "0.75rem",
                    "backgroundColor": "#fee2e2",
                    "borderRadius": "0.5rem",
                    "display": "block"
                },
                email,
                password,
                confirm_password,
            )

        # Check if user already exists
        if user_exists(email):
            return (
                session_data,
                "⚠️ An account with this email already exists. Please sign in instead.",
                {
                    "color": "#dc2626",
                    "fontSize": "0.875rem",
                    "marginBottom": "1rem",
                    "padding": "0.75rem",
                    "backgroundColor": "#fee2e2",
                    "borderRadius": "0.5rem",
                    "display": "block"
                },
                email,
                "",  # Clear password for security
                "",
            )

        # Register new user
        success, message = register_user(email, password)

        if not success:
            return (
                session_data,
                f"⚠️ {message}",
                {
                    "color": "#dc2626",
                    "fontSize": "0.875rem",
                    "marginBottom": "1rem",
                    "padding": "0.75rem",
                    "backgroundColor": "#fee2e2",
                    "borderRadius": "0.5rem",
                    "display": "block"
                },
                email,
                password,
                confirm_password,
            )

        # Success! Create session
        user_data = {
            "email": email,
            "login_time": datetime.now().isoformat(),
            "authenticated": True
        }

        return (
            user_data,
            "",
            {"display": "none"},
            "",  # Clear all fields
            "",
            "",
        )

    # SIGN IN LOGIC
    else:
        # Verify credentials
        success, message = verify_user(email, password)

        if not success:
            return (
                session_data,
                f"⚠️ {message}",
                {
                    "color": "#dc2626",
                    "fontSize": "0.875rem",
                    "marginBottom": "1rem",
                    "padding": "0.75rem",
                    "backgroundColor": "#fee2e2",
                    "borderRadius": "0.5rem",
                    "display": "block"
                },
                email,
                "",  # Clear password for security
                "",
            )

        # Success! Create session
        user_data = {
            "email": email,
            "login_time": datetime.now().isoformat(),
            "authenticated": True
        }

        return (
            user_data,
            "",
            {"display": "none"},
            "",  # Clear all fields
            "",
            "",
        )


# Open/Close Reset Password Modal
@app.callback(
    Output('reset-modal', 'is_open'),
    [
        Input('reset-password-link', 'n_clicks'),
        Input('cancel-reset-btn', 'n_clicks'),
        Input('submit-reset-btn', 'n_clicks'),
    ],
    State('reset-modal', 'is_open'),
    prevent_initial_call=True
)
def toggle_reset_modal(link_clicks, cancel_clicks, submit_clicks, is_open):
    """Toggle the reset password modal"""
    return not is_open




# Handle Password Reset Submission
@app.callback(
    [
        Output('reset-modal', 'is_open', allow_duplicate=True),
        Output('reset-message', 'children'),
        Output('reset-message', 'style'),
        Output('reset-email', 'value'),
        Output('submit-reset-btn', 'children'),
        Output('submit-reset-btn', 'disabled'),
    ],
    Input('submit-reset-btn', 'n_clicks'),
    State('reset-email', 'value'),
    prevent_initial_call=True
)
def handle_password_reset(n_clicks, email):
    """Handle password reset request"""

    if not email:
        return (
            True,  # Keep modal open
            "⚠️ Please enter your email address",
            {
                "marginTop": "1rem",
                "fontSize": "0.875rem",
                "color": "#dc2626",
                "backgroundColor": "#fee2e2",
                "padding": "0.75rem",
                "borderRadius": "0.5rem",
                "display": "block"
            },
            "",
            "Send Reset Link",
            False,
        )

    email = email.strip().lower()

    # Validate email format
    if "@" not in email or "." not in email.split("@")[-1]:
        return (
            True,  # Keep modal open
            "⚠️ Please enter a valid email address",
            {
                "marginTop": "1rem",
                "fontSize": "0.875rem",
                "color": "#dc2626",
                "backgroundColor": "#fee2e2",
                "padding": "0.75rem",
                "borderRadius": "0.5rem",
                "display": "block"
            },
            email,
            "Send Reset Link",
            False,
        )

    # Success! Show success message and keep modal open
    return (
        True,  # Keep modal OPEN to show success message
        "✅ If an account exists with this email, reset instructions have been sent. You can close this window.",
        {
            "marginTop": "1rem",
            "fontSize": "0.875rem",
            "color": "#059669",
            "backgroundColor": "#d1fae5",
            "padding": "0.75rem",
            "borderRadius": "0.5rem",
            "display": "block",
            "lineHeight": "1.6"
        },
        "",  # Clear email field
        "✓ Sent",  # Change button text
        True,  # Disable button
    )


# Reset the modal state when opening
@app.callback(
    [
        Output('submit-reset-btn', 'children', allow_duplicate=True),
        Output('submit-reset-btn', 'disabled', allow_duplicate=True),
        Output('reset-message', 'children', allow_duplicate=True),
        Output('reset-message', 'style', allow_duplicate=True),
    ],
    Input('reset-password-link', 'n_clicks'),
    prevent_initial_call=True
)
def reset_modal_state(n_clicks):
    """Reset modal to initial state when opening"""
    return (
        "Send Reset Link",
        False,
        "",
        {"display": "none"}
    )

# ============================================
# LOGOUT CALLBACK
# ============================================

@app.callback(
    [
        Output('user-session-store', 'data', allow_duplicate=True),
        Output('url', 'pathname', allow_duplicate=True),
    ],
    Input('logout-btn', 'n_clicks'),
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    """Handle user logout"""
    print(f"🚪 User logged out")
    
    # Clear session data
    empty_session = {
        "authenticated": False,
        "email": None,
        "login_time": None
    }
    
    # Redirect to login page
    return (empty_session, "/ClarityApp/")