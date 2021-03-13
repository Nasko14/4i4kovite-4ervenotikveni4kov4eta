function drawCircle() {
    var x = document.getElementById('x').value;
    var y = document.getElementById('y').value;
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");
    ctx.beginPath()
    ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = 'green';
    ctx.fill();
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#003300';
    ctx.stroke();
}

function drawRect(){
    console.log("drawing Rect");
    var x1 = document.getElementById('x1').value;
    var y1 = document.getElementById('y1').value;
    var x2 = document.getElementById('x2').value;
    var y2 = document.getElementById('y2').value;
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");
    ctx.beginPath();
    ctx.lineWidth = 3;
    ctx.strokeStyle = "red";
    ctx.rect(x1, y1, x2-x1, y2-y1);
    ctx.stroke();
}

