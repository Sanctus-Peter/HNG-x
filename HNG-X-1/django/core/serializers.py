from rest_framework import serializers


class InfoResponseSerializer(serializers.Serializer):
    # slack_name = serializers.CharField()
    # track = serializers.CharField()
    current_day = serializers.CharField()
    utc_time = serializers.DateTimeField()
    github_file_url = serializers.URLField()
    github_repo_url = serializers.URLField()
