function gen_ajax(data, url='/ajax', target='result', async=true, timeout=30000) {
    if (target != ''){
        div1 = $('#' + target);
        // console.log('Show loading at ' + div1.id + '/' + div1.name)
        loading(div1);
        // console.log(typeof(div1))
    };
    data['a'] = new Date().getTime();
    var ret = null;
    $.ajax({
        /*
         for async: if it is true, the function calls will not wait. For any purpose need to
         return value, the async needs to be false in order to wait for the return value
        */
        'async': async,
        url: url,
        data: data,
        success: function (res) {
            if (target != ''){
                div1.html(res);
            }
            else{
                // console.log(res);
                ret = res;
                // console.log('ret is: ' + ret);
            }
        },
        error: function (res) {
            if (target != ''){
                div1.html(res);
            }
            else{
                ret = res
            }
        },
        timeout: timeout
    });
    if (target == '') {
        // the value will be returned only in case of async is false
        console.log('Returning: ' + ret);
        return ret;
    };
}

function gen_select_load(data, url = '/ajax', target_id = 'result') {
    data['a'] = new Date().getTime();
    $('#' + target_id).load(url, data);
}

function loading(d , txt='Loading...') {
    d.html('<div class="progress progress-striped active"> \
    <div class="progress-bar progress-bar-success" role="progressbar" \
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" \
         style="width: 100%;"> \
        <span>' + txt + '</span> \
    </div> \
</div>');
}
