from .render_views import render_views

def serve_views(app):
    render_views(app)

__all__ = ["serve_views"]