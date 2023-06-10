// Display the loader on initial page load
window.addEventListener('load', function() {
  showLoader();
});

// Display the loader when making AJAX requests
$(document).ajaxStart(function() {
  showLoader();
});

// Hide the loader when AJAX requests complete
$(document).ajaxStop(function() {
  hideLoader();
});

// Function to show the loader
function showLoader() {
  document.getElementById('loader').style.display = 'flex';
}

// Function to hide the loader
function hideLoader() {
  document.getElementById('loader').style.display = 'none';
}






