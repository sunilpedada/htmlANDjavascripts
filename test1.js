var p1=document.getElementsByTagName("p")[0]
var p2=document.getElementsByTagName("p")[1]
var ul1=document.querySelector("ul")
var ul2=document.querySelector("ol")
function change(){
    var colorPattern="0123456789ABCDEF";
    var setcolor="#";
    for(var i=0;i<6;i++){
        //console.log("for")
        random=Math.floor(Math.random()*16);
        //console.log(random)
        setcolor=setcolor+colorPattern[random];
        //console.log(setcolor)
    }
    return setcolor;
}
function set(){
    p1.style.color=change();
    //console.log("p1")
    p2.style.color=change();
    ul1.style.color=change();
    ul2.style.color=change();
}
setInterval(set,300)