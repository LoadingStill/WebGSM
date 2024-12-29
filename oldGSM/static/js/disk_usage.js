function updateDiskUsage() {
    $.get('/get_disk_usage', function(data) {
        // Assuming the server returns disk usage as a percentage (e.g., data.disk_usage = 55.33 for 55.33%)
        $('#disk-usage').text(data.disk_usage.toFixed(2) + '%');
    });
}

setInterval(updateDiskUsage, 1000); // Update disk usage every 5 seconds
