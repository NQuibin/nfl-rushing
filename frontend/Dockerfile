FROM node:14.8.0-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json /frontend/package.json

RUN yarn install
RUN yarn global add @vue/cli

EXPOSE 8080

CMD ["yarn", "serve"]
