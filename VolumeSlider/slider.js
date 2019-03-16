//TODO: Small improvement would be to make sure slider doesn't reset every time. 

var port = chrome.extension.connect();
port.postMessage({
    action: 'start'
});

var slider = document.getElementById('extendedVolumeSlider');
var output_gain = document.getElementById("gain");
output_gain.innerHTML = slider.value / 25.0

slider.oninput = function() {
    var gain = slider.value / 25.0
    output_gain.innerHTML = gain
    //For whatever reason -1 corresponds to mute NOT 0 
    if (slider.value == 0) {
        gain = -1;
    }
    port.postMessage({
        action: gain
    });
};