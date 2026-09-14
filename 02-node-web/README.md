# 02-node-web

Servidor Express.js containerizado con Docker.

## Estructura

├── server.js        # Servidor Express
├── package.json     # Dependencias
├── Dockerfile       # Configuración Docker
├── .dockerignore    # Archivos excluidos del build
└── README.md        # Este archivo

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Mensaje con hostname y timestamp |
| GET | `/health` | Health check |

## Variables de entorno

| Variable | Por defecto | Descripción |
|----------|-------------|-------------|
| `PORT` | `3000` | Puerto del servidor |
| `SALUDO` | `¡Hola desde Node.js dentro de Docker!` | Mensaje personalizado |
| `HOSTNAME` | *(automático en Docker)* | ID del contenedor |

## Ejecutar

### Local
```bash
npm install
npm start
```

### Docker
```bash
docker build -t node-web-2 .
docker run -d -p 3001:3001 -e PORT=3001 --name puerto-3001 node-web-2
```

### Docker con variables
```bash
docker run -d -p 3012:3012 \
  -e SALUDO="Hola Napoleon" \
  -e HOSTNAME="nar" \
  -e PORT=3012 \
  --name puerto12 \
  node-web-2
```

## Probar

```bash
curl http://localhost:3001
curl http://localhost:3001/health
```

## Dockerfile

```dockerfile
FROM node:26.5.0-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY server.js .
EXPOSE 3000
USER node
CMD ["node", "server.js"]
```
