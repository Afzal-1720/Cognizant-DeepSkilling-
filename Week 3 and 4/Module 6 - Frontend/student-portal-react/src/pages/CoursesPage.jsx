import CourseCard from "../components/CourseCard";

import courses from "../data";

import { useDispatch } from "react-redux";

import { fetchAllCourses }

from "../redux/enrollmentSlice";

function CoursesPage(){

    return(

        <div className="container">

            <h2>Available Courses</h2>

            <div className="grid">

                {

                    courses.map(course=>(

                        <CourseCard

                            key={course.id}

                            {...course}

                        />

                    ))

                }

            </div>

        </div>

    );

}

export default CoursesPage;