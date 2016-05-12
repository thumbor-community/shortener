Use the Shortener
=================

1. To Generate a short url, send a POST to the shortener endpoint:
::
    curl -X POST http://localhost:8888/shortener/unsafe/300x200/http://www.waterfalls.hamilton.ca/images/Waterfall_Collage_home_sm1.jpg

This returns a JSON response with a key:
::
    HTTP/1.1 200 OK
    Date: Thu, 12 May 2016 05:19:42 GMT
    Content-Length: 75
    Content-Type: application/json
    Server: TornadoServer/4.3

    {"key": "e529d3807fdb0b84a92a6e4fa0c7a707e7a77f1d98443ad07b0bdc0cfca621fb"}


2. To retrieve the thumbnail, make a GET request (in your browser or link tag)
to the shortener endpoint with the key:
::
  http://localhost:8888/shortener/e529d3807fdb0b84a92a6e4fa0c7a707e7a77f1d98443ad07b0bdc0cfca621fb
