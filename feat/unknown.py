<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Camera Access</title>
</head>
<body>
    <button id="cameraButton">Access Camera</button>

    <video id="videoElement" autoplay></video>

    <script>
        const cameraButton = document.getElementById('cameraButton');
        const videoElement = document.getElementById('videoElement');

        cameraButton.addEventListener('click', async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                videoElement.srcObject = stream;
            } catch (error) {
                console.error('Error accessing camera:', error);
            }
        });
    </script>
</body>
</html>
