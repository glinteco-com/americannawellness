# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=

# Version of Elastic products
STACK_VERSION=8.15.3

# Set the cluster name
CLUSTER_NAME=docker-cluster

# Port to expose Elasticsearch HTTP API to the host
ES_PORT=127.0.0.1:9200

# Increase or decrease based on the available host memory (in bytes)
MEM_LIMIT=1073741824

# Project namespace (defaults to the current folder name if not set)
#COMPOSE_PROJECT_NAME=myproject