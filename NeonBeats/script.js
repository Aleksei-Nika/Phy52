const sounds = {
    'A': 'sounds/A.wav',
    'S': 'sounds/S.wav',
    'D': 'sounds/D.wav',
    'F': 'sounds/F.wav',
    'G': 'sounds/G.wav',
    'H': 'sounds/H.wav',
    'J': 'sounds/J.wav',
    'K': 'sounds/K.wav',
}

const pads = document.querySelectorAll('.pad');
const volumeSlider = document.getElementById('volumeSlider');
const recBtn = document.getElementById('recBtn');
const stopBtn = document.getElementById('stopBtn');
const playBtn = document.getElementById('playBtn');
const recIndicator = document.getElementById('recIndicator');

let recordedSequence = [];
let isRecording = false;
let startTime = 0;
let currentVolume = 0.5;

function playSound(key) {
    const soundPath = sounds[key];
    if (!soundPath) return;
    const audio = new Audio(soundPath);
    audio.volume = currentVolume;
    audio.currentTime = 0;
    audio.play();
}

window.addEventListener('keydown', (e) => {
    const key = e.key.toUpperCase();
    playSound(key);
});

function 