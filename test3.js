function setcolor(){
    var listPattern="0123456789ABCDEF";
    var set='#';
    for(i=0;i<6;i++){
        var randomSET=Math.floor(Math.random()*16);
        set=set+listPattern[randomSET];
    }
    console.log(set)
    return set;

}
var body=document.body;
var b=document.querySelector("#button1")
function changeColor(){
    body.style.backgroundColor=setcolor();
}
b.addEventListener('click',changeColor);
////////////////checker////////////////////////////
var restButton=document.querySelector("#button2")
var td=document.querySelectorAll("td")
function clickReset(){
    for(eachtd of td){
        eachtd.textContent="";
    }
}
function clickOnTd()
{
    if(this.textContent===""){
        this.textContent='x';
    }
    else if(this.textContent==="x"){
        this.textContent='o';
    }
    else{
        this.textContent='';
    }

}
for(eachtd of td){
    eachtd.addEventListener('click',clickOnTd)
}

restButton.addEventListener('click',clickReset)