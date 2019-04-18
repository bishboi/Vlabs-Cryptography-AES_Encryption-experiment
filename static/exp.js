document.getElementById("datafromdatabase").style.display = "none";
document.getElementById("par1").style.display = "none";
document.getElementById("par2").style.display = "none";
document.getElementById("par3").style.display = "none";
document.getElementById("par4").style.display = "none";
document.getElementById("but").style.display = "none";
document.getElementById("train").style.display = "none";
document.getElementById("algo").style.display = "none";
document.getElementById("feature").style.display = "none";
document.getElementById("answerspace").style.display = "none";

function language() {
	document.getElementById("par1").style.display = "block";
	document.getElementById("train").style.display = "block";
}
function change1() {
	document.getElementById("par2").style.display = "block";
	document.getElementById("algo").style.display = "block";	
}
function change2() {
	document.getElementById("par3").style.display = "block";
	document.getElementById("feature").style.display = "block";	
}
function change3() {
	document.getElementById("par4").style.display = "block";
	document.getElementById("but").style.display = "block";	
}
function answer() {
	dict=document.getElementById('datafromdatabase').innerHTML;
	dict=dict.substr(1).slice(0,-1);
	dict=dict.substr(1);
	dict=JSON.parse(dict);
	a=document.getElementById("lann").value;
	b=document.getElementById("train").value;
	c=document.getElementById("algo").value;
	d=document.getElementById("feature").value;
	if(dict[a][b][c][d]!=undefined)
	{
		document.getElementById('answerspace').innerHTML="<br>" + "Accuracy is : " + dict[a][b][c][d];
		document.getElementById("answerspace").style.display = "block";	
	}
	else
	{
		document.getElementById("answerspace").style.display = "none";	
	}
}