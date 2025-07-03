// 중복되지 않는 0 ~ 9 사이의 랜덤한 숫자 3개가 정해진다.
// 화면에 보이는 칸에 각각 숫자를 넣으면서 순서가 올바른 숫자 3개를 찾는다.

// 숫자는 맞지만 위치가 틀리다 -> 볼
// 숫자와 위치가 전부 맞다 -> 스트라이크

let attempts = 9;
let answer = [];

const inputs = document.querySelectorAll('.input-field');
const btn = document.querySelector('.submit-button');
const resDiv = document.getElementById('results');
const img = document.getElementById('game-result-img');
const atmp = document.getElementById('attempts');

function resetGame() {
    tries = 9;

    // 중복되지 않는 3개의 랜덤한 숫자 설정
    answer = [];
    while (answer.length < 3) {
        const num = Math.floor(Math.random()*10);
        if (!answer.includes(num)) 
            answer.push(num);
    }

    // html의 input과 결과창의 내용 비운다
    inputs.forEach(i => i.value='');
    resDiv.innerHTML = '';
    img.src = '';
    atmp.textContent = attempts;
    btn.disabled = false;
}

function check_numbers() {
    const guess = [...inputs].map(i => +i.value);
    if (guess.some(x => isNaN(x))) {
        inputs.forEach(i => i.value = '');
        return;
    }

    attempts--;
    atmp.textContent = attempts;

    let s = 0, b = 0;
    guess.forEach((v, i) => v === answer[i] ? s++ : (answer.includes(v) && b++));

    const p = document.createElement('p');
    p.textContent = s || b ? `${s}S ${b}B` : 'O';
    resDiv.appendChild(p);

    inputs.forEach(i => i.value='');

  if (s === 3) {
    img.src = 'success.png'; btn.disabled = true;
  } else if (attempts === 0) {
    img.src = 'fail.png';    btn.disabled = true;
  }
}

window.addEventListener('DOMContentLoaded', () => {
  resetGame();
  btn.addEventListener('click', check);
});