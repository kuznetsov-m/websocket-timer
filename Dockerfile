FROM python:3.8.13-buster

RUN adduser user

WORKDIR /home/websocket_timer

############################
# poetry
# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker

ENV POETRY_VERSION=1.1.13

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /home/websocket_timer/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
############################
# project files

COPY app app
COPY migrations migrations
COPY websocket_timer.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP websocket_timer.py

RUN chown -R user:user ./

############################

USER user

EXPOSE 5000

CMD [ "./boot.sh" ]