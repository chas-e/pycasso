var canvas = document.getElementById("paint");
var ctx = canvas.getContext("2d");
var width = canvas.width,
  height = canvas.height;
var curX, curY, prevX, prevY;
var hold = false;
var fill_value = true,
  stroke_value = false;
var canvas_data = {
  pencil: [],
  line: [],
  rectangle: [],
  circle: [],
  eraser: [],
};
ctx.lineWidth = 2;
var BB = canvas.getBoundingClientRect();
var offsetX = BB.left + 5; // change from canvas.offsetLeft
var offsetY = BB.top; // change from canvas.offsetTop
console.log(canvas.getBoundingClientRect());
console.log(canvas.offsetLeft, canvas.offsetTop);
console.log(offsetX, offsetY);

function color(color_value) {
  ctx.strokeStyle = color_value;
  ctx.fillStyle = color_value;
}

function add_pixel() {
  ctx.lineWidth += 1;
}

function reduce_pixel() {
  if (ctx.lineWidth == 2) return;
  else ctx.lineWidth -= 1;
}

function fill() {
  fill_value = true;
  stroke_value = false;
}

function outline() {
  fill_value = false;
  stroke_value = true;
}

function reset() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  canvas_data = { pencil: [], line: [], rectangle: [], circle: [], eraser: [] };
}

// pencil tool

function pencil() {
  canvas.onmousedown = function (e) {
    curX = e.clientX - offsetX;
    curY = e.clientY - offsetY;
    hold = true;

    prevX = curX;
    prevY = curY;
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
  };

  canvas.onmousemove = function (e) {
    if (hold) {
      curX = e.clientX - offsetX;
      curY = e.clientY - offsetY;
      draw();
    }
  };

  canvas.onmouseup = function (e) {
    hold = false;
  };

  canvas.onmouseout = function (e) {
    hold = false;
  };

  function draw() {
    ctx.lineTo(curX, curY);
    ctx.stroke();
    canvas_data.pencil.push({
      startx: prevX,
      starty: prevY,
      endx: curX,
      endy: curY,
      thick: ctx.lineWidth,
      color: ctx.strokeStyle,
    });
  }
}

// line tool

function line() {
  canvas.onmousedown = function (e) {
    img = ctx.getImageData(0, 0, width, height);
    prevX = e.clientX - offsetX;
    prevY = e.clientY - offsetY;
    hold = true;
  };

  canvas.onmousemove = function (e) {
    if (hold) {
      ctx.putImageData(img, 0, 0);
      curX = e.clientX - offsetX;
      curY = e.clientY - offsetY;
      ctx.beginPath();
      ctx.moveTo(prevX, prevY);
      ctx.lineTo(curX, curY);
      ctx.stroke();
      canvas_data.line.push({
        starx: prevX,
        starty: prevY,
        endx: curX,
        endY: curY,
        thick: ctx.lineWidth,
        color: ctx.strokeStyle,
      });
      ctx.closePath();
    }
  };

  canvas.onmouseup = function (e) {
    hold = false;
  };

  canvas.onmouseout = function (e) {
    hold = false;
  };
}

// rectangle tool

function rectangle() {
  canvas.onmousedown = function (e) {
    img = ctx.getImageData(0, 0, width, height);
    prevX = e.clientX - offsetX;
    prevY = e.clientY - offsetY;
    hold = true;
  };

  canvas.onmousemove = function (e) {
    if (hold) {
      ctx.putImageData(img, 0, 0);
      curX = e.clientX - offsetX - prevX;
      curY = e.clientY - offsetY - prevY;
      ctx.strokeRect(prevX, prevY, curX, curY);
      if (fill_value) {
        ctx.fillRect(prevX, prevY, curX, curY);
      }
      canvas_data.rectangle.push({
        starx: prevX,
        stary: prevY,
        width: curX,
        height: curY,
        thick: ctx.lineWidth,
        stroke: stroke_value,
        stroke_color: ctx.strokeStyle,
        fill: fill_value,
        fill_color: ctx.fillStyle,
      });
    }
  };

  canvas.onmouseup = function (e) {
    hold = false;
  };

  canvas.onmouseout = function (e) {
    hold = false;
  };
}

// circle tool

function circle() {
  canvas.onmousedown = function (e) {
    img = ctx.getImageData(0, 0, width, height);
    prevX = e.clientX - offsetX;
    prevY = e.clientY - offsetY;
    hold = true;
  };

  canvas.onmousemove = function (e) {
    if (hold) {
      ctx.putImageData(img, 0, 0);
      curX = e.clientX - offsetX;
      curY = e.clientY - offsetY;
      ctx.beginPath();
      ctx.arc(
        Math.abs(curX + prevX) / 2,
        Math.abs(curY + prevY) / 2,
        Math.sqrt(Math.pow(curX - prevX, 2) + Math.pow(curY - prevY, 2)) / 2,
        0,
        Math.PI * 2,
        true
      );
      ctx.closePath();
      ctx.stroke();
      if (fill_value) ctx.fill();
      canvas_data.circle.push({
        starx: prevX,
        stary: prevY,
        radius: curX - prevX,
        thick: ctx.lineWidth,
        stroke: stroke_value,
        stroke_color: ctx.strokeStyle,
        fill: fill_value,
        fill_color: ctx.fillStyle,
      });
    }
  };

  canvas.onmouseup = function (e) {
    hold = false;
  };

  canvas.onmouseout = function (e) {
    hold = false;
  };
}

// eraser tool

function eraser() {
  canvas.onmousedown = function (e) {
    curX = e.clientX - offsetX;
    curY = e.clientY - offsetY;
    hold = true;

    prevX = curX;
    prevY = curY;
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
  };

  canvas.onmousemove = function (e) {
    if (hold) {
      curX = e.clientX - offsetX;
      curY = e.clientY - offsetY;
      draw();
    }
  };

  canvas.onmouseup = function (e) {
    hold = false;
  };

  canvas.onmouseout = function (e) {
    hold = false;
  };

  function draw() {
    ctx.lineTo(curX, curY);
    ctx.strokeStyle = "#ffffff";
    ctx.stroke();
    canvas_data.eraser.push({
      startx: prevX,
      starty: prevY,
      endx: curX,
      endy: curY,
      thick: ctx.lineWidth,
      color: ctx.strokeStyle,
    });
  }
}

function save() {
  var filename = document.getElementById("fname").value;
  var data = JSON.stringify(canvas_data);
  var image = canvas.toDataURL();
  const painting = {
    save_fname: filename,
    save_cdata: data,
    save_image: image,
  };

  $.post("/paint/", painting);
  alert(filename + " saved");
}

// Chatroom

const roomName = JSON.parse($("#room-name").textContent);

const drawSocket = new WebSocket(
  "ws://" + window.location.host + "ws/chat/" + roomName + "/"
);

drawSocket.onopen = function (e) {
  alert("[open] Connection established");
  alert("Sending to server");
  drawSocket.send("Welcome to paint chat!");
};

drawSocket.onmessage = function (event) {
  alert(`[message] Data received from server: ${event.data}`);
  if (event.data == "reset") {
    reset()
    return;
  }
  d = JSON.parse(event.data);
  console.log(d);

  for (var i = 0; i < d.length; i++) {
    ctx.fillRect();
  }
};

drawSocket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    alert('[close] Connection died');
  }
};

drawSocket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};
