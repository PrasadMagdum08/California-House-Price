// const PredictComponent = () => {
//   const [features, setFeatures] = useState("");
//   const [prediction, setPrediction] = useState(null);

//   const handleInputChange = (e) => {
//     setFeatures(e.target.value);
//   };

//   const handlePredict = async () => {
//     try {
//       const response = await axios.post("http://127.0.0.1:5000/api/predict", {
//         // features: features.split(",").map(Number),
//       });
//       setPrediction(response.data.prediction);
//     } catch (error) {
//       console.error("Error making prediction:", error);
//       setPrediction("Error occurred");
//     }
//   };


    // <div>
    //   <h1>Predict with ML Model</h1>
    //   <input
    //     type="text"
    //     placeholder="Enter features (comma-separated)"
    //     value={features}
    //     onChange={handleInputChange}
    //   />
    //   <button onClick={handlePredict}>Predict</button>
    //   {prediction && <p>Prediction: {prediction}</p>}
    // </div>




// Gemini ai

# models.py
from django.db import models

class Prediction(models.Model):
    input_data = models.TextField()
    predicted_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# serializers.py
from rest_framework import serializers
from .models import Prediction

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__' 

# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction
from .serializers import PredictionSerializer
# Import your machine learning model here
from your_ml_model import make_prediction 

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_data = serializer.validated_data['input_data']

        try:
            predicted_value = make_prediction(input_data) 
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(predicted_value=predicted_value)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# your_ml_model.py
import your_model_library  # Import your model library (e.g., scikit-learn)

def make_prediction(input_data):
    """
    This function takes input data and uses your trained model to make a prediction.

    Args:
        input_data: Input data for the model.

    Returns:
        The predicted value.
    """
    # Preprocess the input data (if necessary)
    # Example:
    # preprocessed_data = preprocess_input(input_data) 

    # Load your trained model
    model = your_model_library.load_model('path/to/your/model.pkl') 

    # Make the prediction
    prediction = model.predict(preprocessed_data) 

    return prediction[0]  # Assuming you get a single prediction value

# urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'predictions', views.PredictionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


// react js
import React, { useState } from 'react';
import axios from 'axios';

function PredictionForm() {
  const [inputData, setInputData] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/api/predictions/', { input_data: inputData });
      setPrediction(response.data.predicted_value);
      setError(null);
    } catch (err) {
      setError(err.response.data.error);
      setPrediction(null);
    }
  };

  return (
    <div>
      <h1>Prediction Form</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="inputData">Input Data:</label>
        <input 
          type="text" 
          id="inputData" 
          value={inputData} 
          onChange={(e) => setInputData(e.target.value)} 
        />
        <button type="submit">Predict</button>
      </form>

      {prediction !== null && (
        <div>
          <h2>Predicted Value: {prediction}</h2>
        </div>
      )}

      {error && (
        <div className="error">
          {error}
        </div>
      )}
    </div>
  );
}

export default PredictionForm;







CORS_ALLOWED_ORIGINS = [
"https://example.com",
"https://sub.example.com",
"http://localhost:8080",
"http://127.0.0.1:9000",
]

CORS_ALLOW_ALL_ORIGINS = True

'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',
    
'corsheaders',