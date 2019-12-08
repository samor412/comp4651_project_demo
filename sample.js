const fetch = require("node-fetch");

// construct the URL to post to a publication
const LOGIN_URL = `http://127.0.0.1:5000/login/`;
const LOGIN_WITH_ACCESS_TOKEN_URL = `http://127.0.0.1:5000/login_with_new_access_token`;
const SIGNUP_URL = `http://127.0.0.1:5000/signup`;
const POST_NEW_COMMENT_URL = `http://127.0.0.1:5000/post_new_comment`;
const POST_NEW_POST_URL = `http://127.0.0.1:5000/post_new_post`;
const FETCH_COMMENT_URL = `http://127.0.0.1:5000/fetch_comment`;
const FETCH_LATEST_POST_URL = `http://127.0.0.1:5000/fetch_latest_post`;
const UPVOTE_POST_URL = `http://127.0.0.1:5000/upvote_post`;
const UPVOTE_COMMENT_URL = `http://127.0.0.1:5000/upvote_comment`;

async function login(username, password) {
    try {
        const response =  await fetch(LOGIN_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                username: username,
                password: password,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function loginWithAccessToken(user_id, access_token) {
    try {
        const response =  await fetch(LOGIN_WITH_ACCESS_TOKEN_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                user_id: user_id,
                access_token: access_token,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function signup(username, password, first_name, last_name) {
    try {
        const response =  await fetch(SIGNUP_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                username: username,
                password: password,
                first_name: first_name,
                last_name: last_name,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function postNewPost(user_id, title, content) {
    try {
        const response =  await fetch(POST_NEW_POST_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                user_id: user_id,
                title: title,
                content: content,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function postNewComment(user_id, post_id, content) {
    try {
        const response =  await fetch(POST_NEW_COMMENT_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                user_id: user_id,
                post_id: post_id,
                content: content,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function fetchComment(post_id, first_n_comment, num_of_comments) {
    try {
        const response =  await fetch(FETCH_COMMENT_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                post_id: post_id,
                first_n_comment: first_n_comment,
                num_of_comments: num_of_comments,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function fetchLatestPost(first_n_post, num_of_posts) {
    try {
        const response =  await fetch(FETCH_LATEST_POST_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                first_n_post: first_n_post,
                num_of_posts: num_of_posts,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}


async function upvotePost(post_id) {
    try {
        const response =  await fetch(UPVOTE_POST_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                post_id: post_id,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}

async function upvoteComment(comment_id) {
    try {
        const response =  await fetch(UPVOTE_COMMENT_URL, {
            method: "post",
            headers: {
                // "Authorization": `Bearer ${MEDIUM_ACCESS_TOKEN}`,
                "Content-type": "application/json",
                "Accept": "application/json",
                "Accept-Charset": "utf-8"
            },
            body: JSON.stringify({
                comment_id: comment_id,
            })
        })
        const responseJSON = await response.json();
        console.log(responseJSON)
    } catch(e) {
        console.log(e)
    }
}


// Test Function

// signup('test6', '123123', 'Dai Ming5', 'Chan')
// login('test5', '123123')
// loginWithAccessToken('1', 'fe87ec7fb12443f53131821d1c02b4e88bcf00cd')  // check the access_code in db if test
// postNewPost("1", "I hate the course", "As mention")
// postNewComment("1", "1", " Ha Ha")
// fetchComment("1", "1", "4")
fetchLatestPost("1", "10")
// upvotePost("1")
// upvoteComment("1")
