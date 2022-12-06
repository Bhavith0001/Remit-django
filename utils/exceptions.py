from rest_framework.response import Response
from rest_framework.status import HTTP_417_EXPECTATION_FAILED

def ResponseException(msg):
        return Response({'exception': f'{msg}'}, status=HTTP_417_EXPECTATION_FAILED)