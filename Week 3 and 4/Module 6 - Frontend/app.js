import { courses } from "./data.js";

/* ==========================================
   STEP 30 - Destructuring
========================================== */

for (const course of courses) {
    const { name, credits } = course;
    console.log(name, credits);
}

/* ==========================================
   STEP 31 - map()
========================================== */

const formattedCourses = courses.map(course =>
    `${course.code} - ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);

/* ==========================================
   STEP 32 - filter()
========================================== */

const filteredCourses = courses.filter(
    course => course.credits >= 4
);

console.log(filteredCourses);
console.log("Count:", filteredCourses.length);

/* ==========================================
   STEP 33 - reduce()
========================================== */

const totalCredits = courses.reduce(
    (total, course) => total + course.credits,
    0
);

console.log("Total Credits:", totalCredits);

/* ==========================================
   STEP 34 - Arrow Function
========================================== */

courses.forEach(course =>
    console.log(`${course.code} - ${course.name}`)
);

/* ==========================================
   STEP 35 - Select DOM Elements
========================================== */

const courseGrid = document.querySelector(".course-grid");
const totalCreditsText = document.querySelector("#total-credits");
const searchInput = document.querySelector("#search-courses");
const sortButton = document.querySelector("#sort-btn");
const selectedCourse = document.querySelector("#selected-course");

/* ==========================================
   HANDS-ON 9
   Accessibility Elements
========================================== */

const resultCount = document.querySelector("#resultCount");

/* ==========================================
   Function : Render Courses
========================================== */

/* ==========================================
   Function : Render Courses
========================================== */

function renderCourses(courseList) {

    courseGrid.innerHTML = "";

    courseList.forEach(course => {

        const card = document.createElement("article");

        card.className = "course-card";

        card.dataset.id = course.id;

        /* STEP 129 */

        card.setAttribute("tabindex", "0");

        card.setAttribute("role", "button");

        card.setAttribute(
            "aria-label",
            `${course.name} course`
        );

        card.innerHTML = `
            <h3>${course.name}</h3>

            <p><strong>Code:</strong> ${course.code}</p>

            <p><strong>Credits:</strong> ${course.credits}</p>

            <p><strong>Grade:</strong> ${course.grade}</p>
        `;

        /* Keyboard Support */

        card.addEventListener("keydown", function (event) {

            if (event.key === "Enter") {

                card.click();

            }

        });

        courseGrid.appendChild(card);

    });

    /* Update total credits */

    const total = courseList.reduce(

        (sum, course) => sum + course.credits,

        0

    );

    totalCreditsText.textContent =
        `Total Credits Enrolled : ${total}`;

    /* STEP 130 */

    resultCount.textContent =
        `${courseList.length} courses found`;

}
/* ==========================================
   Initial Rendering
========================================== */

renderCourses(courses);

/* ==========================================
   STEP 40 & 41 - Search Courses
========================================== */

searchInput.addEventListener("input", () => {

    const searchText =
        searchInput.value.toLowerCase();

    const filtered =
        courses.filter(course =>

            course.name
                .toLowerCase()
                .includes(searchText)

        );

    renderCourses(filtered);

});

/* ==========================================
   STEP 42 - Sort By Credits
========================================== */

sortButton.addEventListener("click", () => {

    courses.sort((a, b) => b.credits - a.credits);

    renderCourses(courses);

});

/* ==========================================
   STEP 43 & 44 - Event Delegation
========================================== */

courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const id = Number(card.dataset.id);

    const course = courses.find(course => course.id === id);

    selectedCourse.textContent =
        `Selected Course : ${course.name} | Grade : ${course.grade}`;

    // If workbook specifically wants an alert, uncomment:
    alert(`${course.name} - Grade: ${course.grade}`);

});

// Step 45
function fetchUser(id){

    fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then(response=>response.json())
    .then(user=>{

        console.log(user.name);

    });

}

fetchUser(1);

// Step 46
async function fetchUserAsync(id){

    try{

        const response = await fetch(
            `https://jsonplaceholder.typicode.com/users/${id}`
        );

        const user = await response.json();

        console.log(user.name);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(1);

// Step 47
function fetchAllCourses(){

    return new Promise(resolve=>{

        setTimeout(()=>{

            resolve(courses);

        },1000);

    });

}

// Step 48
const loading = document.querySelector("#loading");

async function loadCourses(){

    loading.textContent="Loading courses...";

    const courseData = await fetchAllCourses();

    loading.textContent="";

    renderCourses(courseData);

}

loadCourses();

// Step 49
Promise.all([

    fetch("https://jsonplaceholder.typicode.com/users/1")
    .then(response=>response.json()),

    fetch("https://jsonplaceholder.typicode.com/users/2")
    .then(response=>response.json())

])

.then(users=>{

    console.log(users[0].name);

    console.log(users[1].name);

});


const notificationList =
document.querySelector("#notification-list");

const loadingPosts =
document.querySelector("#loading-posts");

async function apiFetch(url){

    const response=await fetch(url);

    if(!response.ok){

        throw new Error(

            `HTTP Error : ${response.status}`

        );

    }

    return await response.json();

}

async function loadPosts(){

    loadingPosts.textContent="Loading Posts...";

    try{

        const posts=await apiFetch(

            "https://jsonplaceholder.typicode.com/posts"

        );

        loadingPosts.textContent="";

        notificationList.innerHTML="";

        posts.slice(0,5).forEach(post=>{

            const card=document.createElement("div");

            card.className="notification-card";

            card.innerHTML=`
                <h3>${post.title}</h3>
                <p>${post.body}</p>
            `;

            notificationList.appendChild(card);

        });

    }

    catch(error){

        loadingPosts.textContent="";

        notificationList.innerHTML=`

            <p style="color:red;">

            ${error.message}

            </p>

            <button id="retry-btn">

            Retry

            </button>

        `;

        document.querySelector("#retry-btn")

        .addEventListener("click",loadPosts);

    }

}

loadPosts();

/* =========================================
   Axios Request Interceptor
========================================= */

axios.interceptors.request.use(config => {

    console.log("API Call Started:", config.url);

    return config;

});

/* =========================================
   Axios Version of apiFetch()
========================================= */

async function apiFetchAxios(url){

    const response = await axios.get(url);

    return response.data;

}

/* =========================================
   Fetch User 1 Posts
========================================= */

async function loadAxiosPosts(){

    try{

        const posts = await axios.get(

            "https://jsonplaceholder.typicode.com/posts",

            {

                params:{

                    userId:1

                }

            }

        );

        console.log("Axios Posts");

        console.log(posts.data);

    }

    catch(error){

        console.log(error.message);

    }

}

loadAxiosPosts();

/*
========================================
Fetch vs Axios
========================================

1. Fetch requires response.ok checking.
   Axios automatically throws errors.

2. Fetch requires response.json().
   Axios automatically parses JSON.

3. Fetch is built into browsers.
   Axios is an external library with
   interceptors, timeout and more features.

*/