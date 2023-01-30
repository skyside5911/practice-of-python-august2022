jQuery(document).ready(function(){
    jQuery("[name='post_title']").css("width","95%").after(" <button id='format_title'>Format</button>");

    jQuery("#format_title").click(function(event) {
        var post_title = jQuery("[name='post_title']").val();
        // post_title = post_title.toLowerCase().replace(/\b[a-z]/g, function(letter) {
        //     return letter.toUpperCase();
        // });
        jQuery("[name='post_title']").val(post_title);
        event.preventDefault();
    });    
});
