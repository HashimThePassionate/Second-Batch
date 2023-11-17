let btn = document.getElementById('btn');
console.log(btn);
function random(no) {
    return Math.floor(Math.random() * no + 1)
}
btn.addEventListener('mouseout', () => {
    const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
    const border =  `rgb(${random(150)}, ${random(130)}, ${random(90)})`;
    const borderColor = `10px dotted ${border}`
    btn.style.backgroundColor = rndCol;
    btn.style.border = borderColor ;
    btn.style.fontFamily = ` "Times New Roman" , "Arial" `;
});