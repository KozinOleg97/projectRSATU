function sendMessage() {
    console.log("in");

    let mess_params = new FormData();
    console.log(this.message_text.value);
    mess_params.append("text", this.message_text.value);
    mess_params.append("chat", '' + appData.chat_id);
    mess_params.append("author", '' + appData.author);
    mess_params.append("dateTime", '0');

    let url = '/chats/' + appData.chat_id;


    $.ajax({
        url: '',
        data: mess_params,
        processData: false,
        contentType: false,
        type: 'POST',
        dataType: 'JSON',
        success: function (data) {
            onAjaxSuccess(data)
        }
    });

    //$.post(url, mess_params, onAjaxSuccess);
    //console.log("post");

    /*$.get({
        url: 'chats/' + appData.chat_id,
        data: mess_params,
    })*/


    console.log("qwe");
}


function onAjaxSuccess(data) {
    $("#visible_message_list ul").append('<li> ' + data.key + '--' + data.value + ' </li>');


}