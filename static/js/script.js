function togglePostForm(postFormRow) {
    let element = document.getElementById(postFormRow);

    if (element.classList.contains('d-none')) {
        element.classList.remove('d-none');
    } else {
        element.classList.add('d-none');
    }
}


function commentReplyToggle(commentId) {
    let replyInput = document.getElementById("reply-input-" + commentId);
    
    if (replyInput.classList.contains('d-none')) {
        replyInput.classList.remove('d-none');
    } else {
        replyInput.classList.add('d-none');
    }
}


function commentToggle(postId) {
    let commentsSection = document.getElementById("comments-" + postId);

    if (commentsSection.classList.contains('d-none')) {
        commentsSection.classList.remove('d-none');
    } else {
        commentsSection.classList.add('d-none');
    }
}