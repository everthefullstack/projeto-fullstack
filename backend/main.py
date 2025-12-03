from app.create_app import create_app


app = create_app()

"""if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
"""

#docker-compose -f docker-compose-projeto-fullstack.yml up --build -d
#docker-compose -f docker-compose-workspace.yml down