# Stage 1: Build Stage
FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY main.go ./
RUN go build -o server main.go

# Stage 2: Production Final Stage
FROM alpine:latest

WORKDIR /app

# Copy only the compiled binary from builder stage
COPY --from=builder /app/server ./

EXPOSE 8080

CMD ["./server"]
