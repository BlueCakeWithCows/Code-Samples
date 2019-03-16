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
    if (slider.value == 0) {
        gain = -1;
    }
    port.postMessage({
        action: gain
    });
};