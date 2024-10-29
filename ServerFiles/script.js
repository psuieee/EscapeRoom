let score = 0;
let gameActive = false;
const targetsContainer = document.getElementById('targets');
const scoreDisplay = document.getElementById('score');
const startButton = document.getElementById('start-button');
const winMessage = document.getElementById('win-message');
const winningScore = 10;
let targetInterval;

startButton.addEventListener('click', startGame);

function startGame() {
    score = 0;
    gameActive = true;
    scoreDisplay.innerText = `Score: ${score}`;
    winMessage.style.display = 'none';
    startButton.style.display = 'none'; // Hide start button
    targetsContainer.innerHTML = ''; // Clear previous targets

    generateTarget(); // Spawn the first target
    targetInterval = setInterval(generateTarget, 2000); // Generate new target every 2 seconds
}

function generateTarget() {
    if (!gameActive) return;

    // Create an img element for target
    const target = document.createElement('img');
    target.src = 'nerd.jpg'; // Set the source to nerd.jpg
    target.classList.add('target');

    // Resize the image
    const targetSize = 75; // Size of the target in pixels
    target.style.width = `${targetSize}px`; // Set the width
    target.style.height = `${targetSize}px`; // Set the height
    
    
    // Position the target randomly within the game area
    
    positionTarget(target);
    targetsContainer.appendChild(target);

    // Remove target after 1 second if not clicked
    setTimeout(() => {
        if (target.parentNode) {
            target.remove();
        }
    }, 1000);

    // Add click event to the target
    target.addEventListener('click', () => {
        score++;
        scoreDisplay.innerText = `Score: ${score}`;
        target.remove(); // Remove target when clicked

        // Check for win condition
        if (score === winningScore) {
            endGame();
        }
    });
}

// Function to position the target randomly within the game area

function positionTarget(target) {
    const targetSize = 75; // Size of the target
    const x = Math.random() * (window.innerWidth - targetSize); // Ensure it stays within the width
    const y = Math.random() * (window.innerHeight - targetSize - 100); // Ensure it stays within the height, leaving some space at the bottom
    
    target.style.left = `${x}px`;
    target.style.top = `${y}px`;
}


function endGame() {
    gameActive = false;
    clearInterval(targetInterval); // Stop generating new targets
    winMessage.style.display = 'block'; // Show the win message
    startButton.style.display = 'block'; // Show the start button again for replay
    winMessage.innerHTML = `You Win! The key is: <strong>YOUR_SECRET_KEY</strong>`; // Display win message with key
}


