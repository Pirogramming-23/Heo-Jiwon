let seconds = 0;
let tenmill = 0;
let intervalId;

const Seconds = document.getElementById('seconds');
const Tenmill = document.getElementById('tenmill');
const StartBtn = document.getElementById('start-button');
const StopBtn = document.getElementById('stop-button');
const ResetBtn = document.getElementById('reset-button');
const RecordList = document.getElementById('record-list');
const DeleteSelectedBtn = document.getElementById('delete-selected');
const ClearAll = document.getElementById('clear-records');
const ClickAllBtn = document.getElementById('click-all');



StartBtn.onclick = function() {
    clearInterval(intervalId);
    intervalId = setInterval(operateTimer, 10);
}

RecordList.addEventListener('click', function(e) {
    if (e.target.classList.contains('click')) {
        e.target.classList.toggle('selected');
    }
})

ClickAllBtn.onclick = () => {
    const allBtns = RecordList.querySelectorAll('.click');
    const anyUnselected = Array.from(allBtns).some(btn => !btn.classList.contains('selected'));
    allBtns.forEach(btn => btn.classList.toggle('selected', anyUnselected));
}

StopBtn.onclick = function() {
    clearInterval(intervalId);

    const currentTime = `${Seconds.textContent}:${Tenmill.textContent}`;
    const li = document.createElement('li');

    const Click = document.createElement('button');
    Click.type = 'button';
    Click.className = 'click';

    const span = document.createElement('span');
    span.textContent = currentTime;

    li.appendChild(Click);
    li.appendChild(span);
    RecordList.appendChild(li);

}

DeleteSelectedBtn.onclick = () => {
    const selected = RecordList.querySelectorAll('.click.selected');
    selected.forEach(btn => btn.closest('li').remove());
}

ClearAll.onclick = () => {
    RecordList.innerHTML = '';
}

ResetBtn.onclick = function() {
    clearInterval(intervalId);
    tenmill = 0;
    seconds = 0;
    Tenmill.textContent = '00';
    Seconds.textContent = '00';
}

function operateTimer() {
    tenmill++;
    Tenmill.textContent = tenmill > 9 ? tenmill : '0' + tenmill;
    if (tenmill > 99) {
        seconds++;
        Seconds.textContent = seconds > 9 ? seconds : '0' + seconds;
        tenmill = 0;
        Tenmill = "00"
    }
}
