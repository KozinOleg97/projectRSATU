function sendMessage() {
    console.log("qwe");

    let mess_params = new FormData();
    console.log(this.message_text.textContent);
    mess_params.append("text", this.message_text.textContent);
    mess_params.append("chat", appData.chat_id.val());
    mess_params.append("author", appData.author.val());
    mess_params.append("dateTime", '0');

    let url = 'chats/' + appData.chat_id;

    $.post(url, {text: this.message_text}, onAjaxSuccess);

    $.get({
        url: 'chats/' + appData.chat_id,
        data: mess_params,
    })


    console.log("qwe");
}


function onAjaxSuccess(data) {
    // Здесь мы получаем данные, отправленные сервером и выводим их на экран.
    alert(data);
}