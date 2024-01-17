document.addEventListener('DOMContentLoaded', function () {
    updateDateTime();
    // Update every second
    setInterval(updateDateTime, 1000);
});

function updateDateTime() {
    var dateTimeElement = document.getElementById('datetime');
    var currentDateTime = new Date();
    var formattedDateTime = currentDateTime.toLocaleString();
    dateTimeElement.textContent = 'Current Date and Time: ' + formattedDateTime;
}