document.addEventListener('DOMContentLoaded', () => {
    // 좋아요 토글
    document.querySelectorAll('.like-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const postDiv = btn.closest('.post');
            const postId = postDiv.dataset.postId;
            fetch(`/like/${postId}/`, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrftoken }
            })
            .then(res => res.json())
            .then(data => {
                btn.querySelector('.like-count').textContent = data.like_count;
                btn.querySelector('.like-icon').textContent = data.liked ? '❤️' : '🤍';
            });
        });
    });

    // 댓글 추가
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', e => {
            e.preventDefault();
            const postDiv = form.closest('.post');
            const postId = postDiv.dataset.postId;
            const input = form.querySelector('input[name="text"]');
            const text = input.value.trim();
            if (!text) return;

            fetch(`/comment/${postId}/add/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({ text })
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) return;
                const html = `
                    <div class="comment" data-comment-id="${data.comment_id}">
                        <strong>${data.username}</strong>: ${data.text}
                        <button class="delete-comment">❌</button>
                    </div>`;
                postDiv.querySelector('.comments').insertAdjacentHTML('beforeend', html);
                input.value = '';
            });
        });
    });

    // 댓글 삭제
    document.addEventListener('click', e => {
        if (!e.target.classList.contains('delete-comment')) return;
        const commentDiv = e.target.closest('.comment');
        const commentId = commentDiv.dataset.commentId;

        fetch(`/comment/${commentId}/delete/`, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken }
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) commentDiv.remove();
        });
    });
});