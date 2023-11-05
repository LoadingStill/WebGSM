// cpu_usage.js
function updateCPUUsage() {
    $.get('/get_cpu_usage', function(data) {
        $('#cpu-usage').text(data.cpu_usage.toFixed(2) + '%');
    });
}

setInterval(updateCPUUsage, 1000); // Update every 5 seconds
