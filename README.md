![Preview](https://user-images.githubusercontent.com/61391551/179115833-4a9a50c8-0031-4b48-ba3b-81a6133baca3.png)

# Websocket Timer ([chech it live](https://websocket-timer.herokuapp.com/))
Example Flask websocket project. Based on [Flask-SocketIO](https://flask-socketio.readthedocs.io/).

Flask server manage Timer with REST API requests (Start/Stop). Server emit timer events (timer value two times per sec) and send them via websockts to frontpage. Also, start/stop events are stored in a database (Postgres).

The application is packaged in a [docker image](https://hub.docker.com/r/kuznetsov1024/websocket_timer) and a [docker-compose](https://github.com/kuznetsov-m/websocket-timer/blob/master/docker-compose.yml) is prepared for deploying a service.

# Run
`gunicorn --bind=127.0.0.1:5000 --worker-class eventlet app:app`

# Links
- https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
- https://github.com/eventlet/eventlet/issues/702