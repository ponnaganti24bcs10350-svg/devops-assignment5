# ==========================================
# Stage 1: Build & Security Hardening
# ==========================================
FROM node:20-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# ==========================================
# Stage 2: Minimal Distroless/Alpine Runner
# ==========================================
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV PORT=8080

# Security: Dedicated system user with specific UID/GID
RUN addgroup -g 10001 -S secgroup && \
    adduser -u 10001 -S secuser -G secgroup

COPY --from=builder --chown=10001:10001 /app/node_modules ./node_modules
COPY --chown=10001:10001 src/ ./src/
COPY --chown=10001:10001 package.json ./

# Switch to non-root user
USER 10001

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1

CMD ["node", "src/app.js"]
