

function getArtist(){
   fetch('https://musicdemons.com/api/v1/slayer')
   .then(function(response) {
     return response.json();
   })
   .then(function(myJson) {
     console.log(JSON.stringify(myJson));
   })
 
};

function UserAction() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
             alert(this.responseText);
         }
    };
    xhttp.open("POST", "https://api.lyrics.ovh/v1/ + 'artist' + '/' + 'song'", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send("Your JSON Data Here");
}


console.log(getArtist());