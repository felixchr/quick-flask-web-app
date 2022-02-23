$(document).ready(function(){
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        var target = $(e.target).attr("href") // activated tab
        //alert(target);
    });
    $("#jupyter_proxy_btn").click(function(){
        console.log("Proxy btn clicked!");
        cmd = 'list_job';
        iframe = $('#proxy_frame')
    });
});
