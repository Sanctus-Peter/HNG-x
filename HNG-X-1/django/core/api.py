from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InfoResponseSerializer


class InfoResponseView(APIView):
    @staticmethod
    def get(request):
        # Retrieve query parameter
        slack_name = request.query_params.get('slack_name')
        track = request.query_params.get('track')

        # Current day and time
        current_day = datetime.now().strftime("%A")
        utc_time = datetime.utcnow()

        # GitHub URLs
        github_file_url = "https://github.com/Sanctus-Peter/HNG-x/blob/main/HNG-X-1/django/core/api.py"
        github_repo_url = "https://github.com/Sanctus-Peter/HNG-x/tree/main/HNG-X-1/"

        res_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200,
        }

        serializer = InfoResponseSerializer(data=res_data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
