from .render_views import render_views

def register_views(app):
    render_views(app)

__all__ = ["register_views"]