import graphene
import graphql_jwt

class ObtainJSONWebToken(graphql_jwt.ObtainJSONWebToken):
    pass

class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()  # Login mutation
