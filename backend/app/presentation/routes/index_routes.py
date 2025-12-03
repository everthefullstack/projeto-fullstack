from flask import Blueprint, Response


index_routes = Blueprint("index", __name__, url_prefix="/api/v1")

@index_routes.route(rule="/healthcheck", methods=["GET"])
def healthcheck():

    http_response = {"status": "ok"}

    return Response(response=http_response, status=200)