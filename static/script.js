$(document).ready(function () {
    $('#predictionForm').on('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        // Collect all feature values
        const features = [
            parseFloat($('#age').val()),
            parseFloat($('#bp').val()),
            parseFloat($('#sg').val()),
            parseFloat($('#al').val()),
            parseFloat($('#su').val()),
            parseInt($('#rbc').val()), // Ensure numeric conversion
            parseInt($('#pc').val()),
            parseInt($('#pcc').val()),
            parseInt($('#ba').val()),
            parseFloat($('#bgr').val()),
            parseFloat($('#bu').val()),
            parseFloat($('#sc').val()),
            parseFloat($('#sod').val()),
            parseFloat($('#pot').val()),
            parseFloat($('#hemo').val()),
            parseFloat($('#pcv').val()),
            parseFloat($('#wc').val()),
            parseFloat($('#rc').val()),
            parseInt($('#htn').val()),
            parseInt($('#dm').val()),
            parseInt($('#cad').val()),
            parseInt($('#appet').val()),
            parseInt($('#pe').val()),
            parseInt($('#ane').val())
        ];

        // Log the collected features for debugging
        console.log("Sending features:", features);

        // Send POST request to Flask backend
        $.ajax({
            url: '/predict',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ features: features }),
            success: function (response) {
                console.log("Response:", response); // Debugging statement
                if (response.prediction) {
                    $('#result').html(`<p class="alert alert-info">Prediction: ${response.prediction}</p>`);
                } else {
                    $('#result').html('<p class="alert alert-danger">Error: Prediction undefined</p>');
                }
            },
            error: function (xhr, status, error) {
                console.error("Error:", xhr.responseJSON); // Debugging statement
                $('#result').html(`<p class="alert alert-danger">Error: ${xhr.responseJSON.error}</p>`);
            }
        });
    });
});