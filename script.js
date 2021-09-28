// const dropArea = document.querySelector(".drag-area"),
// dragText = dropArea.querySelector("header"),
// button = dropArea.querySelector("button"),
// input = dropArea.querySelector("input");
// let file; 

// button.onclick = ()=>{
//   input.click(); 
// }

// input.addEventListener("change", function(){
//   file = this.files[0];
//   dropArea.classList.add("active");
//   showFile();
// });

// dropArea.addEventListener("dragover", (event)=>{
//   event.preventDefault(); 
//   dropArea.classList.add("active");
//   dragText.textContent = "Release to Upload File";
// });

// dropArea.addEventListener("dragleave", ()=>{
//   dropArea.classList.remove("active");
//   dragText.textContent = "Drag & Drop to Upload File";
// });

// dropArea.addEventListener("drop", (event)=>{
//   event.preventDefault(); 
//   file = event.dataTransfer.files[0];
//   showFile(); 
// });

// function showFile(){
//   let fileType = file.type; 
//   let validExtensions = ["application/pdf"]; 
//   if(validExtensions.includes(fileType)){ 
//     let fileReader = new FileReader(); 
//     fileReader.onload = ()=>{
//       let fileURL = fileReader.result; 
//       let docTag = `<img src="${fileURL}" alt="">`; 
//       dropArea.innerHTML = docTag; 
//     }
//     fileReader.readAsDataURL(file);
//   }else{
//     alert("This is not an PDF File!");
//     dropArea.classList.remove("active");
//     dragText.textContent = "Drag & Drop to Upload File";
//   }
// }