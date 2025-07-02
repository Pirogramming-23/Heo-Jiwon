let answer = [];
let triesLeft = 9;

function initGame() {
  answer = [];
  while (answer.length < 3) {
    const num = Math.floor(Math.random() * 10);
    if (!answer.includes(num)) answer.push(num);
  }

  triesLeft = 9;

  const inputs = document.querySelectorAll('.input-field');
  inputs.forEach(input => input.value = '');

  const resultsDiv = document.getElementById('results');
  if (resultsDiv) resultsDiv.innerHTML = '';

  const img = document.getElementById('game-result-img');
  if (img) img.src = '';

  const btn = document.querySelector('.submit-button');
  if (btn) btn.disabled = false;

  const attemptsSpan = document.getElementById('attempts');
  if (attemptsSpan) attemptsSpan.innerText = triesLeft;
}

window.addEventListener('DOMContentLoaded', initGame);

function check_numbers() {
  const inputs = document.querySelectorAll('.input-field');
  const guess = [];

  for (const input of inputs) {
    if (!input.value) {
      inputs.forEach(i => i.value = '');
      return;
    }
    const val = Number(input.value);
    if (isNaN(val) || val < 0 || val > 9) {
      inputs.forEach(i => i.value = '');
      return;
    }
    guess.push(val);
  }

  triesLeft--;
  const attemptsSpan = document.getElementById('attempts');
  if (attemptsSpan) attemptsSpan.innerText = triesLeft;

  let strikes = 0;
  let balls = 0;
  for (let i = 0; i < 3; i++) {
    if (guess[i] === answer[i]) {
      strikes++;
    } else if (answer.includes(guess[i])) {
      balls++;
    }
  }

  const resultsDiv = document.getElementById('results');
  if (!resultsDiv) return;
  const p = document.createElement('p');
  if (strikes === 0 && balls === 0) {
    p.innerText = 'O';
  } else {
    p.innerText = `${strikes}S ${balls}B`;
  }
  resultsDiv.appendChild(p);

  inputs.forEach(i => i.value = '');

  const img = document.getElementById('game-result-img');
  const btn = document.querySelector('.submit-button');
  if (strikes === 3) {
    if (img) img.src = 'success.png';
    if (btn) btn.disabled = true;
  } else if (triesLeft <= 0) {
    if (img) img.src = 'fail.png';
    if (btn) btn.disabled = true;
  }
}
