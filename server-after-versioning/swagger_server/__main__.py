#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Calculates minimum path between points depending on user generated map input.'})
    app.run(host="ec2-54-200-185-55.us-west-2.compute.amazonaws.com", port=8081)
