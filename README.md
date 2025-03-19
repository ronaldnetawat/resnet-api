# ResNet18 API Deployment

An API deployment for the ResNet18 model, prociding image classification tasks through a web service.

## Features

- **ResNet18 Integration**: Uses the ResNet18 architecture for image classification.
- **API Endpoints**: Offers endpoints to submit images and receive classification results.
- **Docker Support**: Contains a `Dockerfile` for containerized deployment.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ronaldnetawat/resnet-api.git
   cd resnet-api
   ```

2. **Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the API**:

   ```bash
   python app.py
   ```

2. **Access the API**:

   Go to `http://localhost:5000` in your browser or use tools like `curl` or Postman.

### Docker deployment

1. **Build the Docker Image**:

   ```bash
   docker build -t resnet-api .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 5000:5000 resnet-api
   ```

## Main files

- `app.py`: Main application file containing the API logic.
- `requirements.txt`: Lists the Python dependencies.
- `Dockerfile`: Instructions to build the Docker image.