//audioCtx = new (window.AudioContext)();
//chrome.tabCapture.capture
//var source = audioCtx.createMediaStreamSource(stream);
//var analyser = audioCtx.createAnalyser();
//createGain

var gain_node;
var audio_ctx;
var media_stream;
var running = false;

chrome.extension.onConnect.addListener(function(port) {
    port.onMessage.addListener(function(msg) {
        var gain = parseFloat(msg.action);
        
        if (msg.action === "start") {
            audio_ctx = new (window.AudioContext)();  
            chrome.tabCapture.capture({
                    audio : true,
                    video : false
            }, function(stream) {
                if (chrome.runtime.lastError){
                    console.log(chrome.runtime.lastError.message);
                } else { 
                    running = true
                    media_stream = stream;
                    var source = audio_ctx.createMediaStreamSource(stream);
                    var analyser = audio_ctx.createAnalyser();
                    source.connect(analyser);
                    analyser.connect(audio_ctx.destination);
                    gain_node = audio_ctx.createGain();
                    source.connect(gain_node);
                    gain_node.connect(audio_ctx.destination);
                    gain_node.gain.value = 1.0; 
                }
        });
        }
        
        if(msg.action == "end") {
            running = false
            audio_ctx.close();
            media_stream.getAudioTracks()[0].stop();
        }
        
        
        if (isFinite(gain) && running) {
            gain = Math.max(gain, -1);
            gain = Math.min(gain, 4);
            gain_node.gain.setValueAtTime(gain, audio_ctx.currentTime);
            //gain_node.gain.value = gain;
        }
    });
});

