from dash import Dash, dcc, dash_table, html, Input, Output, State, Patch, clientside_callback
from app import app
import plotly.graph_objects as go
import plotly.express as px
import data
from data import final_data

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
            }
        }
        return '';
    }
    """,
    Output('sidebar-overlay', 'children'),
    Input('mobile-menu-toggle', 'n_clicks')
)

