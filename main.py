from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

# Route pour ton UniStore
@app.route("/ctgp7creator.unistore")
def unistore():
    store = {
        "storeInfo": {
            "title": "CTGP-7 Creator Shop",
            "author": "TonPseudo",
            "description": "Custom characters and skins"
        },
        "apps": [
            {
                "title": "CTGP-7 Character Pack",
                "author": "TonPseudo",
                "description": "Custom characters for Mario Kart 7",
                "version": "1.0",
                "category": "game",
                "systems": ["3DS"],
                "icon": "icon.png",
                "downloads": [
                    {
                        "type": "archive",
                        "url": "http://tonserveur.com/files/skinpack.chpack",
                        "output": "sdmc:/luma/titles/0004000000030800/"
                    }
                ]
            }
        ]
    }
    return jsonify(store)

# Route pour l’icône
@app.route("/icon.png")
def icon():
    return send_from_directory("static", "icon.png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)