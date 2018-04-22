api_token = "eyJraWQiOiIwZTRjODM1NC0xNmRkLTRlYmYtODUxMy1hNThmM2JjYmM2OTIiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJjb20uaGRzLmZvdW5kcnkiLCJleHAiOjE1MTc4OTQ3OTIsImp0aSI6IjhTTXVKdVJlc2RCV0pTS2hFd3RZT0EiLCJpYXQiOjE1MTc4ODc1OTIsIm5iZiI6MTUxNzg4NzQ3Miwic3ViIjoiYWRtaW4iLCJyZWFsbSI6IkxvY2FsIiwidXVpZCI6IjU5YjlhZjY3LTYyYWItNDNhYy04N2RhLTMxNWUzMjg5Mzg2MSJ9.ZKF7Xt09L_nqOG0GAlS5hgxL2zVgnyDvfRmcJyFT6hL-tD_5Ixw4bxAtW092qJeHaB3PC3jNlcXDiwMUOqEWx5SpH7HemORLKTXFyJJFHsZ-M29-DeWsxoEu6RCdULVjgq_cQDhwqhSz17Z71_jcbvS9JDoRYt0V23y2Ci4uPquvJpZPRBpLsTI_ADhRFr7M9Rq_W7XtQboGNUyBec0-YlUyj6lfcHenUud7QLF4hP5uAanvOlJ8kWH-n8J-Tw7uRHu3BWEGqSrRKTL7iHu-_ka-PErxM9HY5WXH7UiOLvfa1QYI29tgc_6j99kc9zJQqseLc-Mh55JPMXg6wVadhg"
headers = {'Content-Type': 'application/json',
       'Authorization': 'Bearer {0}'.format(api_token)}

http_proxy = "http://10.78.0.111:8080"
https_proxy = "http://10.78.0.111:8080"

proxyDict = {
    "http": http_proxy,
    "https": https_proxy
}


