const name = document.getElementById("calluser");
const uscontact = document.getElementById("uscontact");
const text = document.getElementById("mymes");

const botToken = "5183960744:AAGFAD-gDPrSc_OnZhliPYsdZ_A2UPiBn8g";
const chatID = "-1001532655583";

document.getElementById("myForm").addEventListener('submit', function (event) {

    if(!name.validity.valid || !uscontact.validity.valid || !text.validity.valid) {
      alert("Invalid input!");
      event.preventDefault();
    }
      
    else{
       var message = `<b>New feedback</b>%0AFrom: <i>${uscontact.value}</i>%0AFeedback text: ${text.value}`;
       var URL = `https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatID}&text=${message}&parse_mode=html`;
       console.log(URL);
       httpGetAsync(URL, function(message){console.log(message)});
       event.preventDefault(); 
    }  
  });
