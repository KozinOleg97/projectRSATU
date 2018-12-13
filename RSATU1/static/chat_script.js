function sendMessage() {
    console.log("qwe");
    var mess_params = new FormData();
    mess_params.append("text", this.message_text)
    mess_params.append("chat", appData.chat_id)
    mess_params.append("author", appData.author)
    mess_params.append("dateTime", '0')

    $.get({
        url: 'chats/' + appData.chat_id,
        data: mess_params,
    })


    console.log("qwe");
}

