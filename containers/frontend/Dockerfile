FROM debian:bookworm

SHELL ["/bin/bash", "-c"]
WORKDIR /app

RUN apt-get update && apt-get -y install nodejs git npm curl xsel
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
RUN /bin/bash -c "source /root/.bashrc && nvm install 17.9.1 && npm install --location=global npm@8.11.0"

RUN git clone https://github.com/The-Alpha-Project/Alpha-archives-website

WORKDIR /app/Alpha-archives-website/frontend

RUN npm install --force && npm run build && npm install -g serve
COPY configs/api.tsx /app/Alpha-archives-website/frontend/src/config

ENTRYPOINT ["/bin/bash", "-c", "source /root/.bashrc && serve -s build"]
# ENTRYPOINT ["/bin/bash", "-c", "source /root/.bashrc && npm start"]