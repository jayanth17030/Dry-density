function go()
{
    let value=document.getElementById('height').value;
    document.getElementById('toDisplay').textContent=value;
    let value2=document.getElementById('diameter').value;
    document.getElementById('toDisplay2').textContent=value2;
    let value3=document.getElementById('weightofMould').value;
    document.getElementById('toDisplay3').textContent=value3;
let pie = 22/7;
let vol = (pie/4)*value*(value2**2);
document.getElementById('toDisplay4').textContent=vol;
}

function submission(){
    let mouldAndSoil = document.getElementById('mouldAndSoil').value;
    let values = arrayvalues('csv');
    let values2 =arrayvalues2('csv');

    document.getElementById('output').innerHTML = values+values2;
}
function arrayvalues2(somevalue){
    let splitstring = somevalue.split(",");
    return splitstring;
}
function arrayvalues(somevalue){
    let splitvalue = somevalue.split(",");
    for (x in splitvalue){
        splitvalue[x]=parseFloat(splitvalue[x]);

    }
    return splitvalue;
}

function sendEmail(){
    Email.send({
        Host : "smtp.gmail.com",
        Username : "guna.7382@gmail.com",
        Password : "Jayanth@17030",
        To : 'jayanths8688@gmail.com',
        From : document.getElementById("email").value,
        Subject : "This is the subject",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );
}