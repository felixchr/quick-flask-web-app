$(document).ready(function(){
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        var target = $(e.target).attr("href") // activated tab
        //alert(target);
    });
    $("#job_search_btn").click(function(){
        console.log("Job search button clicked!");
        cmd = 'list_job';
        data = {
            cmd: cmd,
            node_list: nodelist.value,
            job_id: jobid.value,
            user_id: userid.value,
        };
        gen_ajax(data, '/slurm/ajax/'+cmd);
    });
});
