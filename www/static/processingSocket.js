var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

socket.on('connect', function() {
    console.log('Connected');
});

socket.on('error', function(error) {
    console.log('Socket error:', error);
});

socket.on('progress', function(msg) {
    document.getElementById('progress').innerHTML = msg.data;
});

socket.on('errorOccured', function(msg) {
    document.getElementById('errorContent').style.display = "block";
    document.getElementById('errorContent').innerHTML += msg.errorContent + "<br />";
});

socket.on('finished', function() {
    if(document.getElementById('errorContent').style.display == "none")
    {
        window.location.href = '/advanced';
    }
    else
    {
        document.getElementById('LoadingBar').style.display = "none";
        document.getElementById('errorContent').innerHTML += "<button id=\"backButton\" onclick=\"window.location.href = '/advanced';\" class=\"btn btn-primary btn-lg\">Continue</button>";
    }
});

socket.on('disconnect', function() {
    console.log('Disconnected from the server');
});