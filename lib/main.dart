import 'dart:html';
import 'dart:async';

void main() {
  var currentLoc = window.location.href;
  var lastLoc = '';

  Timer.periodic(Duration(milliseconds: 250), (timer) {
    currentLoc = window.location.href;

    // window.console.info('C: $currentLoc  -  L: $lastLoc');

    if (currentLoc != lastLoc) {
      Timer.periodic(Duration(milliseconds: 250), (timer) {
        if (timer.tick <= 10) {
          // window.console.info('--- RUN QS CLICK --');

          querySelector('.ytp-chapter-title-content')?.click();
        } else {
          timer.cancel();
        }
      });
    }
    lastLoc = currentLoc;
  });
}

// querySelector('.ytp-chapter-title-content')!.click();