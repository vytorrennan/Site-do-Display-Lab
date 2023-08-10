from flask import Blueprint

from .views import home, displayCast, exterminandoDrogas, institucional, \
    sobre, projetos

bp = Blueprint("webui", __name__, template_folder="templates", \
               static_folder="static", static_url_path="/webui/static")

bp.add_url_rule("/", view_func=home)
bp.add_url_rule("/projetos", view_func=projetos)
bp.add_url_rule("/institucional", view_func=institucional)
bp.add_url_rule("/sobre", view_func=sobre)
bp.add_url_rule("/projetos/exterminandoDrogas", view_func=exterminandoDrogas)
bp.add_url_rule("/projetos/displayCast", view_func=displayCast)



def init_app(app):
    app.register_blueprint(bp)