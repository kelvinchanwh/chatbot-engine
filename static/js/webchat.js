$(document).ready(function() {

  const load_chat = lang => {
    // remove the previous chat window, if any
    $( "#webchat" ).empty();

    // debug - don't preserve state upon page reload
    localStorage.clear();

    // Support TLS-specific URLs, when appropriate.
    if (window.location.protocol == "https:") {
        var ws_scheme = "wss:";
    } else {
        var ws_scheme = "ws:"
    };


    const socketUrl = `${ws_scheme}//${location.hostname}${location.port ? ':' + location.port : ''}`;
    const serverUrl = `${location.protocol}//${location.hostname}${location.port ? ':' + location.port : ''}`;
console.log(socketUrl);
    WebChat.default.init({
      selector: "#webchat",
      interval: 1000, // 1000 ms between each message
      initPayload: "utter_welcome",
      customData: { 'lang': lang }, // arbitrary custom data. Stay minimal as this will be added to the socket
      socketUrl: socketUrl,
      socketPath: "/socket.io/",
      title: "Let's talk!",
      subtitle: "Practise your vocabulary!",
      inputTextFieldHint: "Type a message...",
      connectingText: "Waiting for server...",
      hideWhenNotConnected: false,  // TODO true
      fullScreenMode: false,
      profileAvatar: serverUrl + "/static/images/avatar.png",
      params: {
        storage: "local"
      }
    });
    WebChat.open();
  };
  // Load the default chat in English
  load_chat('en');

  $("#choice_en").click(function() {
      load_chat('en');
  });

  $("#choice_de").click(function() {
      load_chat('de');
  });
});
