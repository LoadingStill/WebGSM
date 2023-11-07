function updateRAMUsage() {
    $.get('/get_ram_usage', function(data) {
        // Assuming the server returns RAM usage as a percentage (e.g., data.ram_usage = 45.67 for 45.67%)
        $('#ram-usage').text(data.ram_usage.toFixed(2) + '%');
    });
}

setInterval(updateRAMUsage, 1000); // Update RAM usage every 5 seconds
