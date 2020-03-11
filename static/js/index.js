"use strict";
// creating a border around an image during hover

$("img").hover(
  function () {
    $(this).css("border", "1px solid black");
  },
  function () {
    $(this).css("border", "1px none");
  }

);

// <div class="carousel" data-interval="10000">

