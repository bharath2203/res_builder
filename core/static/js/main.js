function yearValidation(year) {
    var current_year = new Date().getFullYear();
    if (year > current_year) {
        alert("Year should not exceed " + current_year);
        return false;
    }
    return true;
}