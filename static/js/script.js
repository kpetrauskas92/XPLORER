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

document.addEventListener('DOMContentLoaded', function() {

    let alerts = document.querySelectorAll('.alert');

    alerts.forEach(function(alert) {
        setTimeout(function() {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

function getCookie(name) {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function likePost(postId) {
    const csrftoken = getCookie('csrftoken');
    const likeButton = document.querySelector(`#like-form-${postId} .like-btn`);
    const heartIcon = document.querySelector(`#like-form-${postId} .like-btn i`);
    const likeCountElement = document.getElementById(`like-count-${postId}`);

    fetch(`/social/likepost/${postId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
    })
    .then(response => response.json())
    .then(data => {
        likeCountElement.innerText = data.likes_count;

        if (data.liked) {
            likeButton.classList.add('liked');
            heartIcon.classList.remove('far');
            heartIcon.classList.add('fas');
        } else {
            likeButton.classList.remove('liked');
            heartIcon.classList.remove('fas');
            heartIcon.classList.add('far');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function likeComment(commentId) {
    const csrftoken = getCookie('csrftoken');
    const likeButton = document.querySelector(`#comment-like-form-${commentId} .like-btn`);
    const heartIcon = document.querySelector(`#comment-like-form-${commentId} .like-btn i`);
    const likeCountElement = document.getElementById(`comment-like-count-${commentId}`);

    fetch(`/social/likecomment/${commentId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
    })
    .then(response => response.json())
    .then(data => {
        likeCountElement.innerText = data.likes_count;

        if (data.liked) {
            likeButton.classList.add('liked');
            heartIcon.classList.remove('far');
            heartIcon.classList.add('fas');
        } else {
            likeButton.classList.remove('liked');
            heartIcon.classList.remove('fas');
            heartIcon.classList.add('far');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}