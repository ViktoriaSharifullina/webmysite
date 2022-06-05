$(document).ready(function (e) {
          // отслеживаем событие отправки формы
          $('#commentForm').submit(function () {
              $.ajax({
                  data: $(this).serialize(),
                  type: $(this).attr('method'),
                  success: function (response) {

                    let result = response["result"];
                    let name = result["name"];
                    let email = result["email"];
                    let body  = result["body"];
                    let created  = result["created"];
                    html = "<div class='card' style='width: 500px;'>"+
                           "<div class='card-header'>" + name +"&#160;"+ created + "</div>"+
                           "<div class='card-body'>"+
                           "<p class='card-text'>"+ body + "</p>"+
                           "</div>"+
                           "</div>"
                    $(".new_comment").append(html);
                  },
                  error: function (response) {
                      alert(response.responseJSON.errors);
                      console.log(response.responseJSON.errors)

                  }
              });
              return false;
          });
      })