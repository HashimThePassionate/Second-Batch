let id = (id) => document.getElementById(id);
let query = (q) => document.querySelectorAll(q);
let quiz = id('quiz');
let btn = id('submit');
let a = id('a_label');
let b = id('b_label');
let c = id('c_label');
let d = id('d_label');
let loadQuestion = id('heading');
let answer = query('.answer');

const QuizAPP = [
    {
        question: 'What is Capital of Pakistan',
        a: 'Sukkur',
        b: 'Islamabad',
        c: 'Rawalpindi',
        d: 'Karachi',
        correct: 'b',
        points: 10, // Assign points for this question
    },
    {
        question: 'What is National Animal of Pakistan',
        a: 'Elephant',
        b: 'Goat',
        c: 'Bat',
        d: 'Markhor',
        correct: 'd',
        points: 10, // Assign points for this question
    },
    {
        question: 'What is national language of Pakistan',
        a: 'Punjabi',
        b: 'Pashto',
        c: 'Arabic',
        d: 'Urdu',
        correct: 'd',
        points: 10, // Assign points for this question
    },
    {
        question: 'Who is Alama Iqbal',
        a: 'Poet',
        b: 'Singer',
        c: 'PM',
        d: 'Anchor',
        correct: 'a',
        points: 10, // Assign points for this question
    },
];

let clear = () => {
    for (let i = 0; i < answer.length; i++) {
        answer[i].checked = false;
    }
};

let checked = () => {
    let chk;
    for (let i = 0; i < answer.length; i++) {
        if (answer[i].checked) {
            chk = answer[i].id;
        }
    }
    return chk;
};

var points = 0;
var initialQuiz = 0;

let loadQuiz = () => {
    clear();
    let Data = QuizAPP[initialQuiz];
    loadQuestion.innerHTML = Data.question;
    a.innerHTML = Data.a;
    b.innerHTML = Data.b;
    c.innerHTML = Data.c;
    d.innerHTML = Data.d;
};

loadQuiz();

btn.addEventListener('click', (e) => {
    const chk = checked();
    if (chk) {
        if (chk === QuizAPP[initialQuiz].correct) {
            points += QuizAPP[initialQuiz].points;
        } else {
            // Subtract points for incorrect answers (negative marking)
            points -= 5;
        }
        initialQuiz++;
        if (initialQuiz < QuizAPP.length) {
            loadQuiz();
        } else {
            quiz.innerHTML = `<h2 style="color:blueviolet;font-size:20px; margin-top:20px;margin-right:20px; ">Your Answer Score is ${points}</h2>
            <button style="background-color:blueviolet;color:white;padding: 10px 55px; border:none; cursor:pointer; margin-top:20px; border-radius:30px;" onclick="history.go(0)">Play Again</button>`;
            console.log(quiz);
        }
    } else {
        alert('Invalid Try Again');
    }
});
// --------------------------------
const bodyEl = document.querySelector("body");

bodyEl.addEventListener("mousemove", (event) => {
  const xPos = event.offsetX;
  const yPos = event.offsetY;
  const spanEl = document.createElement("span");
  spanEl.style.left = xPos + "px";
  spanEl.style.right = yPos + "px";
  const size = Math.random() *50;
  spanEl.style.width = size + "px";
  spanEl.style.height = size + "px";
  bodyEl.appendChild(spanEl);
  setTimeout(() => {
    spanEl.remove();
  }, 3000);
});


