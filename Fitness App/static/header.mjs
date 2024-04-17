function stick_header() {
    /*
    Changes the css of elements identified as "sticky header".
    :return: None
    */
    var header = document.getElementById("sticky_header");
    var logo = document.getElementById("sub-menu icon");

    if (window.pageYOffset > 0) {  // if the position of the page is not at the top
        header.classList.add("sticky");  // appends the sticky class onto the sticky_header
        logo.classList.remove("enlarge_logo");
        logo.classList.add("shrink_logo");
    }
    else {
        header.classList.remove("sticky");  // removes the sticky class from the sticky_header
        logo.classList.remove("shrink_logo");
        logo.classList.add("enlarge_logo");
    }
}

