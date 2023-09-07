# HNG X-1
## Backend Track - Task 1

This is a simple example of creating an API endpoint using FastAPI and django that fulfills the given requirements. The endpoint takes two GET request query parameters (`slack_name` and `track`) and returns specific information in JSON format.

## Requirements

The following information is included in the JSON response:

- Slack name
- Current day of the week
- Current UTC time (accurate within +/-2 minutes)
- Track
- GitHub file URL (specific file being executed)
- GitHub repo URL (link to the main GitHub repository)
- Status code (200 as an integer)

## Dependencies
- FastAPI
    - fastapi
    - uvicorn
    - pydantic
  
- django
    - django
    - djangorestframework

## Example Usage 
E.g.: http://example.com/api?slack_name=example_name&track=backend.

## Response Format
```
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  
}
```

## Framework Used
- [FastAPI](fastapi)
- [django](django)