function stick_header() {
    /*
    Changes the css of elements identified as "sticky header".
    :return: None
    */
    var header = document.getElementById("sticky_header");
    var header_contents = document.getElementById("header_contents");

    if (window.pageYOffset > 0) {  // if the position of the page is not at the top
        header.classList.add("sticky");  // appends the sticky class onto the sticky_header
        header_contents.classList.remove("enlarge_header");
        header_contents.classList.add("shrink_header");
    }
    else {
        header.classList.remove("sticky");  // removes the sticky class from the sticky_header
        header_contents.classList.remove("shrink_header");
        header_contents.classList.add("enlarge_header");
    }
}

