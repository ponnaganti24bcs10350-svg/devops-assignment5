# Multi-Stage Dockerfile for Final DevOps Enterprise Application
# Stage 1: Build & Dependencies
FROM node:20-alpine AS builder
WORKDIR /app

COPY application/package*.json ./
RUN npm ci --only=production

COPY application/src ./src

# Stage 2: Minimal Distroless / Hardened Runtime
FROM node:20-alpine AS runner
WORKDIR /app

# Security: Non-root user execution
USER node

# Copy only production artifacts
COPY --chown=node:node --from=builder /app/node_modules ./node_modules
COPY --chown=node:node --from=builder /app/src ./src
COPY --chown=node:node application/package.json ./

ENV NODE_ENV=production
ENV PORT=8080

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/healthz || exit 1

CMD ["node", "src/server.js"]
