"use strict";

var Alexa = require("alexa-sdk");

var handlers = {
  "OpenIntent": function () {
    this.response.speak("OK, I will open the door for you right now."); 
    this.emit(':responseReady');
  },
  "closeIntent": function (){
    this.response.speak("Sure, wait a second.");
    this.emit(':responseReady');
  },
  "LaunchRequest": function () {
    this.response.speak("Welcome to use the smart arm control system, please tell me where do you want to go?"); 
    this.emit(':responseReady');
  },
  "StopIntent": function() {
    this.response.speak("Process suspended, please tell me again where do you want to go?"); 
    this.emit(':responseReady');
  },
  "ControlIntent": function () {
    var mydestination = this.event.request.intent.slots.num.value;
    if (mydestination == 1) {
      this.response.speak("Ok, system processing, we will take you to the first floor.");
		}
    if (mydestination == 2) {
      this.response.speak("Ok, system processing, we will take you to the second floor.");
    }
    if (mydestination == 3) {
      this.response.speak("Ok, system processing, we will take you to the third floor.");
    }
    if (mydestination == 4) {
      this.response.speak("Ok, system processing, we will take you to the fourth floor.");
    }
    if (mydestination == 5) {
      this.response.speak("Ok, system processing, we will take you to the fifth floor.");
    }
    if (mydestination == 6) {
      this.response.speak("Ok, system processing, we will take you to the sixth floor.");
    }
    if (mydestination == 7) {
      this.response.speak("Ok, system processing, we will take you to the seventh floor.");
    }
    if (mydestination == 8) {
      this.response.speak("Ok, system processing, we will take you to the eighth floor.");
    }
    if (mydestination == 9) {
      this.response.speak("Ok, system processing, we will take you to the ninth floor.");
    }
    if (mydestination == 10) {
      this.response.speak("Ok, system processing, we will take you to the tenth floor.");
    }
    if (mydestination == 11) {
      this.response.speak("Ok, system processing, we will take you to the eleventh floor.");
    }
    if (mydestination == 12) {
      this.response.speak("Ok, system processing, we will take you to the twelveth floor.");
    }
    if (mydestination == 13) {
      this.response.speak("Ok, system processing, we will take you to the thirteenth floor.");
    }
    if (mydestination == 14) {
      this.response.speak("Ok, system processing, we will take you to the fourteenth floor.");
    }
    if (mydestination == 15) {
      this.response.speak("Ok, system processing, we will take you to the fifteenth floor.");
    }
    if (mydestination == 16) {
      this.response.speak("Ok, system processing, we will take you to the sixteenth floor.");
    }
    if (mydestination == 17) {
      this.response.speak("Ok, system processing, we will take you to the seventeenth floor.");
    }
    if (mydestination == 18) {
      this.response.speak("Ok, system processing, we will take you to the eighteenth floor.");
    }
    if (mydestination == 19) {
      this.response.speak("Ok, system processing, we will take you to the nineteenth floor.");
    }
    if (mydestination >19 ) {
      this.response.speak("Ok, system processing, we will take you to that floor.");
    }
    this.emit(':responseReady');
  },
};

exports.handler = function(event, context, callback){
  var alexa = Alexa.handler(event, context);
    alexa.registerHandlers(handlers);
    alexa.execute();
};
