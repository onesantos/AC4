from flask import jsonify, Flask

def init_app(app: Flask):
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404
