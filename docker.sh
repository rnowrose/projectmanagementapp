#!/bin/bash

# Docker management script for FastAPI project

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Show usage
show_usage() {
    echo "Usage: $0 {dev|prod|build|stop|clean|logs|shell}"
    echo ""
    echo "Commands:"
    echo "  dev     - Start development environment"
    echo "  prod    - Start production environment"
    echo "  build   - Build Docker images"
    echo "  stop    - Stop all containers"
    echo "  clean   - Stop containers and remove images"
    echo "  logs    - Show container logs"
    echo "  shell   - Open shell in API container"
    echo ""
}

# Development environment
start_dev() {
    print_status "Starting development environment..."
    docker-compose up --build -d
    print_status "Development environment started!"
    print_status "Project Management API: http://localhost:8000"
    print_status "Project Management Docs: http://localhost:8000/docs"
    print_status "PostGreSQL: localhost:5433"
}

# Production environment
start_prod() {
    print_status "Starting production environment..."
    docker-compose -f docker-compose.prod.yml up --build -d
    print_status "Production environment started!"
    print_status "APIs available at:"
    print_status "  - Project API: http://localhost/api/v1/projects/"
    print_status "  - Health Check: http://localhost/health"
}

# Build images
build_images() {
    print_status "Building Docker images..."
    docker-compose build
    docker-compose -f docker-compose.prod.yml build
    print_status "Images built successfully!"
}

# Stop containers
stop_containers() {
    print_status "Stopping containers..."
    docker-compose down
    docker-compose -f docker-compose.prod.yml down
    print_status "Containers stopped!"
}

# Clean up
clean_up() {
    print_status "Cleaning up containers and images..."
    docker-compose down --rmi all --volumes --remove-orphans
    docker-compose -f docker-compose.prod.yml down --rmi all --volumes --remove-orphans
    print_status "Cleanup completed!"
}

# Show logs
show_logs() {
    echo "Which environment logs? (dev/prod)"
    read -r env
    case $env in
        dev)
            docker-compose logs -f
            ;;
        prod)
            docker-compose -f docker-compose.prod.yml logs -f
            ;;
        *)
            print_error "Invalid choice. Use 'dev' or 'prod'"
            ;;
    esac
}

# Open shell
open_shell() {
    print_status "Opening shell in API container..."
    if docker-compose ps | grep -q "api.*Up"; then
        docker-compose exec api bash
    elif docker-compose -f docker-compose.prod.yml ps | grep -q "api.*Up"; then
        docker-compose -f docker-compose.prod.yml exec api bash
    else
        print_error "No running API container found. Start the environment first."
    fi
}

# Main script logic
case "$1" in
    dev)
        start_dev
        ;;
    prod)
        start_prod
        ;;
    build)
        build_images
        ;;
    stop)
        stop_containers
        ;;
    clean)
        clean_up
        ;;
    logs)
        show_logs
        ;;
    shell)
        open_shell
        ;;
    *)
        show_usage
        exit 1
        ;;
esac
