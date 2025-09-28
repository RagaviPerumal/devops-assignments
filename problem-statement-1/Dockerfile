# Base image
FROM debian:bookworm-slim

# Install dependencies and fortunes database
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bash \
        netcat-openbsd \
        cowsay \
        fortune-mod \
        fortunes-min && \
    rm -rf /var/lib/apt/lists/*

# Add /usr/games to PATH
ENV PATH="/usr/games:${PATH}"

# Set working directory
WORKDIR /app

# Copy script and make executable
COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh

# Expose port
EXPOSE 4499

# Run the script
CMD ["/app/wisecow.sh"]
