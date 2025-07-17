# Pour Vite ou CRA
FROM node:current-alpine3.22

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build || echo "build skipped (en dev)"
EXPOSE 5173

CMD ["npm", "run", "dev"]
