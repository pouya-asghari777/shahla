// Get all dropdowns from the ducument
const dropdowns = document.querySelectorAll('.dropdown');

// Loop through all dropdown elements
dropdowns.forEach(dropdown => {
    // Get inner elements from each dropdown
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');


    /*
    We are using this method in order to have 
    multiple dropdown menus on the page work
    */

    // Add a click events to the select elements
    select.addEventListener('click', () => {
        // Add the clicked select styles to the select elements
        select.classList.toggle('select-clicked');
        // Add the rotate styles to the caret elements
        caret.classList.toggle('caret-rotate');
        // Add the open styles to the menu elements
        menu.classList.toggle('menu-open');
    });

    // Loop through all options elements 
    options.forEach(option => {
        // Add a click event to the options elemet
        option.addEventListener('click', () => {
            // Change selected inner text to clicked option inner text
            selected.innerText = option.innerText;
            // Add the clicked select styles to the select elements
            select.classList.remove('select-clicked');
            // Add the rotate styles to the caret elements
            caret.classList.remove('caret-rotate');
            // Add the open styles to the menu elements
            menu.classList.remove('menu-open');
            // Remove active class from all option elements
            options.forEach(option => {
                option.classList.remove('active');
            });
            option.classList.add('active');
        });
    });
});