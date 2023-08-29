const fetchButton = document.getElementById("fetchButton");
const userInfoDiv = document.getElementById("userInfo");
const apiUrl = "https://api.github.com/users/";

fetchButton.addEventListener("click", async () => {
    const username = "adion81"; // GitHub username
    const response = await fetch(apiUrl + username);
    
    if (response.ok) {
        const userData = await response.json();
        displayUserInfo(userData);
    } else {
        userInfoDiv.textContent = "User not found.";
    }
});

function displayUserInfo(data) {
    userInfoDiv.innerHTML = `
        <h2>${data.login}</h2>
        <img src="${data.avatar_url}" alt="Profile Picture">
        <p>Name: ${data.name}</p>
        <p>Location: ${data.location}</p>
        <p>Followers: ${data.followers}</p>
        <p>Public Repositories: ${data.public_repos}</p>
    `;
}
