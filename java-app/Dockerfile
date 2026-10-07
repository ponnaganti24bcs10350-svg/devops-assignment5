FROM eclipse-temurin:17-jdk AS builder

WORKDIR /app
COPY App.java ./
RUN javac App.java

FROM eclipse-temurin:17-jre

WORKDIR /app
COPY --from=builder /app/App*.class ./

EXPOSE 8080

CMD ["java", "App"]
