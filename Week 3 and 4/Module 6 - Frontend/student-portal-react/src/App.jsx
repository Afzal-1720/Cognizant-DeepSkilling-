import { useEffect, useState } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import "./App.css";

function App() {

    const [courses, setCourses] = useState([]);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    const [searchTerm, setSearchTerm] = useState("");

    const [enrolledCourses, setEnrolledCourses] = useState([]);

    // Fetch courses when component loads
    useEffect(() => {

        fetchCourses();

    }, []);

    // Runs whenever courses change
    useEffect(() => {

        console.log("Courses Updated");

        console.log(courses);

    }, [courses]);

    async function fetchCourses() {

        try {

            const response = await fetch(
                "https://jsonplaceholder.typicode.com/posts"
            );

            if (!response.ok) {

                throw new Error("Unable to fetch courses");

            }

            const data = await response.json();

            const courseList = data.slice(0, 5).map(post => ({

                id: post.id,

                name: post.title,

                code: `CS10${post.id}`,

                credits: 4,

                grade: "A"

            }));

            setCourses(courseList);

        }

        catch (error) {

            setError(error.message);

        }

        finally {

            setLoading(false);

        }

    }

    function handleEnroll(course) {

        const alreadyExists = enrolledCourses.find(

            c => c.id === course.id

        );

        if (!alreadyExists) {

            setEnrolledCourses([

                ...enrolledCourses,

                course

            ]);

        }

    }

    const filteredCourses = courses.filter(course =>

        course.name

            .toLowerCase()

            .includes(searchTerm.toLowerCase())

    );

    if (loading) {

        return <h2>Loading Courses...</h2>;

    }

    if (error) {

        return <h2>{error}</h2>;

    }

    return (

        <>

            <Header

                siteName="Student Portal"

                count={enrolledCourses.length}

            />

            <div className="container">

                <input

                    type="text"

                    placeholder="Search Courses"

                    value={searchTerm}

                    onChange={(e) =>

                        setSearchTerm(e.target.value)

                    }

                />

                <div className="grid">

                    {

                        filteredCourses.map(course => (

                            <CourseCard

                                key={course.id}

                                {...course}

                                onEnroll={handleEnroll}

                            />

                        ))

                    }

                </div>

                <StudentProfile />

            </div>

            <Footer />

        </>

    );

}

export default App;