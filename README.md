# ResNet18 API Deployment

This project provides an API for deploying the ResNet18 model, facilitating image classification tasks through a web service.

## Features

- **ResNet18 Integration**: Utilizes the ResNet18 architecture for image classification.
- **API Endpoints**: Offers endpoints to submit images and receive classification results.
- **Docker Support**: Contains a `Dockerfile` for containerized deployment.

## Getting Started

### Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Docker**: For containerized deployment, install Docker.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ronaldnetawat/resnet-api.git
   cd resnet-api
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the API**:

   ```bash
   python app.py
   ```

2. **Access the API**:

   Navigate to `http://localhost:5000` in your browser or use tools like `curl` or Postman to interact with the endpoints.

### Docker Deployment

1. **Build the Docker Image**:

   ```bash
   docker build -t resnet-api .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -p 5000:5000 resnet-api
   ```

## Repository Structure

- `app.py`: Main application file containing the API logic.
- `requirements.txt`: Lists the Python dependencies.
- `Dockerfile`: Instructions to build the Docker image.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.