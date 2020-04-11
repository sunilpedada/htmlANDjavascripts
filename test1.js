function convertingSnakeToKabab(n){
    var newn='';
    for(var i=0;i<n.length;i++){
        if(n[i]=='_'){
            newn=newn+'-';
        }
        else if(i<n.length){
            newn=newn+n[i]
        }
    }
    return newn
}
var n="hi_sunil_welcome";
console.log(convertingSnakeToKabab(n));