function updateNetworkUsage() {
    $.get('/get_network_percent', function(data) {
        // Assuming the server returns network usage as a percentage (e.g., data.network_percent = 75.12 for 75.12%)
        $('#network-percent').text(data.network_percent.toFixed(2) + '%');
    });
}

setInterval(updateNetworkUsage, 5000); // Update network usage every 5 seconds
