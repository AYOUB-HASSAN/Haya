document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video-frame');
    const animatedText = document.getElementById('animated-text');

    // Trigger when the video ends
    video.addEventListener('ended', () => {
        animatedText.classList.remove('hidden'); // Make the text section visible

        // Split text into letters and animate
        const textElements = animatedText.querySelectorAll('p');
        textElements.forEach((paragraph, paragraphIndex) => {
            const letters = paragraph.textContent.split('');
            paragraph.innerHTML = ''; // Clear original text
            letters.forEach((letter, letterIndex) => {
                const span = document.createElement('span');
                span.textContent = letter;
                span.style.animationDelay = `${(paragraphIndex * 2) + letterIndex * 0.05}s`; // Add delay for each letter
                paragraph.appendChild(span);
            });
        });
    });
});
