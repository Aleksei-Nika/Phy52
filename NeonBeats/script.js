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
const metronom = document.getElementById('metronom');
const metronomSlider = document.getElementById('metronomSlider');
let isMetronom = false;

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

    const pad = document.querySelector(`.pad[data-key="${key}"]`);
    if(pad){
        pad.classList.add('active');
        setTimeout(() => pad.classList.remove('active'), 100);
    }

    if (isRecording){
        recordedSequence.push({
            key: key,
            time: Date.now() - startTime,
        });
    }
}

window.addEventListener('keydown', (e) => {
    const key = e.key.toUpperCase();
    playSound(key);
});

pads.forEach(pad => {
    pad.addEventListener('click', () => {
        playSound(pad.dataset.key);
    })
});

volumeSlider.addEventListener('input', (event)=>{
        currentVolume = event.target.value;

});

recBtn.addEventListener('click', ()=>{
    isRecording = true;
    recordedSequence = [];
    startTime = Date.now();
    recIndicator.classList.add('active');
});

stopBtn.addEventListener('click', () => {
    isRecording = false;
    recIndicator.classList.remove('active');
});

playBtn.addEventListener('click', () => {
    if (recordedSequence.length === 0) return;
    recordedSequence.forEach(item => {
        setTimeout(() => {
            playSound(item.key);
        }, item.time);
    });
});


function funcMetronom(){
    if (!isMetronom) return;
    playSound('A');
}

metronom.addEventListener('click', (event) => {
    setInterval(funcMetronom(), (60 / metronomSlider.value) * 1000)
});