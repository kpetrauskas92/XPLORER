function togglePostForm(postFormRow) {
    let element = document.getElementById(postFormRow);

    if (element.classList.contains('d-none')) {
        element.classList.remove('d-none');
    } else {
        element.classList.add('d-none');
    }
}


function commentReplyToggle(parent_id) {
    let row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}