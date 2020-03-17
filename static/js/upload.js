"use strict";

// File for uploading user images 

// Event listeners for submiting file
document.querySelector('.file-select)
    .addEventListener('change', handleFileUploadChange);
document.querySelector('.file-submit)
    .addEventListener('click', handleFileUploadSubmit);

let selectedFile;
    handleFileUploadChange(evt) {
    // Keeps track of what file the user has inputted
    selectedFile = evt.target.files[0];
}

handleFileUploadSubmit(evt) {
  // location where user images are stored
  const uploadTask = storageRef.child(`/static/user_images/${selectedFile.name}`).put(selectedFile); 
  uploadTask.on('state_changed', (snapshot) => {
  // Observe state change events such as progress, pause, and resume
  }, (error) => {
    // Handle unsuccessful uploads
    console.log(error);
  }, () => {
     // When upload is complete
     console.log('success');
  });
}``