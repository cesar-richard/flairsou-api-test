from rest_framework import serializers
from oauthlib.oauth2 import WebApplicationClient

from flairsou.config import OAUTH_SETTINGS


class AuthorizationLink:
    """
    Classe dédiée à la génération du lien d'autorisation pour demander
    à l'utilisateur d'accepter le partage des données avec l'application
    """

    def __init__(self):
        # création du client oauth avec l'ID du client
        client = WebApplicationClient(OAUTH_SETTINGS['client_id'])

        # construction de la requête d'autorisation oauth
        url = client.prepare_request_uri(
            OAUTH_SETTINGS['authorization_url'],
            redirect_uri=OAUTH_SETTINGS['redirect_uri'],
            scope=OAUTH_SETTINGS['scopes'])

        # enregistrement du lien
        self.link = url


class AuthorizationLinkSerializer(serializers.Serializer):
    """
    Serializer pour AuthorizationLink
    """
    link = serializers.CharField()
