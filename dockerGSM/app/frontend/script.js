function manageDocker(action) {
    fetch(`/api/docker/${action}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error('Error:', error));
}

