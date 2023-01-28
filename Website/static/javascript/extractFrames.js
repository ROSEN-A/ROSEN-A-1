var ffmpeg = require('fluent-ffmpeg');

const path = require('path');

function screenshots(path,des) {

    ffmpeg(path)

      .screenshots({

        count:4,

        filename: "%i.jpg",

        folder:des

      });

  }

function getPath(filename){

    var absolutePath = path.resolve(filename);

    return absolutePath;

}
const file = "sample_video.mp4"

var absolutePath = getPath(file);

screenshots(absolutePath, ".");





