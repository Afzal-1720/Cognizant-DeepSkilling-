import { useParams } from "react-router-dom";

import courses from "../data";

function CourseDetailPage(){

    const { courseId } = useParams();

    const course = courses.find(

        course =>

        course.id === Number(courseId)

    );

    if(!course){

        return(

            <h2>

                Course Not Found

            </h2>

        );

    }

    return(

        <div className="container">

            <h1>

                Course Details

            </h1>

            <h2>{course.name}</h2>

            <p>Code : {course.code}</p>

            <p>Credits : {course.credits}</p>

            <p>Grade : {course.grade}</p>

        </div>

    );

}

export default CourseDetailPage;