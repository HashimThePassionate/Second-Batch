var id = (id) => document.getElementById(id)
let p = id('para')
let mydiv = id('mydiv')
// console.log(p);
let newpara = document.createElement('p');
let newcomment = document.createComment("This is my comment");
let newtext = document.createTextNode("hey there! Welcome to new paragraph");
newpara.appendChild(newcomment)
newpara.appendChild(newtext)
document.body.insertBefore(newpara,p);
console.log(newpara);
let newparaidset = newpara.setAttribute('class','paraClass')
newpara.style.fontSize="30px";
newpara.style.border="2px solid green";
newpara.removeAttribute('class');
let Div = document.createElement('div');
let span = document.createElement('span');
let h5 = document.createElement('h5');
let h6 = document.createElement('h6');
let h5text = document.createTextNode("Heading Five");
let h6text = document.createTextNode("Heading Sixth");
h5.appendChild(h5text);
h6.appendChild(h6text);
let spantext =  document.createTextNode('This span text inside Div');
span.appendChild(spantext);
document.body.insertBefore(Div,p)
Div.append("TEXT ",span,h5)
Div.prepend(h6);
console.log(Div);
console.log(p);
let idOfP = p.getAttribute('id');
console.log(idOfP);
console.log(mydiv);
let idOfDiv = mydiv.getAttribute('id');
let classOfDiv = mydiv.getAttribute('class');
console.log(idOfDiv,classOfDiv);

Div.style.backgroundImage = "url('eyes.jpg')"; 
Div.style.backgroundSize ="contain";
Div.style.backgroundRepeat ="no-repeat";
Div.style.backgroundPosition ="center";
Div.style.padding="30px";
Div.style.backgroundColor="tomato";
// Div.removeAttribute("class","container")



mydiv.classList.add("foo", "success", "failure");
console.log(mydiv.outerHTML);
// mydiv.classList()
mydiv.classList.remove('foo');