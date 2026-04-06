const links = document.querySelectorAll('#link-list li a');
links.forEach(link => {
    if (link.getAttribute('href').startsWith('http')) {
        link.classList.add('external-link');
    }
});

const display = document.getElementById('text-display');
const edit = document.getElementById('text-edit');

document.addEventListener('keydown', (e) => {
    if (e.code === 'KeyE' && e.ctrlKey){
        e.preventDefault();
        edit.value = display.innerText;
        edit.style.display = 'block';
        display.style.display = 'none';
        edit.focus();
    }
    if (e.code === 'KeyQ' && e.ctrlKey) {
        e.preventDefault();
        display.innerText = edit.value;
        display.style.display = 'block';
        edit.style.display = 'none';
    }
});

document.getElementById('nameInput').addEventListener('keypress', (e) => {
    if (/\d/.test(e.key)) {
        e.preventDefault();
    }
});

const field = document.getElementById('field');
const ball = document.getElementById('ball');
field.addEventListener('click', (e) => {
    const rect = field.getBoundingClientRect();
    console.log(rect.width, rect.height);
    console.log(rect.left, rect.right);
    console.log(rect.top, rect.bottom);

    const br = ball.getBoundingClientRect();

    let x = e.clientX - rect.left - (br.width / 2);
    let y = e.clientY - rect.top - (br.height / 2); 

    if (x < 0) x = 0;
    if (y < 0) y = 0;
    if (x > rect.width - br.width) x = rect.width - br.width;
    if (y > rect.height - br.height) y = rect.height - br.height;

    ball.style.left = x + 'px';
    ball.style.top = y + 'px';
});

// Задача 5

let currentLinght = -1;
function changeLight() {
    // console.log(12);
    const lamps = [`red`, `yellow`, `green`];
    lamps.forEach(id => document.getElementById(id).classList.remove(id));
    currentLinght = (currentLinght + 1) % lamps.length;
    const actived = lamps[currentLinght];
    document.getElementById(actived).classList.add(actived);
}

// Задача 6

function calendar() {
    const m = document.getElementById('calMounth').value - 1;
    const y = document.getElementById('calYear').value;
    const conteiner = document.getElementById('calender-conteiner');

    const firstDay = new Date(y, m, 1).getDay();
    const startDay = firstDay === 0 ? 6 : firstDay - 1;
    const daysInMount = new Date(y, m+1, 0).getDate();
    let html = '<table><tr><th>ПН</th><th>ВТ</th><th>СР</th><th>ЧТ</th><th>ПТ</th><th>СБ</th><th>ВС</th></tr><tr>';

    for (let i = 0; i < startDay; i++) html += '<td></td>';

    for (let day = 1; day <= daysInMount; day++){
        if ((startDay + day -1)%7 === 0 && day >1) html += '</tr><tr>';
        html += `<td>${day}</td>`;
    }
    html += '</tr></table>';
    conteiner.innerHTML = html;
};

// Задача 7
const task7 = document.getElementById('task7');
task7.addEventListener('contextmenu', (e) => {
    e.preventDefault();
});


// Задача 8
window.addEventListener('scroll', () => {
    const btnScroll = document.getElementById('task8');
    if (window.scrollY > 100) {
        btnScroll.style.display = 'block';
    } else {
        btnScroll.style.display = 'none';
    }
})

function up() {
    window.scrollTo({top: 0, behavior: 'smooth' });
}

function addBlock(){
    const containet = document.getElementById('block-container');

    let block = document.createElement('div');
    block.classList.add('block');
    // let randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    block.style.backgroundColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    block.onclick = function () {
        containet.removeChild(block);
    }
    containet.appendChild(block);
}