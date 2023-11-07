function updateNetworkUsage() {
    $.get('/get_network_usage', function(data) {
        // Assuming the server returns network usage as a percentage (e.g., data.network_usage = 75.12 for 75.12%)
        $('#network-usage').text(data.network_usage.toFixed(2) + '%');
    });
}

setInterval(updateNetworkUsage, 5000); // Update network usage every 5 seconds
