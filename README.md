![Preview](https://user-images.githubusercontent.com/61391551/179115833-4a9a50c8-0031-4b48-ba3b-81a6133baca3.png)

# Websocket Timer
Example Flask websocket project. Based on [Flask-SocketIO](flask-socketio.readthedocs.io).

Flask server manage Timer with REST API requests (Start/Stop). Server emit timer events (timer value two times per sec) and send them via websockts to frontpage. And also, start/stop events are stored in a database (Postgres).

The application is packaged in a [docker image](https://hub.docker.com/r/kuznetsov1024/websocket_timer) and a [docker-compose](https://github.com/kuznetsov-m/websocket-timer/blob/master/docker-compose.yml) is prepared for deploying a service.
