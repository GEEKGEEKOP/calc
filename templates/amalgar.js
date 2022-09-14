function gam(){
    a=document.getElementById('gam1').value;
    b=document.getElementById('gam2').value;
    a=parseInt(a)
    b=parseInt(b)
    c=document.getElementById("gamm");
    c.value = (a+b);
}

function men(){
    a=document.getElementById('men1').value;
    b=document.getElementById('men2').value;
    a=parseInt(a)
    b=parseInt(b)
    c=document.getElementById("menn");
    c.value = (a-b);
}

function zab(){
    a=document.getElementById('zab1').value;
    b=document.getElementById('zab2').value;
    a=parseInt(a)
    b=parseInt(b)
    c=document.getElementById("zabb");
    c.value = (a*b);
}

function tag(){
    a=document.getElementById('tag1').value;
    b=document.getElementById('tag2').value;
    a=parseInt(a)
    b=parseInt(b)
    c=document.getElementById("tagg");
    c.value = (a/b);
}

function bag(){
    a=document.getElementById('bag1').value;
    b=document.getElementById('bag2').value;
    a=parseInt(a)
    b=parseInt(b)
    c=document.getElementById("bagg");
    c.value = (a%b);
}

function tav(){
    a=document.getElementById('tav1').value;
    b=document.getElementById('tav2').value;
    a=parseInt(a)
    b=parseInt(b)
    c=document.getElementById("tavv");
    c.value = (a**b);
}