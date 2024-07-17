// Example function to fetch user profile data
function fetchUserProfile() {
    const token = localStorage.getItem('token');

    fetch('/api/user/profile', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(data => {
        // Update UI with retrieved user profile information
        console.log('User profile data:', data);
        // Example: Display user profile details on the UI
        document.getElementById('username').innerText = data.username;
        document.getElementById('email').innerText = data.email;
    }).catch(error => {
        console.error('Error fetching user profile:', error);
        // Handle errors here (e.g., display error message to the user)
    });
}
