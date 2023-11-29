FROM mcr.microsoft.com/devcontainers/universal:2

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git wget gnupg software-properties-common

# Install the Azure Functions Core Tools
RUN wget -q https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y azure-functions-core-tools-3