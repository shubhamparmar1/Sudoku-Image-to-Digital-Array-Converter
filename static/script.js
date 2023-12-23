var loadFile = function(event) {
    var output = document.getElementById('preview');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
        URL.revokeObjectURL(output.src) // free memory
        document.getElementById('upload-prompt').style.display = 'none';
        output.style.display = 'block';
        document.getElementById('solve-button').style.display = 'block';
    }
};

var solveSudoku = async function() {
    document.getElementById('loading').style.display = 'flex'; // Show the loading animation
    var imageUpload = document.getElementById('image-upload');
    var formData = new FormData();
    formData.append('image', imageUpload.files[0]);
    var response = await fetch('/solve_sudoku', {
        method: 'POST',
        body: formData
    });
    // var solvedSudokuUrl = await response.text();
    var solvedSudokuUrl = window.location.origin + await response.text();
    document.getElementById('loading').style.display = 'none'; // Hide the loading animation
    document.getElementById('solved-sudoku').src = solvedSudokuUrl;
    document.getElementById('solution-section').style.display = 'block'; // Show the solved Sudoku
};

window.addEventListener('scroll', function() {
    var image = document.querySelector('.image2');
    var imagePosition = image.getBoundingClientRect();

    if(imagePosition.top < window.innerHeight && imagePosition.bottom >= 0) {
        image.classList.add('visible');
    } else {
        image.classList.remove('visible');
    }
}); 

// // Assume solutionAvailable is a boolean that indicates whether a solution is available
// if (solutionAvailable) {
//     document.querySelector('.solution-section').classList.add('solution-available');
// } else {
//     document.querySelector('.solution-section').classList.remove('solution-available');
// }