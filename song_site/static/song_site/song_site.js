
document.addEventListener('DOMContentLoaded', (event) => {

    const plusSign = document.getElementsByClassName("main_window_half_container")[0];
    const triangle = document.getElementsByClassName("main_window_half_container")[1];

    const searchMenu = document.getElementsByClassName("main_window_half_container_menu")[0];
    const randomSong = document.getElementsByClassName("main_window_half_container_menu")[1];

    console.log(triangle.style.marginTop);

    const add = document.getElementById("add");
    const addedSong = document.getElementById("addedSong");
    const added = document.getElementById("notFound");


    if(plusSign && triangle){

        if(plusSign.id != "song_list"){

            plusSign.addEventListener('mouseover', function() {

                plusSign.style.marginLeft = "222px";

            });

            plusSign.addEventListener('mouseout', function() {

                plusSign.style.marginLeft = "212px";

            });

            plusSign.addEventListener('click', function() {

                triangle.style.marginTop = "24%";

                plusSign.style.marginTop = "-500px";

            });


        }

        triangle.addEventListener('click', function() {
            triangle.style.marginTop = "-500px";

        });

        triangle.addEventListener('mouseover', function() {

            triangle.style.marginLeft = "222px";

        });

        triangle.addEventListener('mouseout', function() {

            triangle.style.marginLeft = "212px";

        });



    }

    if(add){

           add.addEventListener('mouseover', function() {

            add.style.marginLeft = "2%";

        });

        add.addEventListener('mouseout', function() {

            add.style.marginLeft = "0%";

        });

        add.addEventListener('click', function() {

            const list = document.getElementById("song_list");

            list.style.marginTop = "-500px";

            var videoData = document.getElementById('song').innerText;

            this.style.marginTop = "-500px";

            triangle.style.marginTop = "24%";

            setTimeout(function () {

                    document.getElementsByName('songData')[0].value = videoData;

                    document.getElementById('addForm').submit();

               }, 500);

        });

    }

    if(searchMenu){

        searchMenu.addEventListener('keydown', (event) => {

            if(event.key === 'Enter'){

                event.preventDefault();

                searchMenu.style.marginTop = "-500px";

                triangle.style.marginTop = "23%";

                setTimeout(function () {

                    document.getElementById('searchForm').submit();

                }, 500);

            }

        });

    }

    if(addedSong){

        addedSong.addEventListener('click', (event) => {

                event.preventDefault();

                addedSong.style.marginTop = "-500px";

                triangle.style.marginTop = "23%";

                console.log("SWITCHING WINDOWS");

                setTimeout(function () {

                    window.location.replace("/");

                }, 500);

        });

    }

    if(notFound){

        notFound.addEventListener('click', (event) => {

                event.preventDefault();

                notFound.style.marginTop = "-500px";

                triangle.style.marginTop = "23%";

                console.log("SWITCHING WINDOWS");

                setTimeout(function () {

                    window.location.replace("");

                }, 500);

        });

    }

});

