$(document).ready(function () {
	
      $('.blog-nav').click(function(e) {     //'e' is shortcut for 'event'
   
           $('.blog-nav-item').removeClass('.active:after');
   
           var $this = $(this);
           if (!$this.hasClass('active')) {
               $this.addClass('active:');
           }
          // e.defaultPrevented;
      });
 });

// // function send_form(){
// //     Dajaxice.examples.send_form(Dajax.process,{'form':$('#my_form').serialize(true)});

  $('#likes').click(function(){
  var artid;
  artid = $(this).attr("data-artid");
  $.get('/entry/',{id: artid}, function(data){
             $('#like_count').html(data);
             $('#likes').hide();
             console.log("bbbb");
    });
});



      $('a.link').click(function() {
        console.log("xxxxx");
        var pageId; 
        pageId = $('#this_url').attr('class')
        $.get(/entry/, {id:pageId},function(data){
     
      
      console.log("aaaaa");

      });
      
 })   


// });






// });







   // $('#dynamic-form').click(function(){
   //      console.log('am i called');
  
   //        $.ajax({
   //            type: "POST",
   //            url: "/create/",
   //            dataType: "json",
   //            data: { "item": $("#dynamic-form").val() },
   //            success: function(data) {
   //                alert(data.message);
   //            }
   //        });
  
   //     });
   // });
  




// $(document).on('submit', 'form.dynamic-form', function(form) {
//   var $form = $(form);
//   $.ajax({
//     type: form.method,
//     url: form.action,
//     data: $form.serialize(),
//     success: function(data) {
//       $form.replace(data);
//       console.log("success");
//     			}
//   			});
// 		});
// 	});
// });

   

// Submit post on submit
// function create_post() {
//         console.log("create post is working!") // sanity check
//         $.ajax({
//             url : "create", // the endpoint
//             type : "POST", // http method
//             data : json_post_data, // data sent with the post request
//             // handle a successful response
//             success : function(json) {
//                 $('#post-text').val(''); // remove the value from the input
//                 // another sanity check
//             },
//             // handle a non-successful response
//             error : function(xhr,errmsg,err) {
//                 $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//             },
//         });
//     };


//     var form_ajax = '#form-ajax';

// $.ajax({
//     url: "{% url 'create' %}",
//     type: "POST",
//     data: $(form_ajax).serialize(),
//     success: function(data) {
//         if (!(data['success'])) {
//             // Here we replace the form, for the
//             $(form_ajax).replaceWith(data['form-html']);
//         }
//         else {
//             // Here you can show the user a success message or do whatever you need
//             $(form_ajax).find('.success-message').show();
//         }
//     },
//     error: function () {
//         $(form_ajax).find('.error-message').show()
//     }
// });
// $('#form_ajax').ajaxForm({
//     success: function(responseText) {
//         var newMessages = $(responseText).find('.hidden-messages').html();
//         $('#messages').append(newMessages);
//     },
// });
// });
