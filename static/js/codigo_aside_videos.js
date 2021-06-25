// Videos de aside
let videos = [
    "https://www.youtube.com/embed/KdLCtBmXqFU", 
    "https://www.youtube.com/embed/xfPbj2F-Ynk", 
    "https://www.youtube.com/embed/1n7mApLx3qg",
    "https://www.youtube.com/embed/YcReRb5UJEA",
    "https://www.youtube.com/embed/TUC_2nPScxo"
]

var randomVideo = videos[Math.floor(Math.random() * videos.length)];
document.getElementById("video_1").innerHTML = '<iframe src=' + randomVideo + ' width="300" height="300" frameborder="0" allowfullscreen></iframe>';
videos.splice(videos.indexOf(randomVideo), 1)

var randomVideo = videos[Math.floor(Math.random() * videos.length)];
document.getElementById("video_2").innerHTML = '<iframe src=' + randomVideo + ' width="300" height="300" frameborder="0" allowfullscreen></iframe>';
videos.splice(videos.indexOf(randomVideo), 1)

var randomVideo = videos[Math.floor(Math.random() * videos.length)];
document.getElementById("video_3").innerHTML = '<iframe src=' + randomVideo + ' width="300" height="300" frameborder="0" allowfullscreen></iframe>';

//Manipulación de imagen con Canvas