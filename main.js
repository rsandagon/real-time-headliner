function getJSON(url, callbackFunction) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            try {
                var responseData = JSON.parse(xmlhttp.responseText);
            } catch(error) {
                return;
            }
            callbackFunction(responseData);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}


document.addEventListener('DOMContentLoaded', (event) => {
    var container = document.getElementById("newsContainer");

    getJSON('news.json', function(data) {
        data.forEach(function (repo) {
            var child = `
                <h1 class="text-6xl font-bold mt-16">
                      <a href='${repo.url}'>${repo.headline}</a>
                </h1>
            `;
            container.insertAdjacentHTML('beforeend', child);
        });
    });
});
