$(document).ready(function() {
  // TODO make configurable
  const port = 8080;

  const load_chat = locale => {
    // remove the previous chat window, if any
    $( "#webchat" ).empty();

    // debug - don't preserve state upon page reload
    localStorage.clear();

    const socketUrl = `${location.protocol}//${location.hostname}:${port}`;
    const serverUrl = `${location.protocol}//${location.hostname}${location.port ? ':' + location.port : ''}`;

    WebChat.default.init({
      selector: "#webchat",
      interval: 1000, // 1000 ms between each message
      initPayload: "hello",
      customData: {}, // arbitrary custom data. Stay minimal as this will be added to the socket
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
