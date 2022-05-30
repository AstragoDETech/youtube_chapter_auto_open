import 'dart:html';
import 'dart:async';

void main() {
  var currentLoc = window.location.href;
  var lastLoc = '';

  Timer.periodic(Duration(milliseconds: 250), (timer) {
    currentLoc = window.location.href;

    // /// Print currentt location
    // window.console.log(currentLoc);

    /// Only run on change of Window Location
    if (currentLoc != lastLoc) {
      /// Only run on video link
      if (currentLoc.startsWith(RegExp(r'https:\/\/(w{3}|m).youtube.com\/watch'))) {
        /// Try to click the open chapter Button for 2.5 seconds
        Timer.periodic(Duration(milliseconds: 250), (timer) {
          if (timer.tick <= 10) {
            querySelector('.ytp-chapter-title-content')?.click();
          } else {
            timer.cancel();
          }
        });
      }
    }

    lastLoc = currentLoc;
  });
}

// querySelector('.ytp-chapter-title-content')!.click();