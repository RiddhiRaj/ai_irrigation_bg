// static/main.js
document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = {
        temperature: document.getElementById('temperature').value,
        humidity: document.getElementById('humidity').value,
        precipitation: document.getElementById('precipitation').value,
        soil_moisture: document.getElementById('soil_moisture').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        alert('Predicted Irrigation Requirement: ' + data.prediction + ' mm');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
